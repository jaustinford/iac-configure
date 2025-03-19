@echo off

cd ..\

docker compose ^
    --profile tunnels-off ^
    up ^
        --detach ^
        --force-recreate

docker compose ^
    --profile tunnels-off ^
    logs ^
        --follow ^
        --timestamps

pause
