#!/usr/bin/env bash

find_internet() {
    result=$(
        curl \
            --silent \
            --output /dev/null \
            --write-out "%{http_code}" \
            https://www.google.com
    )

    if [ "${result}" == "200" ]; then
        INTERNET_FOUND='yes'

    else
        INTERNET_FOUND='no'

    fi
}

echo "${VAULT_PASSWORD}" > /root/.vault.password
echo "${PRIVILEGED_USER_SSH_KEY_B64}" | base64 -d > /root/ssh.key
chmod 600 /root/ssh.key
find_internet

cat <<EOF > /etc/ansible_hosts
[all:vars]
internet_found='${INTERNET_FOUND}'

[lab_onprem:children]
lab_onprem_docker
lab_onprem_nas

[lab_onprem_docker]
docker01 ansible_host='192.168.40.1'
docker02 ansible_host='192.168.40.2'
docker00 ansible_host='192.168.40.4'

[lab_onprem_nas]
nas ansible_host='192.168.40.5'

[lab_linode]
EOF

if [ "${INTERNET_FOUND}" == 'yes' ] || [ "${CYCLE_MODE}" == 'up' ]; then
    echo " "
    echo -e "[ \033[31m*\033[0m ] Adding Portal host to inventory"
    echo " "

    cat <<EOF >> /etc/ansible_hosts
portal ansible_host="{{ lookup('ansible.builtin.file', '/tfstate/instance_portal_ip_address.txt') }}"
EOF

else
    echo " "
    echo -e "[ \033[31m*\033[0m ] Ignoring Portal host for inventory"
    echo " "

fi

ansible all \
    --list-hosts
echo " "
