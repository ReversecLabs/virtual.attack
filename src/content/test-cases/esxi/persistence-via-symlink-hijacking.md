# Persistence via Symlink Hijacking on ESXi

## Component
**ESXi**

## MITRE ATT&CK
- **ID:** T547.009
- **Tactic:** Persistence

## Description
Similar to the common Linux technique, well-known and commonly used symlinks can be modified with appropriate permissions to point to attacker-controlled binaries. An example in ESXi would be the `esxcli` which normally points to `/bin/esxcli.py`. The link can be modified using command `ln -s` to e.g. pass the original arguments to the legitimate binary, after executing a malicious command.  

## Threat Actors
_None_

## Log Sources
- HOSTD Logs (/var/run/log/hostd.log)

## References
- https://www.youtube.com/watch?v=2SFa09fYqW4

## Author
Leonidas Tsaousis (@laripping)
