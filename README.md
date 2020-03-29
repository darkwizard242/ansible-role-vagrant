[![Build Status](https://travis-ci.com/darkwizard242/ansible-role-vagrant.svg?branch=master)](https://travis-ci.com/darkwizard242/ansible-role-vagrant) ![Ansible Role](https://img.shields.io/ansible/role/43055?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/43055?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/43055?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-vagrant&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-vagrant) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-vagrant?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-vagrant?color=orange&style=flat-square)

# Ansible Role: Vagrant

Role to install (_by default_) [vagrant](https://www.vagrantup.com/) package on **Debian/Ubuntu** and **EL** systems.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
vagrant_app: vagrant
vagrant_version: 2.2.7
vagrant_osarch: linux_amd64
vagrant_dl_url: https://releases.hashicorp.com
vagrant_dl_loc: /tmp
vagrant_bin_path: /usr/local/bin
```

### Variables table:

Variable         | Value (default)                  | Description
---------------- | -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------
vagrant_app      | vagrant                          | Defines the app to install i.e. **vagrant**
vagrant_version  | 2.2.7                            | Defined to dynamically fetch the desired version to install. Defaults to: **2.2.7**
vagrant_osarch   | linux_amd64                      | Defines os architecture. Used for obtaining the correct type of binaries based on OS System Architecture. Defaults to: **linux_amd64**
vagrant_dl_url   | <https://releases.hashicorp.com> | Defines URL to download the vagrant binary from.
vagrant_dl_loc   | /tmp                             | Defined to dynamically set where to place the binary archive for `vagrant` temporarily. Defaults to: **/tmp**
vagrant_bin_path | /usr/local/bin                   | Defined to dynamically set the appropriate path to store vagrant binary into. Defaults to (as generally available on any user's PATH): **/usr/local/bin**

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **vagrant**) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.vagrant
```

For customizing behavior of role (i.e. specifying the desired **vagrant** version) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.vagrant
  vars:
    vagrant_version: 2.2.7
```

For customizing behavior of role (i.e. placing binary of **vagrant** package in different location) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.vagrant
  vars:
    vagrant_bin_path: /bin/
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-vagrant/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).
