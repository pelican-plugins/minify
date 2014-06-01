#!/usr/bin/env python
import codecs
import os
import re

from setuptools import setup


with codecs.open('README.rst', encoding='utf-8') as f:
    long_description = f.read()


def get_version():
    """
    Returns the version of the package from the __init__ file.
    :return: version number
    :rtype: str
    """
    with codecs.open(os.path.join(os.path.dirname(__file__), 'minification', '__init__.py'), encoding='utf-8') as f:
        version_file = f.read()
        version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
        if version_match:
            return version_match.group(1)
        raise RuntimeError('Unable to fetch version')


setup(
    name='pelican-minification',
    description='Minifies HTML, CSS and JS of generated Pelican content.',
    version=get_version(),
    author='Alexander Herrmann',
    author_email='darignac@gmail.com',
    license='MIT',
    url='https://github.com/dArignac/pelican-minification',
    long_description=long_description,
    packages=[
        'minification',
    ],
    install_requires=[
        'csscompressor>=0.9.1',
        'htmlmin>=0.1.5',
        'Pelican',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: Markup',
    ]
)
