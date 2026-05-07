# Tunnel Internal Traffic via SOCKS Proxy

## Component
**vCenter**

## MITRE ATT&CK
- **ID:** T1090.001
- **Tactic:** Command and Control

## Description
Malware such as BRICKSTORM installed on a VCSA or other appliance, could establish a SOCKS proxy to tunnel attacker traffic into internal network segments, pivoting from the management plane into application tiers without traversing perimeter controls. Test: use a SOCKS-capable proxy on a benign port and confirm internal reachability through the appliance.

## Threat Actors
- UNC5221
- WARP PANDA

## Log Sources
- Auth Logs (/var/log/auth.log)
- systemd Journal (journalctl)

## References
- https://cloud.google.com/blog/topics/threat-intelligence/brickstorm-espionage-campaign

## Author
Leonidas Tsaousis (@laripping)
