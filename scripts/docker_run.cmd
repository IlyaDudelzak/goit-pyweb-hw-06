@echo off
PUSHD ..\tests

docker run -it --rm  -v goit-pyweb-hw-06_volume:/app/db  --name web_hw_06  ilyadudelzak/goit-pyweb-hw-06

rem docker volume ls
                    

POPD