
Ansible Role: Vagrant
=========

Role to install (_by default_) `vagrant` package  on **Ubuntu** systems.

Requirements
------------

None.

Role Variables
--------------

Available variables are listed below (located in  `defaults/main.yml`):

```yaml
vagrant_app: vagrant
vagrant_version: 2.2.5
vagrant_osarch: linux_amd64
vagrant_dl_url: https://releases.hashicorp.com
vagrant_dl_loc: /tmp
vagrant_bin_path: /usr/local/bin
```

Variable `vagrant_app`: Defines the app to install i.e. **vagrant**

Variable `vagrant_version`: Defined to dynamically fetch the desired version to install. Defaults to: **0.12.4**

Variable `vagrant_osarch`: Defines os architecture. Used for obtaining the correct type of binaries based on OS System Architecture. Defaults to: **linux_amd64**

Variable `vagrant_dl_loc`: Defined to dynamically choose where to place the binary archive for `vagrant` temporarily. Defaults to: **/tmp**

Variable `vagrant_dl_url`: Defines URL to download the vagrant binary from.

Variable `vagrant_bin_path`: Defined to dynamically choose the appropriate path to store vagrant binary into. Defaults to (as generally on any user's PATH): **/usr/local/bin** 

Dependencies
------------

None

Example Playbook
----------------

For default behaviour of role (i.e. installation of **vagrant**) in ansible playbooks.
```yaml
- hosts: servers
  roles:
    - role: darkwizard242.vagrant
```

For customizing behavior of role (i.e. specifying the  desired **vagrant** version) in ansible playbooks.
```yaml
- hosts: servers
  roles:
    - role: darkwizard242.vagrant
      vars:
        vagrant_version: 2.2.4
```

For customizing behavior of role (i.e. placing binary of **vagrant** package in different location) in ansible playbooks.
```yaml
- hosts: servers
  roles:
    - role: darkwizard242.vagrant
      vars:
        vagrant_bin_path: /bin/
```

License
-------

[MIT](https://github.com/darkwizard242/ansible-role-vagrant/blob/master/LICENSE)

Author Information
------------------

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).
