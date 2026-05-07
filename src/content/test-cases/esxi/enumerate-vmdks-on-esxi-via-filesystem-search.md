# Enumerate VMDKs on ESXi via Filesystem Search

## Component
**ESXi**

## MITRE ATT&CK
- **ID:** T1083
- **Tactic:** Discovery

## Description
Adversaries enumerate virtual machine disk files (.vmdk) across mounted datastores to identify high-value VMs (Domain Controllers, file servers, databases) for cloning, detachment, or encryption. Test (from a privileged ESXi shell session): `find /vmfs/volumes -name "*.vmdk" -type f 2>/dev/null` or `ls -la /vmfs/volumes/*/`. Documented in Crowdstrike Hypervisor Jackpotting Part 2 as standard reconnaissance for eCrime ESXi-targeting ransomware operators.

## Threat Actors
- Viking Spider

## Log Sources
- ESXi Shell Logs (/var/log/shell.log)

## References
- https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1083/T1083.md
- https://www.crowdstrike.com/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/

## Author
Atomic Red Team
