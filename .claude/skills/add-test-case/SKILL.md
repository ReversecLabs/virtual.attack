---
name: add-test-case
description: Adds a new simulation test case to the collection, following the standard format. Researches threat intelligence and documentation to populate all required fields. Use when the user wants to add or create a new test case, technique or scenario.
allowed-tools: WebSearch
---


The collection of test cases lives in `src/content/test-cases` organised per component. Output should be a new .md file, fully populated and named appropriately, in the appropriate component directory.  


## Instructions


- keep descriptions brief and concise
- test cases should be reproducible. Provide step by step instructions in the description. Instructions might exist in the LOLESXi project or official docs 
- one test case per MD file
- see `assets/template.md` for the Markdown test case format, and `assets/example.md` for an example. 
- Regarding filenames, the example at `assets/example.md`  should be named `create-new-vm-on-esxi.md`.
- research for threat intelligence to populate References, Threat Actors sections
- MITRE ATT&CK TTP ID & Tactic might have more than one candidate, pick the most defensible, most relevant one, without asking for confirmation
- for the Log Sources section, research Broadcom/VMware product documentation, ideally latest unless we're explicitly refering to an older version, as well as 3rd party blogs (like williamlam.com), or threat detection guidance from e.g. Mandiant
- prompt the user for the Author field, presenting them an example
- Avoid repetition in the collection. If you think a relevant test case already exists in the collection, prompt the user if they want to instead just add additional references found to the existing test case, or continue with adding a variation
- If eventually the test case is added, check if we need to update README on the rough number of test cases (e.g. 70+ -> 80+)  

