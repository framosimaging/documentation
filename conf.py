# -- Path setup --------------------------------------------------------------
import os
import sys
from pathlib import Path
from typing import Any, Dict

import pydata_sphinx_theme
from sphinx.application import Sphinx

sys.path.append(str(Path(".").resolve()))
sys.setrecursionlimit(1500)  # Increase the recursion limit

# -- Project information -----------------------------------------------------

project = "Framos Docs"
copyright = "2024, Framos Inc"
author = "Framos"

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinxext.rediraffe",
    "sphinx_design",
    "sphinx_copybutton",
    # "autoapi.extension",  # Comment this line out
    # custom extensions
    "_extension.gallery_directive",
    # "_extension.component_directive",
    # For extension examples and demos
    "myst_parser",
    "ablog",
    "jupyter_sphinx",
    "sphinxcontrib.youtube",
    "nbsphinx",
    "numpydoc",
    "sphinx_togglebutton",
    # "jupyterlite_sphinx",
    "sphinx_favicon",
]

jupyterlite_config = "jupyterlite_config.json"

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]

# -- Sitemap -----------------------------------------------------------------

# ReadTheDocs has its own way of generating sitemaps, etc.
if not os.environ.get("READTHEDOCS"):
    extensions += ["sphinx_sitemap"]

    html_baseurl = os.environ.get("SITEMAP_URL_BASE", "http://127.0.0.1:8000/")
    sitemap_locales = [None]
    sitemap_url_scheme = "{link}"

# -- MyST options ------------------------------------------------------------

# This allows us to use ::: to denote directives, useful for admonitions
myst_enable_extensions = ["colon_fence", "linkify", "substitution"]
myst_heading_anchors = 2
myst_substitutions = {"rtd": "[Read the Docs](https://readthedocs.org/)"}

# -- Internationalization ----------------------------------------------------

# specifying the natural language populates some key tags
language = "en"

# -- Ablog options -----------------------------------------------------------

# -- Options for HTML output -------------------------------------------------

html_theme = "pydata_sphinx_theme"
html_logo = "_static/FRlogo.svg"
html_favicon = "_static/FRlogo.svg"
html_sourcelink_suffix = ""
html_last_updated_fmt = ""  # to reveal the build date in the pages meta

html_theme_options = {
    "show_nav_level": 1,
    "header_links_before_dropdown": 4,
    "icon_links": [
        {
            "name": "Twitter",
            "url": "https://twitter.com/framosimaging",
            "icon": "fa-brands fa-twitter",
        },
        {
            "name": "GitHub",
            "url": "https://github.com/framosgmbh",
            "icon": "fa-brands fa-github",
        },
    ],
    "logo": {
        "text": "FRAMOS",
        "image_dark": "_static/FRlogo.svg",
    },
    "use_edit_page_button": True,
    "show_toc_level": 2,
    "navbar_align": "left",
    "navbar_center": ["navbar-nav"],
    "footer_start": ["copyright"],
    "footer_end": [],
    # "footer_center": ["sphinx-version"],
    "secondary_sidebar_items": {
        "**/*": ["page-toc-mod", "sourcelink"],
        "examples/no-sidebar": [],
    },
    "navigation_with_keys": False,
    "data_mode": "dark",
    "default_mode": "dark",
}

# html_sidebars = {
#     "index": [
#         "sidebar-nav-bs"
#     ]
# }

# html_sidebars = {
#     "**": ["search-field.html", "sidebar-nav-bs.html"],
#     "index": ["search-field.html", "sidebar-nav-bs.html"],
# }


html_context = {
    "default_mode": "dark",
    "github_user": "pydata",
    "github_repo": "pydata-sphinx-theme",
    "github_version": "main",
    "doc_path": "docs",
}

# rediraffe_redirects = {
#     "contributing.rst": "community/index.rst",
# }

html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_js_files = ["custom-icon.js"]
todo_include_todos = True

# -- favicon options ---------------------------------------------------------

favicons = [
    "FRlogo.svg",
    {"rel": "shortcut icon", "sizes": "any", "href": "FRloho.svg"},
    "android-chrome-192x192.png",
    {"rel": "mask-icon", "color": "#459db9", "href": "safari-pinned-tab.svg"},
    {"rel": "apple-touch-icon", "href": "apple-touch-icon.png"},
    {"name": "msapplication-TileColor", "content": "#459db9"},
    {"name": "theme-color", "content": "#ffffff"},
]

# -- Options for autosummary/autodoc output ------------------------------------
autosummary_generate = True
autodoc_typehints = "description"
autodoc_member_order = "groupwise"

def setup_to_main(
    app: Sphinx, pagename: str, templatename: str, context, doctree
) -> None:
    def to_main(link: str) -> str:
        links = link.split("/")
        idx = links.index("edit")
        return "/".join(links[: idx + 1]) + "/main/" + "/".join(links[idx + 2 :])

    context["to_main"] = to_main

def setup(app: Sphinx) -> Dict[str, Any]:
    app.connect("html-page-context", setup_to_main)
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }