@echo off

cd ..\

docker compose ^
    --profile site ^
    up ^
        --detach ^
        --force-recreate

docker compose ^
    --profile site ^
    logs ^
        --follow ^
        --timestamps

pause
