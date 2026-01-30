# CEH v13 Lab Environment - Complete Design

**Date:** 2026-01-30  
**Purpose:** Educational - CEH Practical & Multiple Choice Exam Preparation  
**Status:** In Progress - Design Phase  
**Priority:** High (Exam Preparation)

---

## Overview

Complete penetration testing lab environment for Certified Ethical Hacker (CEH) v13 certification exam preparation. Built on existing Proxmox homelab infrastructure with complete network isolation for safe malware analysis and exploitation practice.

**Key Requirements:**
- Support all 20 CEH v13 modules
- Safe malware handling and analysis
- Complete network isolation from production
- Realistic attack scenarios
- Snapshot-based reset capability
- Cost: $0 (uses existing infrastructure)

---

## Lab Architecture

### Network Topology

```
Proxmox Homelab
│
├── Production VLAN (10.92.x.x) - ISOLATED
│   ├── TheoShift (Containers 132, 134)
│   ├── LDC Tools (Containers 133, 135)
│   ├── QuantShift (Containers 137, 138)
│   └── PostgreSQL (Container 131)
│
├── Management VLAN (10.92.3.x) - ISOLATED
│   └── Proxmox Management Interface
│
└── CEH Lab VLAN (10.99.1.x) - COMPLETELY ISOLATED ⚠️
    ├── NO internet access
    ├── NO route to production networks
    ├── NO route to management network
    ├── Accessible only via jump box or Proxmox console
    │
    ├── Attack Infrastructure
    │   ├── Kali Linux (Primary) - 10.99.1.10
    │   ├── Parrot Security OS (Alternative) - 10.99.1.11
    │   └── Jump Box (SSH Gateway) - 10.99.1.5
    │
    ├── Windows Targets
    │   ├── Windows 10 Pro (Workstation) - 10.99.1.20
    │   ├── Windows 11 Pro (Workstation) - 10.99.1.21
    │   ├── Windows Server 2019 (AD/DC) - 10.99.1.22
    │   └── Windows Server 2022 (File/Web) - 10.99.1.23
    │
    ├── Linux Targets
    │   ├── Ubuntu 22.04 Server - 10.99.1.30
    │   ├── Ubuntu 20.04 Desktop - 10.99.1.31
    │   ├── CentOS 8 Stream - 10.99.1.32
    │   ├── Metasploitable 2 - 10.99.1.40
    │   └── Metasploitable 3 - 10.99.1.41
    │
    ├── Web Application Targets
    │   ├── DVWA (Damn Vulnerable Web App) - 10.99.1.50
    │   ├── OWASP WebGoat - 10.99.1.51
    │   ├── OWASP Juice Shop - 10.99.1.52
    │   ├── bWAPP - 10.99.1.53
    │   └── Mutillidae II - 10.99.1.54
    │
    ├── Malware Analysis Lab
    │   ├── FlareVM (Windows Analysis) - 10.99.1.60
    │   ├── REMnux (Linux Analysis) - 10.99.1.61
    │   └── Cuckoo Sandbox - 10.99.1.62
    │
    ├── Network Infrastructure
    │   ├── pfSense Firewall - 10.99.1.1
    │   ├── DNS Server (BIND) - 10.99.1.2
    │   ├── FakeNet-NG (Simulated Internet) - 10.99.1.3
    │   └── Vulnerable Router (DD-WRT) - 10.99.1.4
    │
    └── Specialized Targets
        ├── Android Emulator (Mobile) - 10.99.1.70
        ├── IoT Device Simulator - 10.99.1.71
        └── Cloud Simulation (LocalStack) - 10.99.1.72
```

---

## VM Specifications

### Phase 1: Core Lab (Minimum Viable)

**Total Resources:** 24 GB RAM, 12 CPU cores, 400 GB disk

