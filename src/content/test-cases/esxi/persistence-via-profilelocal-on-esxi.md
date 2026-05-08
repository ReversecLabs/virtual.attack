# Persistence via profile.local on ESXi

## Component
**ESXi**

## MITRE ATT&CK
- **ID:** T1546.004
- **Tactic:** Persistence

## Description
When a user logs into the ESXi host via an interactive shell, the user-modifiable script `/etc/profile.local` is sourced.

Adversaries can plant a binary in this file, which will provide execution with user-level. 

## Threat Actors
_None_

## Log Sources
- ESXi Shell Logs (/var/log/shell.log)

## References
- https://www.youtube.com/watch?v=2SFa09fYqW4

## Author
Leonidas Tsaousis (@laripping)
