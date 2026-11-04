# Change ESXi MOTD via SSH for Defacement

## Component
**ESXi**

## MITRE ATT&CK
- **ID:** T1491.001
- **Tactic:** Impact

## Description
Adversaries replace the Message of the Day (MOTD) file at `/etc/motd` to display a defacement notice or ransom note to anyone logging in via SSH. This technique was observed in the Kyber ransomware attack pattern where the malware replaces `/etc/motd` so administrators see the ransom note immediately upon SSH login. Test (from an ESXi shell session with root privileges): `echo "<ransom_note_content>" > /etc/motd`. Verify by SSHing to the ESXi host or reading the file: `cat /etc/motd`.

## Threat Actors
- Kyber
- INC

## Log Sources
- HostD Logs (/var/log/hostd.log)
- ESXi Shell Logs (/var/log/shell.log)
- Secure Logs (/var/log/secure)

## References
- https://www.rapid7.com/blog/post/tr-kyber-ransomware-double-trouble-windows-esxi-attacks-explained/
- https://www.acronis.com/en/tru/posts/from-emerging-threat-to-top-tier-ransomware-as-a-service-the-evolution-of-inc-ransomware/

## Author
Leonidas Tsaousis (@laripping)
