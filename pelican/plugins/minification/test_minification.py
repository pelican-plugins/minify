import os
from shutil import copytree, rmtree
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

    html = (
        os.path.join(PATH_TEST_DATA_DIR, "sample.html"),
        os.path.join(PATH_TEMP_DIR, "sample.html"),
    )
    css = (
        os.path.join(PATH_TEST_DATA_DIR, "styles.css"),
        os.path.join(PATH_TEMP_DIR, "styles.css"),
    )

    def setUp(self) -> None:
        self.settings = get_settings()
        self.settings["OUTPUT_PATH"] = PATH_TEMP_DIR
        self.context = get_context(self.settings)
        copytree(PATH_TEST_DATA_DIR, PATH_TEMP_DIR, dirs_exist_ok=True)

    def tearDown(self) -> None:
        rmtree(PATH_TEMP_DIR)

    def __get_file_content(self, path):
        content = []
        with open(path) as f:
            content = f.readlines()
        return "".join(content)

    def __load_files(self, paths):
        return (self.__get_file_content(paths[0]), self.__get_file_content(paths[1]))

    def test_minify_all(self):
        Minification(Pelican(self.settings))

        html = self.__load_files(self.html)
        css = self.__load_files(self.css)

        self.assertNotEqual(html[0], html[1])
        self.assertNotEqual(css[0], css[1])
        self.assertGreater(len(html[0]), len(html[1]))
        self.assertGreater(len(css[0]), len(css[1]))

    def test_minify_html_only(self):
        self.settings["CSS_MIN"] = False
        Minification(Pelican(self.settings))

        html = self.__load_files(self.html)
        css = self.__load_files(self.css)

        self.assertNotEqual(html[0], html[1])
        self.assertEqual(css[0], css[1])
        self.assertGreater(len(html[0]), len(html[1]))

    def test_minify_css_only(self):
        self.settings["HTML_MIN"] = False
        Minification(Pelican(self.settings))

        html = self.__load_files(self.html)
        css = self.__load_files(self.css)

        self.assertEqual(html[0], html[1])
        self.assertNotEqual(css[0], css[1])
        self.assertGreater(len(css[0]), len(css[1]))

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
