#!/usr/bin/python3
"""
Contains the class TestPlacesDocs
"""

import inspect
import pep8
import unittest


class TestViewPlacesDocs(unittest.TestCase):
    """Class for testing documentation of the places"""

    def test_pep8_conformance_places(self):
        """Test that places.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['api/v1/views/places.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_places(self):
        """Test that tests/test_places.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files([
            'tests/test_api/test_v1/test_views/test_places.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
