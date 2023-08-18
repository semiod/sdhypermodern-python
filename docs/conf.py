"""Sphinx configuration."""
from datetime import datetime


project = "sdHypermodern Python"
author = "Semio Ds"
copyright = f"{datetime.now().year}, {author}"
extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon", "sphinx_autodoc_typehints"]
html_static_path = ["_static"]