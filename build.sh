#!/usr/bin/env sh

export JEKYLL_VERSION=latest
docker run --rm \
  --volume="$PWD:/srv/jekyll:Z" \
  -it jekyll/jekyll:$JEKYLL_VERSION \
  jekyll build