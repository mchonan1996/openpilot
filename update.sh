#!/bin/sh
set -e

git fetch origin
git reset --hard origin/p-master-ci
echo Rebooting...
reboot

