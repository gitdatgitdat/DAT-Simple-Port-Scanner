## DAT Simple Port Scanner

A simple yet effective Python-based port scanner that checks for open TCP ports on a target host within a specified range. 

---

## Features

Multi-threading for rapid scanning across large port ranges

Target validation: Accepts both IP addresses and domain names

Port validation: Ensures proper port range and ordering

Service name resolution using socket.getservbyport

Clean, readable output with open-port listing and service names

Graceful loop for repeated scans without restarting the program

---

## Usage

Enter a target (IP or domain)

Enter a port range (start and end)

View open ports with resolved service names

Repeat or type exit to quit

---

## Example

Scanning google.com from port 1 to 1000...

Open Ports Found:
  • Port 9   (discard)
  • Port 81  (hosts2-ns)
  • Port 995 (pop3s)

----------------------------------------

## Requirements

Python 3.10+

No external dependencies (uses Python standard library only)

---
