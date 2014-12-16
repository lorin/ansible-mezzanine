# Ansible playbooks for deploying a mezzanine application

This is an example that shows how to use Ansible to deploy a mezzanine site into
a Vagrant box.

## Preqs

You need to have installed:

* Ansible
* Vagrant
* Redis
* Python redis library

Redis and the Python redis library are requirements because the ansible.cfg is
configured for fact caching enabled.

You don't need Redis or the Python redis library if you turn off fact caching.
You can turn it off by editing ansible.cfg and commenting out the line:

    fact_caching = redis


## Running the playbook


You need a secrets.yml file that contains the passwords for several of the
services, but you can simply copy the example file secrets.yml.example.

To run it, do:

    cp secrets.yml.example secrets.yml
    vagrant up

Then point your browser to: http://192.168.33.10.xip.io or
https://www.192.168.33.10.xip.io. You'll get a security warning if you use the
https site since it's a self-signed certificate, this is normal.
