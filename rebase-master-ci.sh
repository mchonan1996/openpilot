#!/bin/sh
set -e

git fetch upstream
git rebase --onto upstream/master-ci last-master-ci
git tag -f last-master-ci upstream/master-ci
git push --force-with-lease
