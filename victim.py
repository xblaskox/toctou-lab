#!/usr/bin/env python3
import os
import time

filename ="/tmp/demo_file.txt"

print(f"[Victim] Checking assess to {filename}")
if os.access(filename, os.R_OK):
  print("[Victim] File is readable. Waiting before opening...")
  time.sleep(2) # Artificial delay (race window)
  with open(filename, 'r')as f:
    content=f.read()
    print(f"[Victim] File contents:\n{content}")
else:
  print("[Victim] File is not readable.")
