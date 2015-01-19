# -*- coding: utf-8 -*-
import csscompressor
import htmlmin
import os

from codecs import open

from fnmatch import fnmatch

from pelican import signals


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
                    self.write_to_file(
                        path_file,
                        lambda content: htmlmin.minify(
                            content,
                            remove_comments=True,
                            remove_empty_space=True,
                            reduce_boolean_attributes=True,
                            keep_pre=True,
                            remove_optional_attribute_quotes=False,
                        )
                    )
                elif fnmatch(name, '*.css'):
                    self.write_to_file(
                        path_file,
                        lambda content: csscompressor.compress(content)
                    )

    @staticmethod
    def write_to_file(path_file, callback):
        """
        Reads the content of the given file, puts the content into the callback and writes the result back to the file.
        :param path_file: the path to the file
        :type path_file: str
        :param callback: the callback function
        :type callback: function
        """
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
