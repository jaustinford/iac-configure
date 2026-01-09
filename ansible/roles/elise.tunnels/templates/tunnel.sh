#!/usr/bin/env bash

autossh -N -T \
    -o ServerAliveInterval=30 \
    -o ServerAliveCountMax=960 \
    -o ExitOnForwardFailure=yes \
    -o StrictHostKeyChecking=no \
    -o UserKnownHostsFile=/dev/null \
    -i {{ folder_ssh_tunnels }}/ssh-tunnel.key \
    -R {{ item.external_port }}:{{ item.ipv4 }}:{{ item.internal_port }} \
    {{ names.users.host.associate }}@{{ names.hosts.portal }}.{{ lab.domain }}
