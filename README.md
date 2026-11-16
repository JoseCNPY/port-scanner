# Basic Port Scanner

An educational Python TCP-connect scanner that checks a **fixed list of common TCP ports** on a hostname or IPv4 address. It resolves the target, runs concurrent connection attempts, and saves timestamped results.

## Features

- Checks selected TCP ports with `socket.connect_ex`
- Resolves hostnames using `socket.gethostbyname`
- Uses `ThreadPoolExecutor` to scan multiple ports concurrently
- Validates empty or unresolvable targets
- Saves results to local `Scans/` files and allows another scan in the same session

## Requirements

Python 3. No third-party packages required.

## Usage

```bash
python scanner.py
```

Enter an **IP or domain you own or are expressly authorized to test**. Type `exit` to quit. The output reports each TCP port where a connection was successful and writes the list to a timestamped report in `Scans/`.

## How it works

The script resolves a hostname to one IPv4 address, checks ports defined in `COMMON_PORTS`, applies a one-second timeout per connection, and reports ports where `connect_ex` returns success. Descriptions such as `HTTP` are **common port labels, not verified service detection**.

## Known limitations

- Checks only the fixed list of TCP ports; **does not scan UDP or all 65,535 TCP ports**
- Supports IPv4 addresses and IPv4 DNS resolution, not IPv6
- A filtered, blocked, timed-out, or unreachable service can appear the same as a closed port
- Does not identify service versions, vulnerabilities, or the security of the host
- No automated test suite yet; the sample below is an illustration, **not evidence of a live scan**

## Illustrative output format

```text
Basic Port Scanner v1.1
Enter IP or domain (or type 'exit' to quit): <authorized-host>
Scanning target: <resolved-ip>
Port 80 open (HTTP)
Open ports count: 1
Results saved to Scans/<target>_<timestamp>.txt
```

The lines above only demonstrate the expected format; actual results depend on the target and network.

## Next steps

- Allow custom port selection
- Add tests with a locally controlled TCP listener
- Offer structured CSV/JSON output

## Responsible use

Only test systems that you own or have explicit authorization to scan. Do not assume an open port means a vulnerability.