| VM Name | OS | RAM | CPU | Disk | Purpose |
|---------|-----|-----|-----|------|---------|
| Kali Linux | Kali 2024.1 | 4 GB | 2 | 60 GB | Primary attack platform |
| Windows 10 | Win 10 Pro | 4 GB | 2 | 60 GB | Target workstation |
| Windows Server 2019 | WS 2019 | 4 GB | 2 | 80 GB | AD/DC target |
| Ubuntu 22.04 | Ubuntu Server | 2 GB | 2 | 30 GB | Linux target |
| Metasploitable 2 | Ubuntu 8.04 | 1 GB | 1 | 8 GB | Vulnerable target |
| DVWA | Ubuntu 20.04 | 2 GB | 1 | 20 GB | Web app target |
| pfSense | FreeBSD | 1 GB | 1 | 10 GB | Network segmentation |

### Phase 2: Extended Lab (Full Coverage)

**Total Resources:** 48 GB RAM, 24 CPU cores, 800 GB disk

Add to Phase 1:
- Parrot Security OS (4 GB RAM, 2 CPU, 60 GB)
- Windows 11 Pro (4 GB RAM, 2 CPU, 60 GB)
- Windows Server 2022 (4 GB RAM, 2 CPU, 80 GB)
- Ubuntu 20.04 Desktop (4 GB RAM, 2 CPU, 40 GB)
- CentOS 8 Stream (2 GB RAM, 2 CPU, 30 GB)
- Metasploitable 3 (2 GB RAM, 2 CPU, 20 GB)
- WebGoat (2 GB RAM, 1 CPU, 20 GB)
- Juice Shop (2 GB RAM, 1 CPU, 20 GB)
- bWAPP (2 GB RAM, 1 CPU, 20 GB)
- Mutillidae II (2 GB RAM, 1 CPU, 20 GB)

### Phase 3: Malware Analysis Lab

**Total Resources:** +16 GB RAM, +8 CPU cores, +200 GB disk

- FlareVM (Windows 10 + tools) (6 GB RAM, 2 CPU, 80 GB)
- REMnux (Ubuntu-based) (4 GB RAM, 2 CPU, 60 GB)
- Cuckoo Sandbox (Ubuntu) (4 GB RAM, 2 CPU, 60 GB)
- FakeNet-NG (Ubuntu) (2 GB RAM, 2 CPU, 20 GB)

**Note:** Not all VMs run simultaneously. Use snapshots and start/stop as needed per module.

---

## Network Isolation Configuration

### Proxmox Network Setup

```bash
# Create isolated bridge for CEH lab
auto vmbr99
iface vmbr99 inet static
    address 10.99.1.1
    netmask 255.255.255.0
    bridge_ports none
    bridge_stp off
    bridge_fd 0
    # NO gateway = no internet access
    # NO routing = no access to other VLANs

# Firewall rules (iptables)
# Block all traffic from CEH VLAN to production
iptables -A FORWARD -s 10.99.1.0/24 -d 10.92.0.0/16 -j DROP
iptables -A FORWARD -s 10.99.1.0/24 -o vmbr0 -j DROP

# Block CEH VLAN from internet
iptables -A FORWARD -s 10.99.1.0/24 -o eth0 -j DROP

# Allow only Proxmox console access
# (VNC/SPICE through Proxmox web interface)
```

### pfSense Configuration (Inside CEH VLAN)

```
LAN Interface: 10.99.1.1/24
WAN Interface: Disabled (no uplink)

Firewall Rules:
- Default DENY all
- Allow intra-VLAN traffic only
- Log all connection attempts
- No NAT, no routing outside VLAN
```

---

## Module-by-Module Requirements

### Module 01: Introduction to Ethical Hacking
**Tools:** None (theory)  
**VMs:** None  
**Duration:** 2 hours

### Module 02: Footprinting and Reconnaissance ✅
**Tools:** nmap, nslookup, dig, whois, theHarvester, Maltego, Recon-ng, Shodan  
**VMs Required:**
- Kali Linux (attack)
- Windows 10 (target)
- Ubuntu Server (target)
- DVWA (web target)

**Duration:** 2.5 hours  
**RAM:** 12 GB  
**Practice Scenarios:**
- DNS enumeration
- WHOIS lookups
- Google dorking
- Network scanning
- Email harvesting
- Subdomain enumeration

### Module 03: Scanning Networks
**Tools:** Nmap, Hping3, Netdiscover, Angry IP Scanner  
**VMs Required:**
- Kali Linux
- Windows 10
- Windows Server 2019
- Ubuntu Server
- Metasploitable 2

