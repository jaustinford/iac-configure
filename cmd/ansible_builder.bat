@echo off

cd ..\

docker compose ^
    --profile builder ^
    build

pause
