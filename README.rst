pelican-minification
====================

Content minification for the `Pelican`_ site generator.
This plugin can compress HTML & CSS files as well as inline CSS and JavaScript in HTML files.


Installation and Usage
----------------------

pelican-minification depends on the following packages that will be installed automatically, see below:

* `htmlmin`_
* `csscompressor`_
* `jsmin`_
* `BeautifulSoup`_
* `Pelican`_


Install pelican-minification into your Python interpreter using pip:

.. code-block:: shell

    pip install pelican-minification


Then add the plugin to the ``PLUGINS`` setting within your *pelicanconf.py*:

.. code-block:: python

    PLUGINS = [
        ...
        'pelican.plugins.minification',
    ]

Upon calling the *pelican* command now, all HTML and CSS files are compressed automatically;
including inline JavaScript and CSS rules in ``<script>`` and ``<style>`` tags.

.. _htmlmin: https://pypi.python.org/pypi/htmlmin
.. _csscompressor: https://pypi.python.org/pypi/csscompressor
.. _jsmin: https://pypi.org/project/jsmin
.. _BeautifulSoup: https://pypi.org/project/beautifulsoup4
.. _Pelican: https://pypi.python.org/pypi/pelican
