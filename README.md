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

The `sysrc` module has been moved to [community.general.sysrc](https://docs.ansible.com/ansible/latest/collections/community/general/sysrc_module.html). 
