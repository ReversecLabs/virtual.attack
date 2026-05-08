# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Virtual//Attack** — a collection of 70+ attack technique test cases for threat emulation in VMware/VCF environments. Built as a static documentation site with Astro + Starlight. Content lives in Markdown files; the framework just renders them.

## Development Commands

```bash
npm install && npm run dev   # Install deps, start dev server on localhost:4321
npm run build                # Generate static site to dist/
```

## Tests and Code Review 

- Ask to add some tests next time code is added

- Perform a code review before every commit

## Architecture

- **Content source of truth**: `src/content/test-cases/<component>/*.md` — plain Markdown, no YAML frontmatter
- **Framework**: Astro 4; configuration in `astro.config.mjs`
- **Schema**: `src/content/config.ts` defines the Astro content collection schema with Zod validation
- **Pages**: `src/pages/index.astro` (home) and `src/pages/page.astro` (layout template)
- **Build output**: `dist/` (static HTML, not committed)

## Test Case File Format

See [`template.md`](template.md) for the blank template, per-field guidance, component folder mapping, and a worked example.

## Key Constraints

- **No frontmatter** — never add `---` YAML headers to test case files
- **Do not edit test-cases** — test case `.md` files in `src/content/test-cases/` are the source; only the user modifies these
- **Do not modify `README.md`** unless explicitly asked
- **Keep external dependencies to a minimum** - in scripts, front-end and back-end code 
