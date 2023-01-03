from fnmatch import fnmatch
from functools import lru_cache
import logging
import os

import minify_html

from pelican import signals

__version__ = "1.0.0"

LOGGER = logging.getLogger(__name__)


class Minification:
    """File content minification"""

    def __init__(self, pelican):
        """Minifies the files

        :param pelican: the pelican object
        :type pelican: pelican.Pelican
        """
        LOGGER.info("Minification in progress...")

        # Get settings
        minify_css = pelican.settings.get("CSS_MIN", True)
        minify_html = pelican.settings.get("HTML_MIN", True)
        minify_js = pelican.settings.get("JS_MIN", True)
        minify_inline_css = pelican.settings.get("INLINE_CSS_MIN", True)
        minify_inline_js = pelican.settings.get("INLINE_JS_MIN", True)

        for path, _, files in os.walk(pelican.output_path):
            for name in files:
                path_file = os.path.join(path, name)

                is_html = fnmatch(name, "*.html")
                is_css = fnmatch(name, "*.css")
                is_js = fnmatch(name, "*.js")

                if is_html and minify_html:
                    self.write_to_file(
                        path_file,
                        lambda content: self.minify(
                            content, minify_inline_css, minify_inline_js
                        ),
                    )

                if is_css and minify_css:
                    self.write_to_file(
                        path_file,
                        lambda content: self.minify(content, True, False),
                    )

                if is_js and minify_js:
                    self.write_to_file(
                        path_file, lambda content: self.minify(content, False, True)
                    )

    def minify(self, content, minify_css, minify_js):
        return minify_html.minify(
            content,
            do_not_minify_doctype=True,
            keep_spaces_between_attributes=True,
            minify_css=minify_css,
            minify_js=minify_js,
        )

    @staticmethod
    def write_to_file(path_file, callback):
        """Read the content of the given file, put the content into the callback
        and writes the result back to the file.

        :param path_file: the path to the file
        :type path_file: str
        :param callback: the callback function
        :type callback: function
        """
        try:
            with open(path_file, "r+", encoding="utf-8") as f:
                content = callback(f.read())
                f.seek(0)
                f.write(content)
                f.truncate()
        except Exception as e:
            raise Exception(
                "unable to minify file %(file)s, exception was %(exception)r"
                % {"file": path_file, "exception": e}
            ) from e


@lru_cache(maxsize=None)
def minification_method(method, content):
    """Cached wrapper for minification method

    Some JavaScript or CSS tags may be similar from page to page;
    so caching the return of this function can speed up the minification process.

    :param content: JavaScript or CSS code
    :type content: <str>
    :return: Minified code
    :rtype: <str>
    """
    return method(content)


def register():
    """Register the plugin after the content was generated"""
    signals.finalized.connect(Minification)
