#!/usr/bin/python3
import unittest
import sys
import pep8
import json
import os
from io import StringIO
from models.base import Base
'''
The module tests the base class
'''


class TestBase(unittest.TestCase):
    '''
    class to run tests
    '''

    def setUp(self):
        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_pep8_module(self):
        p = pep8.StyleGuide(quiet=True)
        p1 = p.check_files(['models/base.py'])
        self.assertEqual(p1.total_errors, 0, 'fix pep8')

    def test_pep8_test(self):
        p = pep8.StyleGuide(quiet=True)
        p1 = p.check_files(['models/base.py'])
        self.assertEqual(p.total_errors, 0, 'fix pep8')

    def test_docstrings(self):
        self.assertIsNotNone(module_doc)
        self.assertIsNotNone(Base.__doc__)
        self.assertIs(hasattr(Base, '__init__'), True)
        self.assertIsNotNone(Base.__init__.__doc__)

    def test_id(self):
        Base.Base__nb_objects = 0
        b = Base()
        b1 = Base()
        b2 = Base()
        b3 = Base(12)
        b4 = Base()
        self.assertEqual(b.id, 1)
        self.assertEqual(b1.id, 2)
        self.assertEqual(b2.id, 3)
        self.assertEqual(b3.id, 12)
        self.assertEqual(b4.id, 4)
