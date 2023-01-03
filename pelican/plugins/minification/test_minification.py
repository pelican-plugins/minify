import os
from shutil import copy, rmtree
from tempfile import mkdtemp
import unittest

from minification import Minification

from pelican import Pelican
from pelican.tests.support import get_context, get_settings

# each setting, all together
PATH_CURRENT_DIR = os.path.dirname(__file__)
PATH_TEST_DATA_DIR = os.path.join(PATH_CURRENT_DIR, "test_data")
PATH_TEMP_DIR = mkdtemp(prefix="pelicantests.")


class TestMinification(unittest.TestCase):
    def __get_file_content(self, path):
        content = []
        with open(path) as f:
            content = f.readlines()
        return "".join(content)

    def __load_files(self, paths):
        return (self.__get_file_content(paths[0]), self.__get_file_content(paths[1]))

    def setUp(self) -> None:
        self.tmp_dir = mkdtemp(prefix="pelicantests.")
        self.settings = get_settings()
        self.settings["OUTPUT_PATH"] = self.tmp_dir
        self.context = get_context(self.settings)
        self.html = (
            os.path.join(PATH_TEST_DATA_DIR, "sample.html"),
            os.path.join(self.tmp_dir, "sample.html"),
        )
        self.css = (
            os.path.join(PATH_TEST_DATA_DIR, "styles.css"),
            os.path.join(self.tmp_dir, "styles.css"),
        )
        self.js = (
            os.path.join(PATH_TEST_DATA_DIR, "index.js"),
            os.path.join(self.tmp_dir, "index.js"),
        )
        copy(self.html[0], self.html[1])
        copy(self.css[0], self.css[1])
        copy(self.js[0], self.js[1])

    def tearDown(self) -> None:
        rmtree(self.tmp_dir)

    def get_files(self):
        return (
            self.__load_files(self.html),
            self.__load_files(self.css),
            self.__load_files(self.js),
        )

    def test_minify_all(self):
        Minification(Pelican(self.settings))

        html, css, js = self.get_files()

        self.assertNotEqual(html[0], html[1])
        self.assertGreater(len(html[0]), len(html[1]))
        self.assertNotEqual(css[0], css[1])
        self.assertGreater(len(css[0]), len(css[1]))
        self.assertNotEqual(js[0], js[1])
        self.assertGreater(len(js[0]), len(js[1]))

    def test_minify_html_only(self):
        self.settings["CSS_MIN"] = False
        self.settings["JS_MIN"] = False
        Minification(Pelican(self.settings))

        html, css, js = self.get_files()

        self.assertNotEqual(html[0], html[1])
        self.assertGreater(len(html[0]), len(html[1]))
        self.assertEqual(css[0], css[1])
        self.assertEqual(js[0], js[1])

    def test_minify_css_only(self):
        self.settings["HTML_MIN"] = False
        self.settings["JS_MIN"] = False
        Minification(Pelican(self.settings))

        html, css, js = self.get_files()

        self.assertEqual(html[0], html[1])
        self.assertNotEqual(css[0], css[1])
        self.assertGreater(len(css[0]), len(css[1]))
        self.assertEqual(js[0], js[1])

    def test_minify_js_only(self):
        self.settings["HTML_MIN"] = False
        self.settings["CSS_MIN"] = False
        Minification(Pelican(self.settings))

        html, css, js = self.get_files()

        self.assertEqual(html[0], html[1])
        self.assertEqual(css[0], css[1])
        self.assertNotEqual(js[0], js[1])
        self.assertGreater(len(js[0]), len(js[1]))

    def test_minify_no_inline_css(self):
        self.settings["INLINE_CSS_MIN"] = False
        Minification(Pelican(self.settings))

        html = self.__load_files(self.html)
        self.assertTrue("yellow;\n" in html[1])

    def test_minify_no_inline_js(self):
        self.settings["INLINE_JS_MIN"] = False
        Minification(Pelican(self.settings))

        html = self.__load_files(self.html)
        self.assertTrue(".trim();\n" in html[1])
