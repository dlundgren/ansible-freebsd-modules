import os
import pytest
import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_creates_specified_file(host):
    file = host.file('/tmp/sysrc_file')

    assert file.exists


@pytest.mark.parametrize('file, key, value', [
    # name,value (present, append, substract)
    ("/etc/rc.conf", "sysrc_test_append", "test_a"),
    # dest,name,value
    ("/tmp/sysrc_file", "sysrc_test", "test"),
])
def test_items_in_files(host, file, key, value):
    data = host.run('grep %s= %s' % (key, file))

    assert data.stdout.rstrip() == '%s="%s"' % (key, value)


def test_file_in_jail(host):
    assert host.run('grep test_jail /etc/rc.conf').rc == 1

    jail = host.run('grep test_jail /usr/jails/testjail/etc/rc.conf')

    assert jail.stdout.rstrip() == '%s="%s"' % ("test_jail", "test")
