# Disable Lockdown Mode via vCenter UI

## Component
**ESXi**

## MITRE ATT&CK
- **ID:** T1562
- **Tactic:** Defense Evasion

## Description
ESXi Lockdown Mode is a host-level security control that restricts who can manage the host directly, forcing administration through vCenter. In Normal mode, the DCUI remains available and Exception Users can still log in over SSH/Host Client; in Strict mode, even the DCUI is disabled and only the vpxuser and Exception Users can connect at all. Adversaries with sufficient privilege turn this control off as a precursor to direct ESXi access (SSH/DCUI/Host Client login as root, custom VIB install, etc.) Disable paths: (a) From vCenter UI: select host -> Configure -> System -> Security Profile -> Edit Lockdown Mode -> Disabled.

## Threat Actors
_None_

## Log Sources
- VPXD Logs (/var/log/vmware/vpxd/vpxd.log)

## References
- https://knowledge.broadcom.com/external/article/336894/enabling-or-disabling-lockdown-mode-on-a.html

## Author
Leonidas Tsaousis (@laripping)
