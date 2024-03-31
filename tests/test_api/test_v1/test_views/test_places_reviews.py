#!/usr/bin/python3
"""
Contains the class TestReviewsDocs
"""

import inspect
import pep8
import unittest


class TestViewReviewsDocs(unittest.TestCase):
    """Class for testing documentation of the users"""

    def test_pep8_conformance_users(self):
        """Test that users.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['api/v1/views/places_reviews.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_users(self):
        """Test that tests/test_users.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(
            ['tests/test_api/test_v1/test_views/test_places_reviews.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
