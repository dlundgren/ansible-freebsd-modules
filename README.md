# ansible-freebsd-modules

Ansible Modules for FreeBSD

## Testing

Testing requires Molecule, Vagrant & Virtualbox. 

## Module :: kld

Loads the given kernel module, or puts it in the /boot/loader.conf

### Parameters

| Parameter | Choices/Defaults | Comments |
| :-------- | :--------------- | :----- |
| name      | | Name of the kernel module. .ko is typically not needed |
| load      | Default: True | Load or unload the module |
| boot      | Default: True | Apply the kernel module at boot. |

### Examples

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

## sysrc

Uses [sysrc(8)](https://www.freebsd.org/cgi/man.cgi?query=sysrc) to set a sys var in /etc/rc.conf (default) or the given
`$dest` file

### Parameters

| Parameter | Choices/Defaults | Comments |
| :-------- | :--------------- | :----- |
| dest      | | The file to modify |
| delim     | ` ` | Delimiter. Used with append/subtract |
| name      | | Name of the variable to manage |
| value     | | Required when not `state=absent` |
| state     | **Choices**: <ul><li>append<li>absent</li><li>**present**</li><li>subtract</li></ul> | Whether the var should be appended, substracted, exist, or not exist. |

### Examples

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

# add gif0 to cloned_interfaces
- name: add gif0 interface
  sysrc:
    name: cloned_interfaces
    state: append
    value: "gif0"
```