**Duration:** 3 hours  
**RAM:** 15 GB  
**Practice Scenarios:**
- TCP/UDP scanning
- OS fingerprinting
- Service version detection
- Firewall/IDS evasion
- Network mapping

### Module 04: Enumeration
**Tools:** enum4linux, NBTscan, SNMP-check, ldapsearch  
**VMs Required:**
- Kali Linux
- Windows Server 2019 (AD)
- Windows 10
- Ubuntu Server

**Duration:** 2.5 hours  
**RAM:** 14 GB  
**Practice Scenarios:**
- NetBIOS enumeration
- SNMP enumeration
- LDAP enumeration
- NFS enumeration
- SMB enumeration

### Module 05: Vulnerability Analysis
**Tools:** Nessus, OpenVAS, Nikto, OWASP ZAP  
**VMs Required:**
- Kali Linux
- All target VMs (scan everything)

**Duration:** 3 hours  
**RAM:** 20 GB  
**Practice Scenarios:**
- Automated vulnerability scanning
- Web application scanning
- Report generation
- Prioritizing vulnerabilities

### Module 06: System Hacking
**Tools:** Metasploit, John the Ripper, Hashcat, Mimikatz, pwdump  
**VMs Required:**
- Kali Linux
- Windows 10
- Windows Server 2019
- Metasploitable 2

**Duration:** 4 hours  
**RAM:** 16 GB  
**Practice Scenarios:**
- Password cracking
- Privilege escalation
- Backdoor installation
- Covering tracks
- Keylogging

### Module 07: Malware Threats ⚠️
**Tools:** theZoo, VirusTotal, Process Monitor, Autoruns, Wireshark  
**VMs Required:**
- FlareVM (analysis)
- REMnux (analysis)
- Windows 10 (victim)
- Kali Linux (payload creation)

**Duration:** 3 hours  
**RAM:** 16 GB  
**Practice Scenarios:**
- Static malware analysis
- Dynamic malware analysis
- Trojan creation with Metasploit
- Malware detection/removal
- Behavioral analysis

**Safety:** Completely isolated network, snapshots before infection

### Module 08: Sniffing
**Tools:** Wireshark, tcpdump, Ettercap, Cain & Abel  
**VMs Required:**
- Kali Linux
- Windows 10
- Ubuntu Server
- DVWA (generate traffic)

**Duration:** 2.5 hours  
**RAM:** 12 GB  
**Practice Scenarios:**
- Packet capture
- ARP poisoning
- MITM attacks
- Protocol analysis
- Password sniffing

### Module 09: Social Engineering
**Tools:** Social Engineering Toolkit (SET), Gophish, BeEF  
**VMs Required:**
- Kali Linux
- Windows 10 (victim)
- Ubuntu Desktop (victim)

**Duration:** 2 hours  
**RAM:** 12 GB  
**Practice Scenarios:**
- Phishing campaigns
- Credential harvesting
- Browser exploitation
- USB payload creation

### Module 10: Denial of Service
**Tools:** hping3, LOIC, Slowloris, GoldenEye  
**VMs Required:**
- Kali Linux
- Ubuntu Server (victim)
- DVWA (web target)

**Duration:** 2 hours  
**RAM:** 10 GB  
**Practice Scenarios:**
- SYN flood
- UDP flood
- HTTP flood
- Slowloris attack
- DDoS detection

### Module 11: Session Hijacking
**Tools:** Burp Suite, OWASP ZAP, Wireshark, Ettercap  
**VMs Required:**
- Kali Linux
- DVWA
- Juice Shop
- Windows 10

**Duration:** 2 hours  
**RAM:** 12 GB  
**Practice Scenarios:**
- Session token capture
- Cookie hijacking
- Session fixation
- CSRF attacks

### Module 12: Evading IDS, Firewalls, and Honeypots
**Tools:** Nmap (evasion), Metasploit (encoders), Veil-Evasion  
**VMs Required:**
- Kali Linux
- Windows 10 (with AV)
- pfSense (firewall)
- Snort/Suricata IDS

**Duration:** 3 hours  
**RAM:** 14 GB  
**Practice Scenarios:**
- Firewall rule bypass
- IDS signature evasion
- AV evasion
- Payload obfuscation

