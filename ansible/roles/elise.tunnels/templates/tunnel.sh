#!/usr/bin/env bash

autossh -N -T \
    -o ServerAliveInterval=30 \
    -o ServerAliveCountMax=960 \
    -o ExitOnForwardFailure=yes \
    -o StrictHostKeyChecking=no \
    -o UserKnownHostsFile=/dev/null \
    -i /root/tunnel-ssh.key \
    -R {{ item.external_port }}:{{ item.ipv4 }}:{{ item.internal_port }} \
    root@portal.{{ lab.domain }}
