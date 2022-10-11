[![build-test](https://github.com/darkwizard242/ansible-role-vagrant/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-vagrant/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-vagrant/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-vagrant/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/43055?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/43055?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/43055?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-vagrant&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-vagrant) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-vagrant&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-vagrant) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-vagrant&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-vagrant) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-vagrant&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-vagrant) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-vagrant?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-vagrant?color=orange&style=flat-square)

# Ansible Role: Vagrant

Role to install (_by default_) [vagrant](https://www.vagrantup.com/) package on **Debian/Ubuntu** and **EL** systems.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
vagrant_app: vagrant
vagrant_version: 2.3.1
vagrant_os: linux
vagrant_arch: amd64
vagrant_dl_url: https://releases.hashicorp.com
vagrant_dl_loc: /tmp
vagrant_bin_path: /usr/local/bin
vagrant_file_owner: root
vagrant_file_group: root
vagrant_file_mode: '0755'
```

### Variables table:

Variable           | Description
------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------
vagrant_app        | Defines the app to install i.e. **vagrant**
vagrant_version    | Defined to dynamically fetch the desired version to install. Defaults to: **2.3.1**
vagrant_os         | Defines os type. Used for obtaining the correct type of binaries based on OS type. Defaults to: **linux**
vagrant_arch       | Defines os architecture. Used to set the correct type of binaries based on OS System Architecture. Defaults to: **amd64**
vagrant_dl_url     | Defines URL to download the vagrant binary from.
vagrant_dl_loc     | Defined to dynamically set where to place the binary archive for `vagrant` temporarily. Defaults to: **/tmp**
vagrant_bin_path   | Defined to dynamically set the appropriate path to store vagrant binary into. Defaults to (as generally available on any user's PATH): **/usr/local/bin**
vagrant_file_owner | Owner for the binary file of vagrant.
vagrant_file_group | Group for the binary file of vagrant.
vagrant_file_mode  | Mode for the binary file of vagrant.

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
    vagrant_version: 2.2.10
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

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/).
