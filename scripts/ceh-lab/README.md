# CEH v13 Lab Automation Scripts

Automated deployment and management scripts for CEH v13 lab environment on Proxmox.

## Scripts Overview

### 1. `configure-ceh-network.sh`
**Purpose:** Set up isolated network for CEH lab  
**Run first:** Yes  
**Requirements:** Root access on Proxmox host

**What it does:**
- Creates isolated bridge `vmbr99` (10.99.1.0/24)
- Configures firewall rules to block external access
- Verifies network isolation

**Usage:**
```bash
ssh prox
sudo ./configure-ceh-network.sh
```

### 2. `deploy-ceh-lab.sh`
**Purpose:** Deploy Phase 1 CEH lab VMs  
**Run second:** Yes  
**Requirements:** ISOs downloaded to `/var/lib/vz/template/iso/`

**What it does:**
- Creates 7 VMs (IDs 200-206)
- Configures VM specs (RAM, CPU, disk)
- Attaches ISOs for installation

**Usage:**
```bash
ssh prox
./deploy-ceh-lab.sh
```

**VMs created:**
- 200 - Kali Linux (4GB RAM, 2 CPU, 60GB disk)
- 201 - Windows 10 (4GB RAM, 2 CPU, 60GB disk)
- 202 - Windows Server 2019 (4GB RAM, 2 CPU, 80GB disk)
- 203 - Ubuntu Server (2GB RAM, 2 CPU, 30GB disk)
- 204 - Metasploitable 2 (1GB RAM, 1 CPU, 8GB disk)
- 205 - DVWA (2GB RAM, 1 CPU, 20GB disk)
- 206 - pfSense (1GB RAM, 1 CPU, 10GB disk)

### 3. `snapshot-ceh-lab.sh`
**Purpose:** Create clean snapshots for easy reset  
**Run third:** After OS installation and configuration  
**Requirements:** VMs must be running

**What it does:**
- Creates "clean-state" snapshot for each VM
- Deletes old snapshots if they exist
- Timestamps snapshot creation

**Usage:**
```bash
ssh prox
./snapshot-ceh-lab.sh
```

### 4. `reset-ceh-lab.sh`
**Purpose:** Revert all VMs to clean state  
**Run:** Between exercises or after malware infection  
**Requirements:** Clean snapshots must exist

**What it does:**
- Stops all VMs
- Reverts to "clean-state" snapshot
- Optionally restarts VMs

**Usage:**
```bash
# Reset and restart VMs
ssh prox
./reset-ceh-lab.sh

# Reset but leave VMs stopped
ssh prox
./reset-ceh-lab.sh --no-start
```

## Deployment Workflow

### Initial Setup (One Time)

1. **Download ISOs**
   ```bash
   ssh prox
   cd /var/lib/vz/template/iso/
   
   # Kali Linux
   wget https://cdimage.kali.org/kali-2024.1/kali-linux-2024.1-installer-amd64.iso
   
   # Windows (download from Microsoft)
   # - Windows 10: https://www.microsoft.com/software-download/windows10
   # - Windows Server 2019: https://www.microsoft.com/evalcenter/
   
   # Ubuntu
   wget https://releases.ubuntu.com/22.04/ubuntu-22.04-server-amd64.iso
   wget https://releases.ubuntu.com/20.04/ubuntu-20.04-server-amd64.iso
   
   # Metasploitable 2
   wget https://sourceforge.net/projects/metasploitable/files/Metasploitable2/metasploitable-linux-2.0.0.zip
   unzip metasploitable-linux-2.0.0.zip
   
   # pfSense
   wget https://atxfiles.netgate.com/mirror/downloads/pfSense-CE-2.7.0-RELEASE-amd64.iso.gz
   gunzip pfSense-CE-2.7.0-RELEASE-amd64.iso.gz
   ```

2. **Configure Network**
   ```bash
   ssh prox
   sudo ./configure-ceh-network.sh
   ```

3. **Deploy VMs**
   ```bash
   ssh prox
   ./deploy-ceh-lab.sh
   ```

4. **Install Operating Systems**
   - Access each VM via Proxmox console
   - Install OS with default settings
   - Configure static IP (10.99.1.x)
   - Install SSH/RDP for remote access

5. **Configure VMs**
   
   **Kali Linux (10.99.1.10):**
   ```bash
   # Update system
   sudo apt update && sudo apt upgrade -y
   
   # Install additional tools
   sudo apt install -y metasploit-framework
   
   # Configure static IP
   sudo nano /etc/network/interfaces
   # Add:
   # auto eth0
   # iface eth0 inet static
   #   address 10.99.1.10
   #   netmask 255.255.255.0
   #   gateway 10.99.1.1
   ```
   
   **Windows 10 (10.99.1.20):**
   - Disable Windows Defender (for testing)
   - Enable RDP
   - Configure static IP
   - Create test user accounts
   
   **Windows Server 2019 (10.99.1.22):**
   - Install Active Directory Domain Services
   - Promote to Domain Controller
   - Create domain: `cehlab.local`
   - Create test users and groups
   
   **Ubuntu Server (10.99.1.30):**
   ```bash
   # Install services
   sudo apt install -y openssh-server apache2 mysql-server vsftpd
   
   # Configure static IP
   sudo nano /etc/netplan/00-installer-config.yaml
   ```
   
   **Metasploitable 2 (10.99.1.40):**
   - Default credentials: msfadmin/msfadmin
   - Already configured with vulnerabilities
   - Configure static IP
   
   **DVWA (10.99.1.50):**
   ```bash
   # Install LAMP stack
   sudo apt install -y apache2 mysql-server php php-mysqli php-gd libapache2-mod-php
   
   # Install DVWA
   cd /var/www/html
   sudo git clone https://github.com/digininja/DVWA.git
   sudo chown -R www-data:www-data DVWA
   
   # Configure database
   sudo mysql -e "CREATE DATABASE dvwa;"
   sudo mysql -e "CREATE USER 'dvwa'@'localhost' IDENTIFIED BY 'p@ssw0rd';"
   sudo mysql -e "GRANT ALL ON dvwa.* TO 'dvwa'@'localhost';"
   
   # Configure DVWA
   cd DVWA/config
   sudo cp config.inc.php.dist config.inc.php
   sudo nano config.inc.php
   # Set database credentials
   ```

