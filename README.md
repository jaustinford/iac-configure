# elysianskies-configure

 > started : 23.04.2024

_building the image_

```bash
 docker build -t elysianskies-configure:main .
 ```

 _executing site playbook_

 ```bash
 docker run --interactive --rm elysianskies-configure:main //bin/bash -c "echo '${LOCAL_VAULT_PASSWORD}' > //root/.vault.password ; ansible-playbook //etc/ansible/site.yml"
 ```

_managing the vault files_

 ```bash
 docker run --interactive --rm elysianskies-configure:main //bin/bash -c "echo '${LOCAL_VAULT_PASSWORD}' > //root/.vault.password ; ansible-vault decrypt //etc/ansible/group_vars/all.yml --output -"
 ```
