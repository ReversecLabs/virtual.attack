# Test Case Template

- **Pre-flight check!** Avoid repetition in the collection. If you think a relevant test case already exists in the collection, consider adding to its References instead. Variations are allowed.

- No frontmatter (`---` blocks) in the Markdown, and one test case per file.

- Filename should be the hyphenated lowercase slug of the title (e.g. `reboot-esxi-host.md`).

## Template Fields

The order of the fields is required and must be exact.

**`# Title`** — The test case name

**`## Component`** — The VCF component wrapped in bold (e.g. `**ESXi**`). Maps to the containing folder; folder name is the lowercase hyphenated component name. Create a new folder if adding a new component.

| Folder | Component |
|--------|-----------|
| `ad/` | Active Directory |
| `esxi/` | ESXi |
| `sddc-manager/` | SDDC Manager |
| `vcenter/` | vCenter |
| `vcf-automation/` | VCF Automation |
| `vcf-operations-for-logs/` | VCF Operations for Logs |
| `vidm/` | Workspace ONE Identity Manager (vIDM) |

**`## MITRE ATT&CK`** — `ID` and `Tactic`. A technique may have more than one candidate; pick the most defensible and most relevant

**`## Description`** — Provide brief, step-by-step reproducible instructions. Pro tip: Check LOLESXi (https://lolesxi-project.github.io/) and official Broadcom/VMware docs for existing procedure guidance.

**`## Threat Actors`** — Known threat actors sourced from threat intelligence reports. Use `_None_` if no known actors are documented.

**`## Log Sources`** — Primitive logs only, no SIEM or syslog collection. Format: `Log Name (/path/to/log)`. Research Broadcom/VMware product documentation to identify log sources, prefering latest versions of each component (unless specified in the description that test case targets older releases). Good third-party sources (e.g. williamlam.com, Threat Intelligence providers' detection guidance blog posts) can also come in handy. Keep log source naming consistent across the collection. Finally, use `_None_` if unknown.

**`## References`** — URLs supporting the description and threat actor attribution. Use `_None_` if no references exist.

**`## Author`** — Your name and handle (optional), e.g. `Leonidas Tsaousis (@laripping)`.


