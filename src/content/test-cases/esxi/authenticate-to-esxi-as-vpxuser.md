# Authenticate to ESXi as vpxuser

## Component
**ESXi**

## MITRE ATT&CK
- **ID:** T1078.003
- **Tactic:** Lateral Movement

## Description
Once vpxuser credentials have been extracted from vCenter, the attacker authenticates directly to managed ESXi hosts as vpxuser. This grants full root-equivalent rights to ESXi while bypassing vCenter RBAC and audit logging. Fire Ant operators used PowerCLI Connect-VIServer with vpxuser credentials to interact with hosts directly.

## Threat Actors
- UNC3886
- Fire Ant

## Log Sources
- HOSTD Logs (/var/log/hostd.log)
- Auth Logs (/var/log/auth.log)

## References
- https://www.sygnia.co/blog/fire-ant-a-deep-dive-into-hypervisor-level-espionage/

## Author
Leonidas Tsaousis (@laripping)
