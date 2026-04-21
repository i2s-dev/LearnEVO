# Kill any previously-launched LearnEVO help server.
#
# Why this exists:
# A zombie Python server from an earlier session can keep its port bound
# AND, more insidiously, keeps Edge/Chromium serving the stale CSS/JS it
# cached from that old session. Launching a new server on a different
# port does not help because the browser never revalidates the cached
# entries. We kill every python.exe whose command line looks like one of
# our launches before starting fresh.
#
# Safe to run when no server is listening — errors are swallowed.

Get-CimInstance Win32_Process -Filter "Name='python.exe'" |
    Where-Object {
        $_.CommandLine -like '*server.py*' -or
        $_.CommandLine -like '*http.server*876*'
    } |
    ForEach-Object {
        Write-Host "Stopping prior help server PID $($_.ProcessId)"
        Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue
    }
