#!/usr/bin/env python3
"""Generate shields.io badges with current technique and component counts."""

import glob
import os
import re
import urllib.parse


def count_test_cases():
    test_cases_path = "src/content/test-cases"
    test_count = 0

    for file_path in glob.glob(f"{test_cases_path}/**/*.md", recursive=True):
        with open(file_path, "r") as f:
            content = f.read()
            if content.strip():
                test_count += 1

    return test_count


def count_components():
    test_cases_path = "src/content/test-cases"
    components = set()

    for file_path in glob.glob(f"{test_cases_path}/**/*.md", recursive=True):
        component = file_path.split("/")[-2]
        components.add(component)

    return len(components)


def generate_badge(label, message, style="flat"):
    params = {"label": label, "message": str(message), "style": style}
    badge_url = "https://img.shields.io/badge/{}-{}-{}.svg".format(
        urllib.parse.quote_plus(params["label"]),
        urllib.parse.quote_plus(params["message"]),
        urllib.parse.quote_plus(params["style"]),
    )
    return badge_url


def main():
    test_count = count_test_cases()
    component_count = count_components()

    test_badge = generate_badge("Techniques", test_count)
    component_badge = generate_badge("Components", component_count)

    print(test_badge)
    print(component_badge)

    if os.getenv("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a") as fh:
            print(f"test_badge={test_badge}", file=fh)
            print(f"component_badge={component_badge}", file=fh)

    # Update README.md with new badges
    readme_path = "README.md"
    if os.path.exists(readme_path):
        update_readme(readme_path, test_badge, component_badge)


def update_readme(readme_path, test_badge, component_badge):
    """Update the README.md file with the new badge URLs."""
    with open(readme_path, "r") as f:
        content = f.read()

    # Pattern to match the existing badge URLs in the badges section
    test_pattern = r'https://img\.shields\.io/badge/Techniques-[0-9]+.*?\.svg\?style=flat-square'
    component_pattern = r'https://img\.shields\.io/badge/Components-[0-9]+.*?\.svg\?style=flat-square'

    content = re.sub(test_pattern, test_badge, content)
    content = re.sub(component_pattern, component_badge, content)

    with open(readme_path, "w") as f:
        f.write(content)

    print(f"Updated {readme_path} with new badges")


if __name__ == "__main__":
    main()
