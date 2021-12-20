import pytest
import os
import yaml
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.fixture()
def AnsibleDefaults(Ansible):
    with open("../../../defaults/main.yml", 'r') as stream:
        return yaml.load(stream)
  

def test_service(host):
    s = host.service("nfs-server")
    assert s.is_enabled
    assert s.is_running
