# Minimal image for the LearnEVO help viewer.
#
# Only server.py is baked into the image. The rest of learnevo-help/
# (content, data, css, js, index.html, glossary.py, build.py) is expected
# to be bind-mounted at /app/learnevo-help so that `git pull` on the host
# updates the served content with no image rebuild.
#
# Rebuild the image only when server.py, Python version, or system deps
# change:
#     docker compose up -d --build
FROM python:3.12-alpine

WORKDIR /app/learnevo-help

# Bake only the server. Content comes from the bind-mount at runtime.
COPY learnevo-help/server.py ./server.py

ENV HOST=0.0.0.0 \
    PORT=8765 \
    NO_BROWSER=1 \
    PYTHONUNBUFFERED=1

EXPOSE 8765

CMD ["python", "server.py"]
