#!/bin/sh

# make sure we are in this directory
test -f extra/cleanup.sh &&
    grep '0Hth9zfK2C5Py8ofplNCa7VGGrIeeQ38tUsJysXBeXV9' extra/cleanup.sh -q ||
    { echo >&2 wrong directory.; exit 1; }

rm -r src/sma/hm/classes src/sma/hm/tables
rm -r bin
rm gen/*
rm -r gen/__pycache__
rm metamodel/classes.gmf* metamodel/classes.genmodel metamodel/classes.trace
rm metamodel/tables.gmf* metamodel/tables.genmodel metamodel/tables.trace
rm -r ../sma.hm.diagram ../sma.hm.edit ../sma.hm.editor ../sma.hm.tests
