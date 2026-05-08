---
name: add-test-case
description: Adds a new simulation test case to the collection, following the standard format. Researches threat intelligence and documentation to populate all required fields. Use when the user wants to add or create a new test case, technique or scenario.
allowed-tools: WebSearch
---


The collection of test cases lives in `src/content/test-cases` organised per component. Output should be a new .md file, fully populated and named appropriately, in the appropriate component directory.  


## Instructions

### General
- one test case per MD file
- see `template.md` (repo root) for the Markdown format, per-field guidance, and a worked example.
- Regarding filenames, the example in `template.md` (`Reboot ESXi Host`) would be named `reboot-esxi-host.md`.
- Avoid repetition in the collection. If you think a relevant test case already exists in the collection, prompt the user if they want to instead just add additional references found to the existing test case, or continue with adding a variation
- If eventually the test case is added, check if we need to update README on the rough number of test cases (e.g. 70+ -> 80+)  


### Descriptions 
- keep descriptions brief and concise
- test cases should be reproducible. Provide step by step instructions in the description. Instructions might exist in the LOLESXi project or official docs 

### References and MITRE metadata
- research for threat intelligence to populate References, Threat Actors sections
- MITRE ATT&CK TTP ID & Tactic might have more than one candidate, pick the most defensible, most relevant one, without asking for confirmation

### Logs
- for the Log Sources section, research Broadcom/VMware product documentation, ideally latest unless we're explicitly refering to an older version, as well as 3rd party blogs (like williamlam.com), or threat detection guidance from e.g. Mandiant
- Logs must follow the format "Log name (/path/to/log)" as in the example, keep naming consistent across the collection
- Primitive logs only, assume no SIEM or syslog collection

### Author
- prompt the user for the Author field, presenting them an example



