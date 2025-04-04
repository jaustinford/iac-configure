#!/usr/bin/env bash

echo "${VAULT_PASSWORD}" > /root/.vault.password
echo "${B64_SSH_KEY}" | base64 -d > /root/ssh.key
chmod 600 /root/ssh.key
