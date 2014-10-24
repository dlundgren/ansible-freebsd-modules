ansible-freebsd-modules
=======================

Ansible Modules for FreeBSD

## kld

Loads the given kernel module, or puts it in the /boot/loader.conf

Accepts the following options

- **name** The name of the kernel module. .ko is typically not needed
- **load** Load or unload the module. Default: True
- **boot** Apply the kernel module at boot. Default: True

#### example
```yaml
---
# Adds accf_http to the bootloader and loads it
- kld:
    name: accf_http
# Removes accf_http from the bootloader and loads it
- kld:
    name: accf_http
    load: true
    boot: false
```

#### sysrc

Uses [sysrc(8)](https://www.freebsd.org/cgi/man.cgi?query=sysrc) to set a sys var in /etc/rc.conf (default) or the given
$dest file

Accepts the following options

- **name** The name of the variable
- **value** The value of the variable
- **state** Whether the var should be present or absent
- **dest**  What file to add this value to

#### example
```yaml
---
# enable mysql in the /etc/rc.conf
- name: Configure mysql pid file
  sysrc:
    name: mysql_pidfile
    value: "/var/run/mysqld/mysqld.pid"

# enable accf_http kld in the boot loader
- name: enable accf_http kld
  sysrc:
    name: accf_http_load
    state: present
    value: "YES"
    dest: /boot/loader.conf
```