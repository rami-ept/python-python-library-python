import unittest
import importlib

core = importlib.import_module("fake-pypi-project.core")

class FakePyPiProjectTestCase(unittest.TestCase):
    def test_fakepypiproject(self):
        self.assertEqual(core.get_message(), 'Hello World!')

if __name__ == '__main__':
    unittest.main()