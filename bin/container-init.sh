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

convert_mounted_files() {
    cp /automation/ansible-vault-password /ansible-vault-password
    cp /automation/iac-configure.key /iac-configure.key

    chmod 600 \
        /ansible-vault-password \
        /iac-configure.key
}

find_internet
convert_mounted_files

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
    cat <<EOF >> /etc/ansible_hosts
portal ansible_host="{{ (lookup('ansible.builtin.file', '/tmp/portal.json') | from_json)['ip_address'] }}"
EOF

fi

ansible all \
    --list-hosts
echo " "
