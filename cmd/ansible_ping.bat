@echo off

cd ..\

docker compose ^
    --profile ping ^
    up ^
        --detach ^
        --force-recreate

docker compose ^
    --profile ping ^
    logs ^
        --follow ^
        --timestamps

pause
