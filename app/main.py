#!/usr/bin/python
# -*- coding: utf-8 -*-


import collect.fetch as Fetch
import collect.patch as Patch
from utilities.db import CleanTable, StoreRecords
from utilities.format import item

def Main():
  '''Wrapper.'''

  #
  # Collecting data from UNHCR.
  #
  print '%s Collecting data from UNHCR.' % item('bullet')
  data = Fetch.Fetch()

  #
  # Patching data.
  # Epoch time doesn't seem to be 1970.
  #
  print '%s Patching data.' % item('bullet')
  # pdata = Patch.Epoch(data)
  pdata = Patch.Date(data)

  #
  # Storing data in database.
  #
  print '%s Storing records in database.' % item('bullet')
  CleanTable('monthly_arrivals_by_country')
  StoreRecords(pdata, 'monthly_arrivals_by_country')

  print '%s Collected data from UNHCR successfully.' % item('success')
