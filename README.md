# iac-configure

This project uses Ansible to configure the host and container infrastructure that comprise the lab. The pipeline executes a `playbook_site` job which runs the [`site.yml`](https://cicd.pendragonlab.com/elise/infrastructure/iac-configure/-/blob/main/ansible/site.yml?ref_type=heads) playbook. Per Ansible's documentation, this is intended as the entrypoint playbook to launch the entire stack so that the full infrastructure is executed every time.

### references
- [Ansible Best Practices](https://docs.ansible.com/ansible/2.8/user_guide/playbooks_best_practices.html)
