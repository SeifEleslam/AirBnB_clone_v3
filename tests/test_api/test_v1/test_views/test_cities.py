#!/usr/bin/python3
"""
Contains the class TestCitiesDocs
"""

import inspect
import pep8
import unittest


class TestViewCitiesDocs(unittest.TestCase):
    """Class for testing documentation of the cities"""

    def test_pep8_conformance_cities(self):
        """Test that cities.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['api/v1/views/cities.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_cities(self):
        """Test that tests/test_cities.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files([
            'tests/test_api/test_v1/test_views/test_cities.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
