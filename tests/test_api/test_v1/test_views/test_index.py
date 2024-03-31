#!/usr/bin/python3
"""
Contains the class TestIndexDocs
"""

import inspect
import pep8
import unittest


class TestViewIndexDocs(unittest.TestCase):
    """Class for testing documentation of the index"""

    def test_pep8_conformance_index(self):
        """Test that index.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['api/v1/views/index.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_index(self):
        """Test that tests/test_index.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files([
            'tests/test_api/test_v1/test_views/test_index.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