6. **Create Clean Snapshots**
   ```bash
   ssh prox
   ./snapshot-ceh-lab.sh
   ```

### Daily Usage

**Start lab session:**
```bash
# Start all VMs
ssh prox
for vm in 200 201 202 203 204 205 206; do qm start $vm; done

# Or start specific VMs for a module
qm start 200  # Kali
qm start 201  # Windows 10
qm start 203  # Ubuntu
```

**End lab session:**
```bash
# Reset to clean state
ssh prox
./reset-ceh-lab.sh

# Or just stop VMs without reset
for vm in 200 201 202 203 204 205 206; do qm stop $vm; done
```

**After malware infection:**
```bash
# Immediately reset infected VM
ssh prox
qm stop 201
qm rollback 201 clean-state
qm start 201
```

## VM Management Commands

### Check VM Status
```bash
ssh prox
qm list | grep "20[0-6]"
```

### Start/Stop Individual VM
```bash
ssh prox
qm start 200   # Start Kali
qm stop 200    # Stop Kali
qm shutdown 200  # Graceful shutdown
```

### Access VM Console
```bash
# Via Proxmox web interface
https://your-proxmox-ip:8006

# Or via SSH (if configured)
ssh kali@10.99.1.10
ssh administrator@10.99.1.20
```

### List Snapshots
```bash
ssh prox
qm listsnapshot 200
```

### Create Manual Snapshot
```bash
ssh prox
qm snapshot 200 before-exploit "Before attempting exploit"
```

### Delete Snapshot
```bash
ssh prox
qm delsnapshot 200 snapshot-name
```

## Troubleshooting

### VMs Can't Communicate
```bash
# Check bridge exists
ssh prox
ip link show vmbr99

# Check firewall isn't blocking intra-VLAN traffic
sudo iptables -L FORWARD -n | grep 10.99.1
```

### VMs Have Internet Access (Should Not)
```bash
# Verify firewall rules
ssh prox
sudo iptables -L FORWARD -n

# Re-apply rules
sudo iptables -A FORWARD -s 10.99.1.0/24 -o vmbr0 -j DROP
sudo iptables -A FORWARD -s 10.99.1.0/24 -o eth0 -j DROP
sudo iptables-save > /etc/iptables/rules.v4
```

### Snapshot Creation Fails
```bash
# Ensure VM is running
ssh prox
qm status 200

# Check disk space
df -h

# Check if snapshot already exists
qm listsnapshot 200
```

### VM Won't Start After Rollback
```bash
# Check VM configuration
ssh prox
qm config 200

# Try starting with debug
qm start 200 --debug
```

## Resource Management

### Check Resource Usage
```bash
ssh prox
# Overall system
free -h
df -h

# Per VM
qm status 200 --verbose
```

### Adjust VM Resources
```bash
# Increase RAM
ssh prox
qm set 200 --memory 8192

# Add CPU cores
qm set 200 --cores 4

# Resize disk (requires VM shutdown)
qm stop 200
qm resize 200 scsi0 +20G
qm start 200
```

## Security Notes

⚠️ **CRITICAL SAFETY RULES:**

1. **Network Isolation**
   - CEH lab MUST be on isolated VLAN (10.99.1.0/24)
   - NO internet access
   - NO access to production networks (10.92.x.x)
   - Verify isolation before running exploits

2. **Malware Handling**
   - Only run malware in isolated VMs
   - Always revert to clean snapshot after infection
   - Never transfer files from infected VMs to production
   - Document all malware samples used

3. **Legal Considerations**
   - Only attack VMs you own
   - Never use skills on unauthorized systems
   - CEH certification requires ethical use agreement
   - Keep lab completely isolated

4. **Backup Strategy**
   - Maintain clean snapshots at all times
   - Export VM configurations periodically
   - Document VM setup procedures
   - Test restore procedures

## Next Steps

After completing initial setup:

1. **Test Network Isolation**
   - Verify VMs can ping each other
   - Verify VMs cannot ping internet (8.8.8.8)
   - Verify VMs cannot ping production (10.92.x.x)

2. **Begin Module 2**
   - Start with Footprinting and Reconnaissance
   - Follow exercises in CEH course material
   - Document findings and techniques

3. **Expand Lab**
   - Add Phase 2 VMs as needed
   - Set up malware analysis lab (FlareVM, REMnux)
   - Configure specialized targets (Android, IoT)

## Support

For issues or questions:
- Review main lab document: `ideas/in-progress/2026-01-30-ceh-v13-lab-environment.md`
- Check Proxmox documentation: https://pve.proxmox.com/wiki/
- CEH official resources: https://www.eccouncil.org/train-certify/certified-ethical-hacker-ceh/

---

**Remember:** This lab is for educational purposes only. Always practice ethical hacking principles.
