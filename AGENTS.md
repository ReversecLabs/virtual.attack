# AGENTS.md

## Project Overview

**Virtual//Attack** — a collection of attack technique test cases for threat emulation in VMware/VCF environments. 
This repository contains the test cases (content) saved as Markdown files, and a static documentation site for rendering them, powered by Astro and using custom pages and layouts. The site is hosted on GitHub Pages, and is built automatically using the workflow in `.github/workflows/deploy.yml`.

## Architecture

- `src/content/test-cases/<component>/*.md` is the content source of truth.
- `src/utils/parseTestCase.ts` parses Markdown into card and detail metadata.
- `src/content/config.ts` defines the Astro content collection; it does not validate Markdown metadata.
- `src/pages/index.astro` renders search and filtering; `src/pages/techniques/[...slug].astro` generates technique detail pages.
- `src/layouts/Layout.astro` and `src/styles/global.css` provide shared presentation.
- `astro.config.mjs` configures Astro. Build output is `dist/` and is not committed.

## Content ownership and format

- Test cases in `src/content/test-cases/**/*.md` are user-maintained. Do not create or edit them unless the user explicitly requests it.
- Never add YAML frontmatter to test case files.
- When explicitly changing test-case content, preserve the conventions in [`template.md`](template.md) and the exact parser contract in `src/utils/parseTestCase.ts`.
	- The parser requires headings including `## Component` and `## MITRE ATT&CK`.
	- MITRE metadata uses `**ID:**` and `**Tactic:**` labels.
	- List metadata uses Markdown bullets; filenames are lowercase kebab-case.

## Validation

- Install dependencies with `npm ci`; use `npm run dev` for local development.
- Run `npm run build` for site, parser, configuration, dependency, or workflow changes.
- There is currently no automated test, lint, or type-check script. When adding logic, ask whether coverage should be added.

## Scope and generated files

- Keep external dependencies minimal.
- Do not edit `README.md` unless explicitly requested. The badge generator and optional pre-commit hook may update its badge values as a generated side effect.
- Do not commit generated `dist/`, `.astro/`, or `node_modules/` directories.
- Review changes before creating a commit.
