#!/usr/bin/python3
"""
Contains the class TestAppDocs
"""

import inspect
import pep8
import unittest


class TestAppDocs(unittest.TestCase):
    """Class for testing documentation of the app"""

    def test_pep8_conformance_app(self):
        """Test that app.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['app.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_app(self):
        """Test that tests/test_app.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_app.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
