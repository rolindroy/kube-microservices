#!/bin/python
# Python environment secret decoder
# @Author: Rolind Roy <rolindroy>

import os
import sys
import base64
import time

arguments = sys.argv[1:]
arg_count = len(arguments)

if arg_count > 0:
    secretKey=sys.argv[1]
else:
    secretKey="secretKey"
while 1 == 1:
    try:
        print("Decoded value for %s is: %s" % (secretKey, os.environ.get(secretKey)));
    except:
        print("Not exist environment value for %s" % secretKey);
    time.sleep(5);
