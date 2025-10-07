#!/usr/bin/env bash
set -e
for h in 1.1.1.1 8.8.8.8; do if ping -c1 -W1 $h >/dev/null 2>&1; then echo "$h up"; else echo "$h down"; fi; done
