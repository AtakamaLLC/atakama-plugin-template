# Atakama Plugin: Template

## Overview

Template repository.

Adjust as follows:
 1. Rename `plugin_template` folder - this should be a descriptive name for the main module.
 2. Edit `pyproject.toml` - set project `name` attribute to module name from step 1
 3. Edit `Makefile`:
    1. Replace `plugin_template` everywhere it appears with module name from step 1
    2. Adjust paths in `apkg` section (key, crt, pkg) as needed
 4. Edit `README.md` as needed
