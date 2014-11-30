# Ansible playbooks for deploying a mezzanine application

This is an example that shows how to use Ansible to deploy a mezzanine site into
a Vagrant box.

## Preqs

You need to have installed:

* Ansible
* Vagrant
* Redis
* Python redis library

Redis and the Python redis library are because this has fact caching enabled.
You can turn off fact caching by editing ansible.cfg and commenting out the line:

    fact_caching = redis


## Running the playbook

To run it, do:

    vagrant up

Then point your browser to: http://192.168.33.10.xip.io or
https://www.192.168.33.10.xip.io. You'll get a security warning if you use the
https site since it's a self-signed certificate, this is normal.
