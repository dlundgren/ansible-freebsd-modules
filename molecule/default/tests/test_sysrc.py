import os
import pytest
import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


@pytest.mark.parametrize('file, key, value', [
    # name,value (present, append, substract)
    ("/etc/rc.conf", "new_item", "test"),
    ("/etc/rc.conf", "firstboot_pkgs_list", "sudo virtualbox-ose-additions bash"),
    ("/etc/rc.conf", "firstboot_freebsd_update_enable", "NO"),
    # dest,name,value
    ("/tmp/test_sysrc.conf", "test_test", "test"),
    # dest,name,value,delim
    ("/tmp/test_sysrc.conf", "test_delim", "t2,t3")
])
def test_items_in_files(host, file, key, value):
    data = host.run('grep %s %s' % (key, file))

    assert data.stdout.rstrip() == '%s="%s"' % (key, value)


def test_removes_from_default_file(host):
    cmd = host.run('grep firstboot_pkgs_enable /etc/rc.conf')

    assert cmd.rc == 1


def test_creates_specified_file(host):
    file = host.file('/tmp/test_sysrc_new')

    assert file.exists


def test_file_in_jail(host):
    assert host.run('grep test_jail /etc/rc.conf').rc == 1

    jail = host.run('grep test_jail /usr/jails/testjail/etc/rc.conf')

    assert jail.stdout.rstrip() == '%s="%s"' % ("test_jail", "test")
