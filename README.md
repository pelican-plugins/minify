pelican-minification: A Plugin for Pelican
====================================================

[![Build Status](https://img.shields.io/github/workflow/status/pelican-plugins/pelican-minification/build)](https://github.com/pelican-plugins/pelican-minification/actions)
[![PyPI Version](https://img.shields.io/pypi/v/pelican-minification)](https://pypi.org/project/pelican-minification/)
![License](https://img.shields.io/pypi/l/pelican-minification?color=blue)

This Pelican plugin can compress HTML & CSS files as well as inline CSS and JavaScript in HTML files.

Installation
------------

This plugin can be installed via:

    python -m pip install pelican-minification

Usage
-----

By default, all HTML and CSS files will be conpressed, including inline JavaScript and CSS rules in `<script>` and `<style>` tags.

To configure the behavior of the plugin, add the following variables in your pelicanconf.py* (here are the default values):

```
CSS_MIN = True
HTML_MIN = True
INLINE_CSS_MIN = True
INLINE_JS_MIN = True
```

Please note that ``INLINE_CSS_MIN`` and ``INLINE_JS_MIN`` require ``HTML_MIN`` be enabled.

Contributing
------------

Contributions are welcome and much appreciated. Every little bit helps. You can contribute by improving the documentation, adding missing features, and fixing bugs. You can also help out by reviewing and commenting on [existing issues][].

To start contributing to this plugin, review the [Contributing to Pelican][] documentation, beginning with the **Contributing Code** section.

[existing issues]: https://github.com/pelican-plugins/pelican-minification/issues
[Contributing to Pelican]: https://docs.getpelican.com/en/latest/contribute.html

License
-------

This project is licensed under the MIT license.
