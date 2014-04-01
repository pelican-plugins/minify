# -*- coding: utf-8 -*-
import htmlmin
import os

from codecs import open

from fnmatch import fnmatch

from pelican import signals


__version__ = '0.1.0'


class Minification(object):
    """
    Class that does file content minification.
    """
    def __init__(self, pelican):
        """
        Minifies the files.
        :param pelican: the pelican object
        :type pelican: pelican.Pelican
        """
        for path, subdirs, files in os.walk(pelican.output_path):
            for name in files:
                path_file = os.path.join(path, name)

                if fnmatch(name, '*.html'):
                    self.minify_html(path_file)

    def minify_html(self, path_file):
        cb_minify_html = lambda x: htmlmin.minify(
            x,
            remove_comments=True,
            remove_empty_space=True,
            reduce_boolean_attributes=True,
            keep_pre=True,
        )
        self.write_to_file(path_file, cb_minify_html)

    @staticmethod
    def write_to_file(path_file, callback):
        try:
            with open(path_file, 'r+', encoding='utf-8') as f:
                content = callback(f.read())
                f.seek(0)
                f.write(content)
                f.truncate()
        except Exception as e:
            raise Exception(
                'unable to minify file %(file)s, exception was %(exception)r' % {
                    'file': path_file,
                    'exception': e,
                }
            )


def register():
    """
    Registers after the content was generated.
    """
    signals.finalized.connect(Minification)
