#!usr/bin/env python
# -*- coding: utf-8 -*-
"""PASSWORD!"""

import data
ACCESS = False

COUNTER = 3
while ACCESS != True:
    ATTEMPT = raw_input(
        "What is your password ({} attempts remaining)?".format(int(COUNTER)))
    if ATTEMPT == data.PASSWORD:
        ACCESS is True
        print "Access granted!"
    COUNTER -= 1
    if COUNTER is 0:
        print "Try again another time."
        break
