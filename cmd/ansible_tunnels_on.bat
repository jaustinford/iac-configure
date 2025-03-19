@echo off

cd ..\

docker compose ^
    --profile tunnels-on ^
    up ^
        --detach ^
        --force-recreate

docker compose ^
    --profile tunnels-on ^
    logs ^
        --follow ^
        --timestamps

pause
