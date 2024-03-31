#!/usr/bin/python3
"""
Contains the class TestStatesDocs
"""

import inspect
import pep8
import unittest


class TestViewStatesDocs(unittest.TestCase):
    """Class for testing documentation of the states"""

    def test_pep8_conformance_states(self):
        """Test that states.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['api/v1/views/states.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_states(self):
        """Test that tests/test_states.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(
            ['tests/test_api/test_v1/test_views/test_states.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
