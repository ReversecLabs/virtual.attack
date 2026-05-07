# Establish VMCI Socket Backdoor on ESXi-Guest Channel

## Component
**ESXi**

## MITRE ATT&CK
- **ID:** T1095
- **Tactic:** Command and Control

## Description
VMCI (Virtual Machine Communication Interface) is a host-to-guest IPC channel that bypasses normal network paths. With root on ESXi, the attacker establishes a listening VMCI socket on the host and a client inside a guest VM, enabling C2 traffic that does not traverse network firewalls or IDS/IPS. Mandiant's detection guidance lists VMCI backdoors among priority hardening targets on compromised hosts.

## Threat Actors
- UNC3886
- Fire Ant

## Log Sources
- HOSTD Logs (/var/log/hostd.log)
- Per-VM Logs (/vmfs/volumes/<datastore>/<vm>/vmware.log)
- sysclog (/var/log/sysclog)

## References
- https://www.sygnia.co/blog/fire-ant-a-deep-dive-into-hypervisor-level-espionage/
- https://cloud.google.com/blog/topics/threat-intelligence/vmware-detection-containment-hardening
- https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence
- https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-detection-hardening

## Author
Leonidas Tsaousis (@laripping)
