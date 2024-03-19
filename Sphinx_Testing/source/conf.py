# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'PIL_TEST_SPHINX'
copyright = '2024, Lawrence Ireland'
author = 'Lawrence Ireland'
release = '1.0.v.0'
html_logo = '/Users/erikherman/Documents/GitHub/PublicInformationLimited/Sphinx_Testing/source/Group 1.png'
html_logo_style = 'vertical-align: top; margin-right: 10px;'  # Aligns the logo at the top and adds margin to the right


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'reStructuredText markup'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'classic'
html_static_path = ['_static']
