#!/usr/bin/env python3.6


import os

stage = os.getenv("STAGE", default='dev').upper()

output = f"We'r running in {stage}"

if stage.startswith("PROD"):
    output = "DANGER!!! - " + output

print(output)
