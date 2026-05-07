# Extract Credentials from VM Memory Snapshot

## Component
**ESXi**

## MITRE ATT&CK
- **ID:** T1003.001
- **Tactic:** Credential Access

## Description
After capturing a memory-inclusive snapshot of a high-value VM (e.g. a Domain Controller; see "Snapshot VM on ESXi"), the attacker exfiltrates the .vmem file and analyses it offline with Volatility (or Sygnia-observed UpdateApp) to extract LSASS, lsa, NTDS, or kerberos credential material from in-memory structures, bypassing on-host EDR.

## Threat Actors
- UNC3886
- Fire Ant

## Log Sources
- HOSTD Logs (/var/log/hostd.log)
- Per-VM Logs (/vmfs/volumes/<datastore>/<vm>/vmware.log)

## References
- https://www.sygnia.co/blog/fire-ant-a-deep-dive-into-hypervisor-level-espionage/

## Author
Leonidas Tsaousis (@laripping)
