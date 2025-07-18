import os
import sys
sys.path.insert(0, os.path.abspath(".."))  # so Sphinx can find your package

project = "GLSI Tools"
author = "GLSI"
release = "0.0.0"

# General configuration
extensions = [
    "myst_parser",            # Enables Markdown
    "sphinx.ext.autodoc",     # Optional: auto-generate API docs
    "sphinx.ext.napoleon",    # Optional: parse Google/Numpy-style docstrings
]

templates_path = ["_templates"]
exclude_patterns = []

# Recognize both .md and .rst files
source_suffix = [".rst", ".md"]

# Use 'index.md' as the root document
master_doc = "index"

myst_enable_extensions = [
    "colon_fence",  # allows ::: and ```{ } blocks
]

# HTML output options
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_logo = "_static/GLSI_logo.png"

html_theme_options = {
    "logo_only": False,
    "display_version": True,
}
