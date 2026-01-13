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
    cp /automation/ansible-tmp-path.json /ansible-tmp-path.json

    chmod 600 \
        /ansible-vault-password \
        /iac-configure.key \
        /ansible-tmp-path.json
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
docker00 ansible_host='192.168.40.4' ansible_remote_tmp="{{ (lookup('ansible.builtin.file', '/ansible-tmp-path.json') | from_json)['docker00'] }}"
docker01 ansible_host='192.168.40.1' ansible_remote_tmp="{{ (lookup('ansible.builtin.file', '/ansible-tmp-path.json') | from_json)['docker01'] }}"
docker02 ansible_host='192.168.40.2' ansible_remote_tmp="{{ (lookup('ansible.builtin.file', '/ansible-tmp-path.json') | from_json)['docker02'] }}"

[lab_onprem_nas]
nas

[lab_onprem_nas:vars]
ansible_host='192.168.40.5'
ansible_remote_tmp="{{ (lookup('ansible.builtin.file', '/ansible-tmp-path.json') | from_json)['nas'] }}"

[lab_linode:vars]
ansible_host="{{ (lookup('ansible.builtin.file', '/tmp/portal.json') | from_json)['ip_address'] }}"
ansible_remote_tmp="{{ (lookup('ansible.builtin.file', '/ansible-tmp-path.json') | from_json)['portal'] }}"

[lab_linode]
EOF

if [ "${INTERNET_FOUND}" == 'yes' ] || [ "${CYCLE_MODE}" == 'up' ]; then
    cat <<EOF >> /etc/ansible_hosts
portal
EOF

fi

ansible all \
    --list-hosts
echo " "
