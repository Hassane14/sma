#!/bin/sh

# make sure we are in this directory
test -f extra/cleanup.sh &&
    grep '0Hth9zfK2C5Py8ofplNCa7VGGrIeeQ38tUsJysXBeXV9' extra/cleanup.sh -q ||
    { echo >&2 wrong directory.; exit 1; }

rm -r src/sma/hm/classes
rm -r bin
rm gen/*
rm metamodel/classes.gmf* metamodel/classes.genmodel metamodel/classes.trace
rm -r ../sma.hm.{diagram,edit,editor,tests}