### Module 13: Hacking Web Servers
**Tools:** Metasploit, Nikto, DirBuster, Burp Suite  
**VMs Required:**
- Kali Linux
- Ubuntu Server (Apache/Nginx)
- Windows Server 2022 (IIS)
- DVWA

**Duration:** 3 hours  
**RAM:** 14 GB  
**Practice Scenarios:**
- Web server fingerprinting
- Directory traversal
- Server misconfiguration exploitation
- Web shell upload

### Module 14: Hacking Web Applications
**Tools:** Burp Suite, OWASP ZAP, SQLMap, Nikto  
**VMs Required:**
- Kali Linux
- DVWA
- WebGoat
- Juice Shop
- bWAPP
- Mutillidae II

**Duration:** 4 hours  
**RAM:** 16 GB  
**Practice Scenarios:**
- XSS attacks
- CSRF attacks
- File upload vulnerabilities
- Command injection
- Authentication bypass

### Module 15: SQL Injection
**Tools:** SQLMap, Burp Suite, Havij  
**VMs Required:**
- Kali Linux
- DVWA
- bWAPP
- Mutillidae II

**Duration:** 3 hours  
**RAM:** 12 GB  
**Practice Scenarios:**
- Error-based SQL injection
- Blind SQL injection
- Time-based SQL injection
- Database enumeration
- Data exfiltration

### Module 16: Hacking Wireless Networks
**Tools:** Aircrack-ng, Reaver, Wifite, Kismet  
**VMs Required:**
- Kali Linux (with USB WiFi adapter)
- Wireless router (physical or simulated)

**Duration:** 3 hours  
**RAM:** 4 GB  
**Practice Scenarios:**
- WEP cracking
- WPA/WPA2 cracking
- WPS attacks
- Evil twin attacks
- Rogue AP detection

**Note:** Requires USB WiFi adapter with monitor mode support

### Module 17: Hacking Mobile Platforms
**Tools:** Android Studio, Drozer, APKTool, MobSF  
**VMs Required:**
- Kali Linux
- Android Emulator (AVD)
- Windows 10 (for Android Studio)

**Duration:** 3 hours  
**RAM:** 12 GB  
**Practice Scenarios:**
- APK reverse engineering
- Mobile app vulnerability scanning
- Android debugging
- Insecure data storage

### Module 18: IoT Hacking
**Tools:** Shodan, Nmap, Firmware Analysis Toolkit  
**VMs Required:**
- Kali Linux
- IoT device simulator
- Vulnerable IoT firmware

**Duration:** 2 hours  
**RAM:** 8 GB  
**Practice Scenarios:**
- IoT device discovery
- Firmware extraction
- Firmware analysis
- IoT protocol exploitation

### Module 19: Cloud Computing
**Tools:** ScoutSuite, Prowler, CloudSploit, LocalStack  
**VMs Required:**
- Kali Linux
- LocalStack (AWS simulation)
- Ubuntu Server (cloud simulation)

**Duration:** 2.5 hours  
**RAM:** 10 GB  
**Practice Scenarios:**
- Cloud misconfiguration detection
- S3 bucket enumeration
- IAM policy analysis
- Container security

### Module 20: Cryptography
**Tools:** OpenSSL, John the Ripper, Hashcat, CrypTool  
**VMs Required:**
- Kali Linux
- Windows 10

**Duration:** 2 hours  
**RAM:** 8 GB  
**Practice Scenarios:**
- Hash cracking
- Encryption/decryption
- Digital signatures
- PKI analysis
- SSL/TLS attacks

---

## Malware Analysis Lab - Detailed Setup

### Safety Protocols ⚠️

**CRITICAL RULES:**
1. **Complete network isolation** - No internet, no LAN access
2. **Snapshot before infection** - Always revert after analysis
3. **No production network contact** - Ever
4. **Disable antivirus on victim VMs** - For analysis purposes
5. **Document everything** - Track samples, behaviors, IOCs

### Malware Sample Sources (Legal & Ethical)

