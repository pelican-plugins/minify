Minify: A Plugin for Pelican
============================

[![Build Status](https://img.shields.io/github/actions/workflow/status/pelican-plugins/minify/main.yml?branch=main)](https://github.com/pelican-plugins/minify/actions)
[![PyPI Version](https://img.shields.io/pypi/v/pelican-minify)](https://pypi.org/project/pelican-minify/)
![License](https://img.shields.io/pypi/l/pelican-minify?color=blue)

This Pelican plugin can compress HTML & CSS files as well as inline CSS and JavaScript in HTML files.

Requirements
------------

Because this plugin depends on the [`minify-html`](https://pypi.org/project/minify-html) Python package, which in turn utilizes the Rust-based [`minify-html`](https://github.com/wilsonzlin/minify-html) project, you must have Cargo (the Rust package manager) installed and available on your `PATH`. Rust and Cargo can be installed on Mac systems via Homebrew:

    brew install rust

Alternatively, Rust and Cargo can be installed via your particular system’s package manager or via: <https://rustup.rs/>

Installation
------------

This plugin can be installed via:

    python -m pip install pelican-minify

As long as you have not explicitly added a `PLUGINS` setting to your Pelican settings file, then the newly-installed plugin should be automatically detected and enabled. Otherwise, you must add `minify` to your existing `PLUGINS` list. For more information, please see the [How to Use Plugins](https://docs.getpelican.com/en/latest/plugins.html#how-to-use-plugins) documentation.

Usage
-----

By default, all HTML and CSS files will be compressed, including inline JavaScript and CSS rules in `<script>` and `<style>` tags.

To configure the behavior of the plugin, add the following variables in your Pelican settings file (values shown here are the default values):

```python
CSS_MIN = True
HTML_MIN = True
INLINE_CSS_MIN = True
INLINE_JS_MIN = True
```

Please note that `INLINE_CSS_MIN` and `INLINE_JS_MIN` require that `HTML_MIN` be enabled.

Contributing
------------

Contributions are welcome and much appreciated. Every little bit helps. You can contribute by improving the documentation, adding missing features, and fixing bugs. You can also help out by reviewing and commenting on [existing issues][].

To start contributing to this plugin, review the [Contributing to Pelican][] documentation, beginning with the **Contributing Code** section.

[existing issues]: https://github.com/pelican-plugins/minify/issues
[Contributing to Pelican]: https://docs.getpelican.com/en/latest/contribute.html

License
-------

This project is licensed under the MIT license.
