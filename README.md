# Python TCP Port Scanner

A beginner cybersecurity project built with Python to practice TCP networking, socket programming, and input validation.

## Features

- Accepts an IPv4 address as input.
- Validates the IP address.
- Scans multiple TCP ports in one run.
- Validates port numbers from 1 to 65535.
- Uses a connection timeout.
- Reports successful and unsuccessful connection attempts.
- Uses exception handling and `finally` to close sockets.

## Requirements

- Python 3
- No third-party Python packages required.

## How to Run

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Run:

   ```bash
   python portscanner.py
   ```

4. Enter an IPv4 address when prompted.
5. Enter one or more space-separated port numbers.

## Example

```text
Enter ip_address : 192.168.56.1
enter the port number 5000 5001
port 5000 is open
Port 5001: connection failed, error code 10035
```

The output above is an example from a local lab. Results depend on the target, network, operating system, and listening services.

## What I Learned

- Creating TCP sockets with Python's `socket` module.
- Using `connect_ex()` to attempt TCP connections.
- Validating IPv4 addresses with `ipaddress`.
- Converting and validating user input.
- Handling exceptions with `try` and `except`.
- Using `finally` to clean up sockets.
- Understanding that failed connections do not always prove a port is closed.

## Limitations

This is a beginner project, not a replacement for a full-featured scanner such as Nmap. It currently reports connection results rather than performing service detection or vulnerability assessment.

## Responsible Use

Only scan systems you own or have explicit permission to test. Scanning third-party systems without authorization may violate their policies or applicable laws.

## Future Improvements

- Interpret common connection error codes.
- Improve timeout and failure reporting.
- Compare results with Nmap.
- Analyze TCP connection attempts using Wireshark.

---

**Status:** Beginner learning project.
