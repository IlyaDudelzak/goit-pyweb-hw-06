@echo off
PUSHD %~dp0
docker build -t ilyadudelzak/goit-pyweb-hw-06 .
docker images
POPD