**Legitimate repositories:**
- **theZoo** - https://github.com/ytisf/theZoo (10,000+ samples)
- **VirusShare** - https://virusshare.com (free registration)
- **Malware Bazaar** - https://bazaar.abuse.ch (fresh samples)
- **Hybrid Analysis** - https://hybrid-analysis.com (analyzed samples)
- **VirusTotal** - https://virustotal.com (sample downloads)

**Sample categories to practice:**
- Trojans (RATs, backdoors)
- Ransomware (WannaCry, Locky variants)
- Worms (Conficker, Stuxnet)
- Rootkits
- Keyloggers
- Botnets
- Cryptominers

### FlareVM Setup (Windows Malware Analysis)

**Base:** Windows 10 Pro (6 GB RAM, 2 CPU, 80 GB disk)

**Installation:**
```powershell
# Install FlareVM (FireEye's toolkit)
# https://github.com/mandiant/flare-vm

# Disable Windows Defender
Set-MpPreference -DisableRealtimeMonitoring $true

# Install FlareVM
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
Invoke-WebRequest https://raw.githubusercontent.com/mandiant/flare-vm/main/install.ps1 -OutFile install.ps1
Unblock-File .\install.ps1
.\install.ps1
```

**Included tools (150+):**
- Debuggers: x64dbg, OllyDbg, WinDbg
- Disassemblers: IDA Free, Ghidra, Radare2
- Monitors: Process Monitor, Process Explorer, Autoruns
- Network: Wireshark, Fiddler, FakeNet-NG
- Forensics: Volatility, YARA, PE-bear
- Reverse engineering: dnSpy, de4dot, CFF Explorer

### REMnux Setup (Linux Malware Analysis)

**Base:** Ubuntu 20.04 (4 GB RAM, 2 CPU, 60 GB disk)

**Installation:**
```bash
# Install REMnux
wget https://REMnux.org/remnux-cli
chmod +x remnux-cli
sudo ./remnux-cli install
```

**Included tools:**
- Static analysis: strings, file, exiftool, YARA
- Dynamic analysis: strace, ltrace, tcpdump
- Network: Wireshark, NetworkMiner, FakeNet-NG
- Malware unpacking: UPX, upx-ucl
- Forensics: Volatility, bulk_extractor

### Cuckoo Sandbox Setup (Automated Analysis)

**Base:** Ubuntu 20.04 (4 GB RAM, 2 CPU, 60 GB disk)

**Installation:**
```bash
# Install dependencies
sudo apt-get install python3 python3-pip mongodb postgresql

# Install Cuckoo
pip3 install cuckoo

# Initialize Cuckoo
cuckoo init

# Configure analysis VMs
cuckoo machine --add windows10 --platform windows --ip 10.99.1.20
```

**Workflow:**
1. Submit malware sample to Cuckoo
2. Cuckoo automatically spins up victim VM
3. Executes malware in sandbox
4. Captures behavior (processes, network, files, registry)
5. Generates comprehensive report
6. Reverts VM to clean snapshot

### Malware Analysis Workflow

**Example: Analyzing a Trojan**

1. **Preparation:**
   ```bash
   # Take snapshot of clean Windows 10 VM
   qm snapshot 100 clean-state "Clean Windows 10 before infection"
   
   # Start victim VM
   qm start 100
   
   # Start network capture on Kali
   tcpdump -i eth0 -w trojan-capture.pcap
   ```

2. **Static Analysis (REMnux):**
   ```bash
   # File type identification
   file malware.exe
   
   # String extraction
   strings malware.exe | less
   
   # Hash calculation
   md5sum malware.exe
   sha256sum malware.exe
   
   # YARA rule matching
   yara rules.yar malware.exe
   
   # PE analysis
   pefile malware.exe
   ```

3. **Dynamic Analysis (FlareVM):**
   ```powershell
   # Start Process Monitor (filter on malware.exe)
   procmon.exe
   
   # Start Process Explorer
   procexp.exe
   
   # Start Wireshark
   wireshark.exe
   
   # Execute malware
   .\malware.exe
   
   # Observe:
   # - Process creation
   # - File system changes
   # - Registry modifications
   # - Network connections
   ```

