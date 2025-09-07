

```python
import nmap
import argparse


parser = argparse.ArgumentParser(description='Simple Nmap vulnerability scanner')
parser.add_argument('--target', help='Target IP or hostname', required=True)
args = parser.parse_args()

target = args.target


nm = nmap.PortScanner()

print(f"Scanning {target} for open ports...")


nm.scan(hosts=target, arguments='-sV -T4')

for host in nm.all_hosts():
    print(f"\nHost: {host}")
    print(f"State: {nm[host].state()}")
    
    for proto in nm[host].all_protocols():
        print(f"\nProtocol: {proto}")
        
        lport = nm[host][proto].keys()
        for port in sorted(lport):
            service = nm[host][proto][port]['name']
            version = nm[host][proto][port].get('version', '')
            print(f"Port {port}\tService: {service}\tVersion: {version}")
          
            risky_ports = {21: "FTP", 23: "Telnet", 80: "HTTP", 445: "SMB"}
            if port in risky_ports:
                print(f"⚠️ Risky Port Detected! {port} ({risky_ports[port]})")
