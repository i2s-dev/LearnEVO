# Deploy — LearnEVO help viewer → `i2s111-CTDC4`

This folder contains everything needed to run the help viewer on a
Docker-only Windows server that has **no git and no Python** — just
Docker.

The flow is:

1. **On the workstation**, build an image and save it to a tar file.
2. **Copy three files** to the server.
3. **On the server**, run one script to load and start the container.

After the first deploy, updates only require copying a fresh
`evo-help.tar` over and re-running the same script.

---

## One-time setup

### On the workstation

```cmd
deploy\build-image.bat
```

This runs `learnevo-help\build.py` to regenerate content, builds the
Docker image, and saves it to `deploy\evo-help.tar` (≈ 65 MB, gitignored).

### Copy to the server (`i2s111-CTDC4`)

Create `C:\deploy\evo-help\` on the server (SMB, RDP, or any transfer)
and drop in these three files:

| File | Where it comes from |
|------|---------------------|
| `evo-help.tar` | `deploy\evo-help.tar` on the workstation |
| `docker-compose.yml` | repo root (unchanged, checked into git) |
| `update-server.bat` | `deploy\update-server.bat` (this folder) |

### First run on the server

Open a command prompt as a user with Docker permissions:

```cmd
cd C:\deploy\evo-help
update-server.bat
```

### Windows Firewall (one time, admin PowerShell on the server)

```powershell
New-NetFirewallRule -DisplayName "LearnEVO Help" -Direction Inbound ^
    -Protocol TCP -LocalPort 8765 -Action Allow -Profile Domain
```

### Verify

Anyone on the LAN can now hit:

```
http://i2s111-ctdc4:8765/
```

`docker-compose.yml` sets `restart: unless-stopped`, so the container
survives server reboots.

---

## Updating content (the common case)

Whenever you want to publish new docs / glossary / styles:

### On the workstation

```cmd
deploy\build-image.bat
```

### Move the new tar to the server

Overwrite `C:\deploy\evo-help\evo-help.tar` on the server with the new
one from `deploy\evo-help.tar`.

### On the server

```cmd
cd C:\deploy\evo-help
update-server.bat
```

That's the whole loop. `docker-compose.yml` and `update-server.bat`
don't need to be re-copied unless they themselves change.

---

## What gets moved vs. what stays

| Moved each update | Never moved to the server |
|---|---|
| `evo-help.tar` (≈ 65 MB — whole viewer, prebuilt) | `docs/`, `samples/`, `scripts/`, `research/`, `.git/`, Python, build tools |

No git, no Python, no source code touches the server. Everything the
container needs is inside the tar.

---

## Anatomy of the image

- Base: `python:3.12-alpine` (~55 MB).
- Adds: `learnevo-help/server.py` + prebuilt `content/`, `data/`, `css/`,
  `js/`, and `index.html`.
- Final image: ~65 MB.
- Runtime: stdlib only — no pip install, no extra packages.
- Env defaults (see [`../Dockerfile`](../Dockerfile)): `HOST=0.0.0.0`,
  `PORT=8765`, `NO_BROWSER=1`.
- Server sends `Cache-Control: no-store` on every response so LAN users
  never see stale CSS/JS after an update.

---

## Troubleshooting

**Port 8765 already in use on the server.** Something else is listening.
`netstat -ano | findstr :8765` — stop it, or change the published port in
`docker-compose.yml` (left side of `"8765:8765"`).

**`docker compose` not recognized.** You're on the old standalone
`docker-compose` (Python). Edit `update-server.bat` and replace
`docker compose` with `docker-compose`. Long-term, install Docker CLI
plugin.

**Stale image served after update.** `update-server.bat` uses
`--force-recreate`, so this shouldn't happen. If it does:
`docker compose down && docker compose up -d`.

**`docker load` complains about disk space.** The tar unpacks to a few
hundred MB of layers. Free space under `C:\ProgramData\Docker\` or move
Docker's data-root.
