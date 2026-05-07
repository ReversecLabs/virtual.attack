# Network Configuration Discovery on ESXi

## Component
**ESXi**

## MITRE ATT&CK
- **ID:** T1016
- **Tactic:** Discovery

## Description
Adversaries enumerate ESXi networking - vmkernel ports, management network, VLANs, NIC MAC addresses - to map their position in the cluster and identify pivot paths. Test (from a privileged shell session): `esxcli network nic list; esxcli network ip interface ipv4 get; esxcli network ip route ipv4 list; esxcli network firewall ruleset list`. Documented in Trellix RansomHouse 2024 reporting.

## Threat Actors
- RansomHouse

## Log Sources
- ESXi Shell Logs (/var/log/shell.log)

## References
- https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1016/T1016.md

## Author
Atomic Red Team
