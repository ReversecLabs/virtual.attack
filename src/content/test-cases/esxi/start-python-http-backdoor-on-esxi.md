# Execute Python Script on ESXi

## Component
**ESXi**

## MITRE ATT&CK
- **ID:** T1059.006
- **Tactic:** Execution

## Description
ESXi ships with Python, which attackers can use to bypass execution restrictions like `execInstalledOnly`. In documented incidents, Python backdoors have been launched from the commandline. 

To simulate: 

1. Connect to the ESXi host via SSH or ESXi Shell with root privileges
2. Drop or write a Python backdoor script on the host (e.g. `/store/packages/vmtools.py` to also use indicators from the incident documented by Juniper)
   - For PoC using documented indicators: a minimal HTTP localhost listener on port 8008 can be used: `import http.server, socketserver; socketserver.TCPServer(('localhost', 8008), http.server.SimpleHTTPRequestHandler).serve_forever()"`
3. The script was then started using nohup so it persisted after shell disconnection: `nohup /bin/python -u /store/packages/vmtools.py >/dev/null 2>&1 &`


## Threat Actors
- _None_

## Log Sources
- ESXi Shell Logs (/var/log/shell.log)
- VMkernel Logs (/var/log/vmkernel.log)
- HOSTD Logs (/var/log/hostd.log)

## References
- https://blogs.juniper.net/en-us/threat-research/a-custom-python-backdoor-for-vmware-esxi-servers

## Author
Leonidas Tsaousis (@laripping)
