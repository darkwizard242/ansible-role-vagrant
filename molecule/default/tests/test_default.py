import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

VAGRANT_BINARY_PATH = '/usr/local/bin/vagrant'


def test_vagrant_binary_exists(host):
    host.file('VAGRANT_BINARY_PATH').exists


def test_vagrant_binary_file(host):
    host.file('VAGRANT_BINARY_PATH').is_file


def test_vagrant_binary_run(host):
    host.check_output('whereis vagrant') == VAGRANT_BINARY_PATH
