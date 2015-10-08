#!/usr/bin/python
# -*- coding: utf-8 -*-

# system
import os
import sys
dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
sys.path.append(os.path.join(dir, 'app'))

# testing
import mock
import unittest
from mock import patch

# program
import app.collect.fetch as Fetch

class TestFetch(unittest.TestCase):
  '''Unit tests for testing if the communication with UNCHR works as expected.'''

  def test_fetch_returns_array_dictionary(self):
    d = Fetch.Fetch()
    assert type(d) == type([{}])
