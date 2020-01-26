import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_vagrant_binary_exists(host):
    assert host.file('/usr/local/bin/vagrant').exists


def test_vagrant_binary_file(host):
    assert host.file('/usr/local/bin/vagrant').is_file


def test_vagrant_binary_which(host):
    assert host.check_output('which vagrant') == '/usr/local/bin/vagrant'
