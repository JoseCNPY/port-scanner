[README.md](https://github.com/user-attachments/files/27210767/README.md)
# Basic Port Scanner

A simple Python TCP port scanner that checks common ports on a target IP address or domain.

## Features

- Scan common TCP ports
- Multi-threaded scanning for faster results
- Resolves domains to IP addresses
- Saves results to timestamped files
- Input validation (handles invalid or empty input)
- Repeat scans without restarting the program

## Technologies Used

- Python
- Socket library
- concurrent.futures (ThreadPoolExecutor)

## How to Use

Run the program:

python scanner.py

Then enter a target when prompted:

Enter IP or domain: google.com

## Example Output

Port 80 open (HTTP)
Port 443 open (HTTPS)

## Project Structure

port-scanner/
│
├── scanner.py
├── README.md
├── Scans/
│   └── scan_YYYY-MM-DD_HH-MM-SS.txt

## Limitations

- Only scans common ports (not full range)
- No service version detection
- No vulnerability scanning

## Future Improvements

- Custom port range input
- Export results to CSV
- Add GUI interface
- Improve scan speed further

## Disclaimer

This project is for educational purposes only.
Only scan systems you own or have permission to test.
