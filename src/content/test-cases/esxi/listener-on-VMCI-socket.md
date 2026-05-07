# Listener on VMCI Socket

## Component
**ESXi**

## MITRE ATT&CK
- **ID:** T1095
- **Tactic:** Command and Control

## Description
VMCI (Virtual Machine Communication Interface) is a host-to-guest IPC channel that bypasses normal network paths. With root on ESXi, an attacker can bind to a VMCI socket and initiate communications from clients within guest VMs, thereby enabling C2 traffic that does not traverse network firewalls or IDS/IPS. To test this, a listener can be bound on the fixed 18098 (VIRUALPITA) VMCI port of the ESXi host.

## Threat Actors
- UNC3886
- Fire Ant

## Log Sources
- HOSTD Logs (/var/log/hostd.log)
- Per-VM Logs (/vmfs/volumes/<datastore>/<vm>/vmware.log)

## References
- https://www.sygnia.co/blog/fire-ant-a-deep-dive-into-hypervisor-level-espionage/
- https://cloud.google.com/blog/topics/threat-intelligence/vmware-detection-containment-hardening
- https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence
- https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-detection-hardening

## Author
Leonidas Tsaousis (@laripping)
