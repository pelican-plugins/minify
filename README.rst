pelican-minification
====================

Minification for Pelican pages.


Installation and Usage
----------------------

pelican-minification depends on the following packages that will be installed automatically, see below:

* `htmlmin >= 0.1.5`_
* `csscompressor >= 0.9.1`_


Install pelican-minification into your Python interpreter using pip:

.. code-block:: shell

    pip install pelican-minification


Then add the plugin to the PLUGINS setting within your *pelicanconf.py*:

.. code-block:: python

    PLUGINS = [
        ...
        'minification',
    ]

Upon calling the *pelican* command now, all HTML and CSS files are compressed automatically.


.. _htmlmin >= 0.1.5: https://pypi.python.org/pypi/htmlmin/0.1.5
.. _csscompressor >= 0.9.1: https://pypi.python.org/pypi/csscompressor/0.9.3
