# Change ESXi Root Password via CLI

## Component
**ESXi**

## MITRE ATT&CK
- **ID:** T1098
- **Tactic:** Persistence

## Description
With direct shell access to an ESXi host, an attacker can change the root password to lock out legitimate administrators and maintain exclusive access. Agenda ransomware was documented doing this programmatically across all ESXi hosts in an environment before deploying its payload.

1. Connect to the ESXi host via SSH or ESXi Shell with root privileges
2. Change the root password interactively: `passwd`
3. Alternatively, change it non-interactively: `esxcli system account set -i root -p <new_password> -c <new_password>`

## Threat Actors
- Agenda
- UNC3944
- Scattered Spider

## Log Sources
- ESXi Shell Logs (/var/log/shell.log)
- Auth Logs (/var/log/auth.log)
- HOSTD Logs (/var/log/hostd.log)

## References
- https://www.trendmicro.com/en_us/research/24/c/agenda-ransomware-propagates-to-vcenters-and-esxi-via-custom-pow.html
- https://cloud.google.com/blog/topics/threat-intelligence/defending-vsphere-from-unc3944

## Author
Leonidas Tsaousis (@laripping)
