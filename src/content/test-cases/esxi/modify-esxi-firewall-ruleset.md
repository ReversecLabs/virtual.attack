# Modify ESXi Firewall Ruleset

## Component
**ESXi**

## MITRE ATT&CK
- **ID:** T1562.004
- **Tactic:** Defense Evasion

## Description
With root on an ESXi host, the attacker disables the ESXi firewall or relaxes rules to permit attacker-controlled tooling traffic (e.g., open SSH from any source IP, open custom C2 ports). Achieved via `esxcli network firewall set --enabled false` or `esxcli network firewall ruleset set --allowed-all true`. UNC3886 / Fire Ant operators add custom ESXi firewall rules from VIB-deployed startup scripts to permit inbound traffic on backdoor listener ports (e.g. TCP/2233, TCP/7475, VMCI/18098).

## Threat Actors
- UNC3886
- Fire Ant

## Log Sources
- HOSTD Logs (/var/log/hostd.log)
- ESXi Shell Logs (/var/log/shell.log)
- Auth Logs (/var/log/auth.log)

## References
- https://www.sygnia.co/blog/fire-ant-a-deep-dive-into-hypervisor-level-espionage/
- https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence

## Author
Leonidas Tsaousis (@laripping)
