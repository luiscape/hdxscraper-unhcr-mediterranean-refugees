#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests

def Fetch():
  '''Fetches data from UNHCR's Mediterrean instance.'''

  u = 'http://data.unhcr.org/api/stats/mediterranean/monthly_arrivals_by_country.json'
  r = requests.get(u)

  return r.json()
