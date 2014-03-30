# -*- coding: utf-8 -*-

import htmlmin
import os

from codecs import open

from fnmatch import fnmatch

from pelican import signals


__version__ = '0.1.0'


def minify(pelican):
    """
    Minifies the files.
    :param pelican: the pelican object
    :type pelican: pelican.Pelican
    """
    print type(pelican)
    for path, subdirs, files in os.walk(pelican.output_path):
        for name in files:
            # minify HTML using htmlmin
            if fnmatch(name, '*.html'):
                path_file = os.path.join(path, name)
                try:
                    with open(path_file, 'r+', encoding='utf-8') as f:
                        content = htmlmin.minify(
                            f.read(),
                            remove_comments=True,
                            remove_empty_space=True,
                            reduce_boolean_attributes=True,
                            keep_pre=True,
                        )
                        f.seek(0)
                        f.write(content)
                        f.truncate()
                except Exception as e:
                    raise Exception(
                        'unable to minify HTML of file %(file)s, exception was %(exception)r' % {
                            'file': path_file,
                            'exception': e,
                        }
                    )


def register():
    """
    Registers after the content was generated.
    """
    signals.finalized.connect(minify)
