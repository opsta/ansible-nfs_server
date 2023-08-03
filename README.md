# Ansible Role: NFS Server Repository
This Ansible Role will setup NFS Service
- Install NFS Package; check in `vars` folder
  - Debian `nfs-common`, `nfs-kernel-server`
  - RedHat `nfs-utils`
- Create `exports` file for NFS Share

## Requirements

- Be sure to know basic of installing NFS on Linux and how NFS works

## Role Variables

- **REQUIRED** - `nfs_exportfs_configs` 
```
nfs_exportfs_configs:
  - client_ip: 10.33.48.0/16
    path: /nfs
    mount_options: "(rw)"
  - client_ip: 10.33.48.0/16
    path: /nfs2
    mount_options: "(rw,sync,no_subtree_check)"
```
This will be transformed into `exports` config file
- Templeting from `templates/exports.j2`
```
/nfs    10.33.48.0/16(rw)
/nfs2   10.33.48.0/16(rw,sync,no_root_squash,no_subtree_check)
...
```

- Use Static Port for RPC
```
nfs_server_rpcmount_port: 33333
```

## Dependencies

None.

## Example Playbook

    - hosts: all
      roles:
        - opsta.nfs_server

## Ansible Molecules

To be documented.

## License

MIT

## Author Information

Opsta (Thailand) Co.,Ltd.
