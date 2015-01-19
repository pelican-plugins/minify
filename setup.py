#!/usr/bin/env python
import codecs

from setuptools import setup


with codecs.open('README.rst', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='pelican-minification',
    description='Minifies HTML, CSS and JS of generated Pelican content.',
    version='0.1.1',
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
