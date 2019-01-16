#!/bin/python
# Python environment variable reader
# @Author: Rolind Roy <rolindroy>

import os
import time

env_key="env_value_key"
while 1 == 1:
    try:
        print("Value for the env variable %s is: %s" % (env_key, os.environ.get(env_key)));
    except KeyError:
        print("Not exist environment value for %s" % env_key)
    time.sleep(5);