4. **Network Analysis:**
   ```bash
   # Analyze captured traffic
   wireshark trojan-capture.pcap
   
   # Extract IOCs
   # - C2 server IPs
   # - Domain names
   # - HTTP requests
   # - DNS queries
   ```

5. **Cleanup:**
   ```bash
   # Revert to clean snapshot
   qm rollback 100 clean-state
   
   # Document findings
   # - Behavior summary
   # - IOCs (IPs, domains, hashes)
   # - Persistence mechanisms
   # - Mitigation recommendations
   ```

### FakeNet-NG Setup (Simulated Internet)

**Purpose:** Tricks malware into thinking it has internet connectivity

**Installation (on FlareVM):**
```powershell
pip install fakenet-ng
```

**Configuration:**
```yaml
# fakenet.conf
[DNS]
Enabled: True
Port: 53
# Resolve all domains to local IP

[HTTP]
Enabled: True
Port: 80
# Respond to all HTTP requests

[HTTPS]
Enabled: True
Port: 443
# Respond to all HTTPS requests
```

**Usage:**
```powershell
# Start FakeNet-NG
fakenet.exe
```

Malware will attempt to connect to C2 servers, but FakeNet-NG intercepts and logs all connections without actually reaching the internet.

---

## Deployment Automation

### Proxmox VM Creation Script

```bash
#!/bin/bash
# deploy-ceh-lab.sh - Automated CEH lab deployment

# Configuration
STORAGE="local-lvm"
BRIDGE="vmbr99"
GATEWAY="10.99.1.1"

# Create Kali Linux VM
qm create 200 \
  --name kali-linux \
  --memory 4096 \
  --cores 2 \
  --net0 virtio,bridge=$BRIDGE \
  --scsi0 $STORAGE:60 \
  --cdrom /var/lib/vz/template/iso/kali-linux-2024.1-installer-amd64.iso \
  --boot order=scsi0

# Create Windows 10 VM
qm create 201 \
  --name windows10-target \
  --memory 4096 \
  --cores 2 \
  --net0 virtio,bridge=$BRIDGE \
  --scsi0 $STORAGE:60 \
  --cdrom /var/lib/vz/template/iso/windows10.iso \
  --boot order=scsi0

# Create Windows Server 2019 VM
qm create 202 \
  --name windows-server-2019 \
  --memory 4096 \
  --cores 2 \
  --net0 virtio,bridge=$BRIDGE \
  --scsi0 $STORAGE:80 \
  --cdrom /var/lib/vz/template/iso/windows-server-2019.iso \
  --boot order=scsi0

# Create Ubuntu Server VM
qm create 203 \
  --name ubuntu-server \
  --memory 2048 \
  --cores 2 \
  --net0 virtio,bridge=$BRIDGE \
  --scsi0 $STORAGE:30 \
  --cdrom /var/lib/vz/template/iso/ubuntu-22.04-server-amd64.iso \
  --boot order=scsi0

# Create Metasploitable 2 VM
qm create 204 \
  --name metasploitable2 \
  --memory 1024 \
  --cores 1 \
  --net0 virtio,bridge=$BRIDGE \
  --scsi0 $STORAGE:8 \
  --cdrom /var/lib/vz/template/iso/metasploitable-linux-2.0.0.zip \
  --boot order=scsi0

# Create DVWA VM (Ubuntu + LAMP + DVWA)
qm create 205 \
  --name dvwa \
  --memory 2048 \
  --cores 1 \
  --net0 virtio,bridge=$BRIDGE \
  --scsi0 $STORAGE:20 \
  --cdrom /var/lib/vz/template/iso/ubuntu-20.04-server-amd64.iso \
  --boot order=scsi0

# Create pfSense VM
qm create 206 \
  --name pfsense \
  --memory 1024 \
  --cores 1 \
  --net0 virtio,bridge=$BRIDGE \
  --scsi0 $STORAGE:10 \
  --cdrom /var/lib/vz/template/iso/pfSense-CE-2.7.0-RELEASE-amd64.iso \
  --boot order=scsi0

echo "CEH Lab VMs created. Configure and start VMs manually."
```

### Snapshot Management Script

