#!/usr/bin/env python3.6
"""
  Run as STAGE="prod" ./running_environ.py
"""

import os


stage = os.environ["STAGE"].upper()

output = f"We'r running in {stage}"

if stage.startswith("PROD"):
    output = "DANGER!!! - " + output

print(output)
