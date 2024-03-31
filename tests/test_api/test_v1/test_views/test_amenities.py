#!/usr/bin/python3
"""
Contains the class TestAmenitiesDocs
"""

import inspect
import pep8
import unittest


class TestViewAmenitiesDocs(unittest.TestCase):
    """Class for testing documentation of the amenities"""

    def test_pep8_conformance_amenities(self):
        """Test that amenities.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['api/v1/views/amenities.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_amenities(self):
        """Test that tests/test_amenities.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files([
            'tests/test_api/test_v1/test_views/test_amenities.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