```bash
#!/bin/bash
# snapshot-ceh-lab.sh - Create clean snapshots for all CEH VMs

VMS=(200 201 202 203 204 205 206)

for vm in "${VMS[@]}"; do
  echo "Creating snapshot for VM $vm..."
  qm snapshot $vm clean-state "Clean state before exercises"
done

echo "All snapshots created."
```

### Reset Lab Script

```bash
#!/bin/bash
# reset-ceh-lab.sh - Revert all VMs to clean state

VMS=(200 201 202 203 204 205 206)

for vm in "${VMS[@]}"; do
  echo "Reverting VM $vm to clean state..."
  qm rollback $vm clean-state
  qm start $vm
done

echo "Lab reset complete."
```

---

## ISO Downloads Required

### Attack Platforms
- Kali Linux 2024.1 - https://www.kali.org/get-kali/
- Parrot Security OS - https://www.parrotsec.org/download/

### Windows Targets
- Windows 10 Pro - https://www.microsoft.com/software-download/windows10
- Windows 11 Pro - https://www.microsoft.com/software-download/windows11
- Windows Server 2019 - https://www.microsoft.com/evalcenter/
- Windows Server 2022 - https://www.microsoft.com/evalcenter/

**Note:** Use evaluation versions (180-day trial)

### Linux Targets
- Ubuntu 22.04 Server - https://ubuntu.com/download/server
- Ubuntu 20.04 Desktop - https://ubuntu.com/download/desktop
- CentOS 8 Stream - https://www.centos.org/download/
- Metasploitable 2 - https://sourceforge.net/projects/metasploitable/
- Metasploitable 3 - https://github.com/rapid7/metasploitable3

### Specialized VMs
- REMnux - https://remnux.org/
- pfSense - https://www.pfsense.org/download/

### Web Applications (Install on Ubuntu)
- DVWA - https://github.com/digininja/DVWA
- OWASP WebGoat - https://github.com/WebGoat/WebGoat
- OWASP Juice Shop - https://github.com/juice-shop/juice-shop
- bWAPP - http://www.itsecgames.com/
- Mutillidae II - https://github.com/webpwnized/mutillidae

---

## Implementation Timeline

### Week 1: Foundation
- [ ] Create isolated VLAN (vmbr99) on Proxmox
- [ ] Configure firewall rules (block all external access)
- [ ] Download ISOs (Kali, Windows 10, Ubuntu, Metasploitable)
- [ ] Deploy Phase 1 VMs (7 VMs)
- [ ] Configure static IPs
- [ ] Create clean snapshots
- [ ] Test network isolation

**Deliverable:** Working lab for Modules 2-6

### Week 2: Extended Targets
- [ ] Download additional ISOs (Windows Server, CentOS, web apps)
- [ ] Deploy Phase 2 VMs (10 additional VMs)
- [ ] Install web applications (DVWA, WebGoat, Juice Shop)
- [ ] Configure Active Directory on Windows Server
- [ ] Create domain users and policies
- [ ] Test all targets accessible from Kali

**Deliverable:** Working lab for Modules 7-15

### Week 3: Malware Analysis Lab
- [ ] Deploy FlareVM (Windows analysis)
- [ ] Deploy REMnux (Linux analysis)
- [ ] Deploy Cuckoo Sandbox
- [ ] Install FakeNet-NG
- [ ] Download malware samples from theZoo
- [ ] Test malware analysis workflow
- [ ] Verify complete network isolation

**Deliverable:** Working lab for Module 7 (Malware Threats)

### Week 4: Specialized Targets
- [ ] Set up Android emulator
- [ ] Deploy IoT simulator
- [ ] Set up LocalStack (AWS simulation)
- [ ] Configure wireless testing (USB adapter)
- [ ] Test all 20 modules
- [ ] Document any gaps

**Deliverable:** Complete CEH v13 lab environment

---

## Resource Management

### Running VMs by Module

**Not all VMs run simultaneously.** Start only what you need:

**Light modules (8-12 GB RAM):**
- Modules 2, 4, 8, 9, 10, 11, 15, 18, 20
- Run: Kali + 2-3 targets

**Medium modules (14-16 GB RAM):**
- Modules 3, 5, 6, 12, 13, 14
- Run: Kali + 4-5 targets

