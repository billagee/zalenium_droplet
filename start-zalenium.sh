#!/bin/bash -e

# Starts Zalenium in the foreground.
#
# Only listen on 127.0.0.1:4444 and 5555 so remote hosts
# can't access the hub without authenticating:
docker run --rm -it --name zalenium \
    -p 127.0.0.1:44444:4444 -p 127.0.0.1:55555:5555 \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v /tmp/videos:/home/seluser/videos \
    dosel/zalenium start
