#!/usr/bin/env bash

echo "${VAULT_PASSWORD}" > /root/.vault.password
echo "${B64_SSH_KEY}" | base64 -d > /root/ssh.key
chmod 600 /root/ssh.key

cat <<EOF > /etc/ansible_hosts
[secrets:children]
elysianskies_onprem_docker
elysianskies_onprem_nas
elysianskies_linode

[elysianskies_onprem_docker]
docker01-teine.home.elysianskies.com ansible_host='172.16.17.2'
docker02-teine.home.elysianskies.com ansible_host='172.16.17.3'
docker03-teine.home.elysianskies.com ansible_host='172.16.17.4'

[elysianskies_onprem_nas]
nas-teine.home.elysianskies.com ansible_host='172.16.17.5'

[elysianskies_linode]
EOF

if [ $(curl -s -o /dev/null -w "%{http_code}" https://www.google.com) == "200" ]; then
    echo " "
    echo -e "[ \033[31m*\033[0m ] Adding Portal host to inventory."
    echo " "

    cat <<EOF >> /etc/ansible_hosts
portal.elysianskies.com ansible_host="{{ lookup('ansible.builtin.file', '/tfstate/instance_portal_ip_address.txt') }}"
EOF

else
    echo " "
    echo -e "[ \033[31m*\033[0m ] Ignoring Portal host for inventory."
    echo " "

fi

ansible all \
    --list-hosts
echo " "
