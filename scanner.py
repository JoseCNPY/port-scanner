# Basic Port Scanner
# Version 1.1
# Educational use only

import os
import socket
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

VERSION = "1.1"

COMMON_PORTS = {
    20: "FTP Data",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP Server",
    68: "DHCP Client",
    80: "HTTP",
    110: "POP3",
    123: "NTP",
    135: "MS RPC",
    139: "NetBIOS",
    143: "IMAP",
    161: "SNMP",
    389: "LDAP",
    443: "HTTPS",
    445: "SMB",
    587: "SMTP Secure",
    993: "IMAPS",
    995: "POP3S",
    1433: "MSSQL",
    3306: "MySQL",
    3389: "Remote Desktop",
    5432: "PostgreSQL",
    5900: "VNC",
    8080: "HTTP Alternate"
}


def check_port(target_ip, port, service):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((target_ip, port))

            if result == 0:
                return port, service

    except socket.error:
        return None

    return None


def scan_ports(target_ip):
    open_ports = []

    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = []

        for port, service in COMMON_PORTS.items():
            future = executor.submit(check_port, target_ip, port, service)
            futures.append(future)

        for future in as_completed(futures):
            result = future.result()

            if result:
                port, service = result
                print(f"Port {port} open ({service})")
                open_ports.append((port, service))

    open_ports.sort()
    return open_ports


def save_results(target, target_ip, open_ports, duration):
    folder = "Scans"

    if not os.path.exists(folder):
        os.makedirs(folder)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    safe_target = target.replace(".", "_")
    filename = f"{folder}/{safe_target}_{timestamp}.txt"

    with open(filename, "w") as file:
        file.write("=" * 50 + "\n")
        file.write(f"Basic Port Scanner v{VERSION}\n")
        file.write(f"Target (input): {target}\n")
        file.write(f"Resolved IP: {target_ip}\n")
        file.write(f"Start: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"Scan duration: {duration}\n")
        file.write(f"Open ports count: {len(open_ports)}\n")
        file.write("=" * 50 + "\n")

        if open_ports:
            file.write("Open ports found:\n")
            for port, service in open_ports:
                file.write(f"- {port}: {service}\n")
        else:
            file.write("No open ports were found on the common list.\n")

    print(f"Results saved to {filename}")


def main():
    print(f"Basic Port Scanner v{VERSION}")

    while True:
        while True:
            target = input("Enter IP or domain (or type 'exit' to quit): ").strip()

            if not target:
                print("Target cannot be empty. Please try again.\n")
                continue

            if target.lower() == "exit":
                print("Goodbye.")
                input("Press Enter to exit...")
                return

            try:
                target_ip = socket.gethostbyname(target)
                break
            except socket.gaierror:
                print("Invalid IP or domain. Please try again.\n")

        scan_start = datetime.now()

        print("-" * 50)
        print(f"Scanning target: {target_ip}")
        print(f"Start: {scan_start.strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 50)

        open_ports = scan_ports(target_ip)

        scan_end = datetime.now()
        duration = scan_end - scan_start

        print("-" * 50)
        if open_ports:
            print("Open ports found:")
            for port, service in open_ports:
                print(f"- {port}: {service}")
        else:
            print("No open ports were found on the common list.")

        print(f"Open ports count: {len(open_ports)}")
        print(f"Scan duration: {duration}")

        save_results(target, target_ip, open_ports, duration)

        print("Scan complete.")

        while True:
            again = input("Do you want to scan another target? (y/n): ").lower().strip()

            if again == "y":
                break

            if again == "n":
                print("Goodbye.")
                input("Press Enter to exit...")
                return

            print("Invalid option. Please type 'y' or 'n'.\n")


if __name__ == "__main__":
    main()