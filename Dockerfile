# Self-contained image for the LearnEVO help viewer.
#
# Used for the i2s111-CTDC4 deploy where the server has Docker but no
# git and no Python. Everything the viewer needs is baked in; updates
# are shipped by rebuilding the image here, saving to a tar file, and
# copying that one file to the server.
#
#   Build:    deploy/build-image.bat        (on the workstation)
#   Deploy:   deploy/update-server.bat      (on i2s111-CTDC4)
FROM python:3.12-alpine

WORKDIR /app/learnevo-help

# Copy the server first so later rebuilds that only touch content reuse
# this layer from cache.
COPY learnevo-help/server.py ./server.py

# Copy the viewer itself (prebuilt content + static assets).
COPY learnevo-help/index.html   ./index.html
COPY learnevo-help/css/         ./css/
COPY learnevo-help/js/          ./js/
COPY learnevo-help/content/     ./content/
COPY learnevo-help/data/        ./data/

ENV HOST=0.0.0.0 \
    PORT=8765 \
    NO_BROWSER=1 \
    PYTHONUNBUFFERED=1

EXPOSE 8765

CMD ["python", "server.py"]
