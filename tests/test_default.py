import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


@pytest.mark.parametrize('name', ['Django', 'gunicorn'])
def test_pip_packages(PipPackage, name):
    assert name in PipPackage.get_packages()


# These tests assume
# - centos/7 Vagrantbox has selinux
# - centos:7 docker image doesn't have selinux
def test_selinux(Command, Sudo, TestinfraBackend):
    host = TestinfraBackend.get_hostname()
    if host == 'omero-web-runtime-docker':
        assert not Command.exists('semanage')
    else:
        with Sudo():
            out = Command.check_output('semanage port -l -C')
            assert out.split()[-3:] == ['http_port_t', 'tcp', '4080']
