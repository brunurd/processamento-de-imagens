#!/usr/bin/env bash

set -e

coverage run -m pytest \
    --junitxml=./tests_report/junit.xml \
    -s --maxfail=1

coverage report --fail-under=80 -m

coverage html -d tests_report