**Heavy modules (20+ GB RAM):**
- Module 7 (Malware Analysis)
- Run: Kali + FlareVM + REMnux + victim

**Optimization strategies:**
1. Use snapshots - start/stop VMs as needed
2. Run modules in sequence, not parallel
3. Shut down unused VMs
4. Use LXC containers for lightweight targets (Ubuntu, DVWA)
5. Consider running on multiple Proxmox nodes if available

---

## Study Plan

### Exam Preparation Timeline (12 weeks)

**Weeks 1-2:** Lab setup + Modules 1-5  
**Weeks 3-4:** Modules 6-10  
**Weeks 5-6:** Modules 11-15  
**Weeks 7-8:** Modules 16-20  
**Weeks 9-10:** Practice exams + weak areas  
**Weeks 11-12:** Final review + exam scheduling

### Daily Study Routine

**Weekdays (2 hours/day):**
- 30 min: Video lectures (EC-Council course)
- 60 min: Hands-on lab practice
- 30 min: Note-taking + flashcards

**Weekends (4 hours/day):**
- 90 min: Lab exercises
- 90 min: Practice questions
- 60 min: Review + documentation

### Practice Exam Resources

- EC-Council iLearn practice exams (included)
- Boson ExSim-Max (highly recommended)
- PentesterAcademy practice tests
- TryHackMe CEH path
- HackTheBox Academy

---

## Cost Analysis

### Total Cost: $0 (Uses Existing Infrastructure)

**What you already have:**
- Proxmox homelab (16 containers, 12 VMs capacity)
- Network infrastructure
- Storage capacity
- Technical expertise

**What's free:**
- Kali Linux (open source)
- Metasploitable (free)
- Web applications (open source)
- Malware samples (legal repositories)
- FlareVM toolkit (free)
- REMnux (free)

**Optional purchases:**
- Windows licenses - $0 (use evaluation versions, 180-day trial)
- USB WiFi adapter - $30-50 (for Module 16)
- Boson practice exams - $99 (optional but recommended)

**Compared to alternatives:**
- EC-Council iLabs - $449 (6 months access)
- Cybrary labs - $399/year
- PentesterAcademy - $249/year
- Cloud-based labs - $50-100/month

**Savings: $449-1200/year**

---

## Success Metrics

### Lab Readiness Checklist

- [ ] All Phase 1 VMs deployed and accessible
- [ ] Network completely isolated (verified)
- [ ] Clean snapshots created for all VMs
- [ ] Can successfully complete Module 2 exercises
- [ ] Kali Linux has all required tools installed
- [ ] Windows targets have RDP/SMB enabled
- [ ] Linux targets have SSH/FTP enabled
- [ ] Web applications accessible from Kali

### Exam Readiness Checklist

- [ ] Completed all 20 modules
- [ ] Scored 80%+ on practice exams
- [ ] Can perform all attacks from memory
- [ ] Understand theory behind each attack
- [ ] Documented common pitfalls
- [ ] Practiced time management (4 hours for practical)

---

## Next Steps

1. **Review this document** - Ensure understanding of architecture
2. **Check Proxmox resources** - Verify available RAM/CPU/disk
3. **Download ISOs** - Start with Phase 1 (Kali, Windows 10, Ubuntu, Metasploitable)
4. **Create isolated VLAN** - Configure vmbr99 on Proxmox
5. **Deploy first VM** - Start with Kali Linux
6. **Test network isolation** - Verify no internet/LAN access
7. **Begin Module 2** - Footprinting and Reconnaissance

---

## References

- EC-Council CEH v13 Official Curriculum
- Kali Linux Documentation - https://www.kali.org/docs/
- Metasploit Unleashed - https://www.offensive-security.com/metasploit-unleashed/
- OWASP Testing Guide - https://owasp.org/www-project-web-security-testing-guide/
- NIST Cybersecurity Framework - https://www.nist.gov/cyberframework
- MITRE ATT&CK Framework - https://attack.mitre.org/

---

**Status:** Design complete, ready for implementation  
**Next Action:** Create isolated VLAN on Proxmox and deploy Kali Linux VM  
**Estimated Setup Time:** 3-4 weeks (part-time)  
**Estimated Study Time:** 12 weeks to exam readiness
