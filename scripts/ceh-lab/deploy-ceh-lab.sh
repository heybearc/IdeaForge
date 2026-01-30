#!/bin/bash
# deploy-ceh-lab.sh - Automated CEH v13 Lab Deployment
# 
# Purpose: Deploy Phase 1 CEH lab VMs on Proxmox
# Usage: ./deploy-ceh-lab.sh
# Requirements: Run from Proxmox host or via SSH

set -e

# Configuration
STORAGE="local-lvm"
BRIDGE="vmbr99"
ISO_PATH="/var/lib/vz/template/iso"
START_VMID=200

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}CEH v13 Lab Deployment Script${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""

# Check if running on Proxmox
if ! command -v qm &> /dev/null; then
    echo -e "${RED}Error: qm command not found. Run this script on Proxmox host.${NC}"
    exit 1
fi

# Check if ISOs exist
check_iso() {
    local iso=$1
    if [ ! -f "$ISO_PATH/$iso" ]; then
        echo -e "${YELLOW}Warning: ISO not found: $iso${NC}"
        echo "Download from appropriate source before deploying this VM."
        return 1
    fi
    return 0
}

# Create VM function
create_vm() {
    local vmid=$1
    local name=$2
    local memory=$3
    local cores=$4
    local disk=$5
    local iso=$6
    
    echo -e "${GREEN}Creating VM $vmid: $name${NC}"
    
    # Check if VM already exists
    if qm status $vmid &> /dev/null; then
        echo -e "${YELLOW}VM $vmid already exists. Skipping.${NC}"
        return
    fi
    
    # Check if ISO exists
    if ! check_iso "$iso"; then
        echo -e "${YELLOW}Skipping VM $vmid due to missing ISO.${NC}"
        return
    fi
    
    # Create VM
    qm create $vmid \
        --name "$name" \
        --memory $memory \
        --cores $cores \
        --net0 virtio,bridge=$BRIDGE \
        --scsi0 $STORAGE:$disk \
        --cdrom "$ISO_PATH/$iso" \
        --boot order=scsi0 \
        --ostype l26
    
    echo -e "${GREEN}✓ VM $vmid created successfully${NC}"
    echo ""
}

# Phase 1: Core Lab VMs
echo -e "${GREEN}Phase 1: Deploying Core Lab VMs${NC}"
echo ""

# VM 200: Kali Linux
create_vm 200 "kali-linux" 4096 2 60 "kali-linux-2024.1-installer-amd64.iso"

# VM 201: Windows 10
create_vm 201 "windows10-target" 4096 2 60 "windows10.iso"

# VM 202: Windows Server 2019
create_vm 202 "windows-server-2019" 4096 2 80 "windows-server-2019.iso"

# VM 203: Ubuntu Server
create_vm 203 "ubuntu-server" 2048 2 30 "ubuntu-22.04-server-amd64.iso"

# VM 204: Metasploitable 2
create_vm 204 "metasploitable2" 1024 1 8 "metasploitable-linux-2.0.0.iso"

# VM 205: DVWA (Ubuntu base)
create_vm 205 "dvwa" 2048 1 20 "ubuntu-20.04-server-amd64.iso"

# VM 206: pfSense
create_vm 206 "pfsense" 1024 1 10 "pfSense-CE-2.7.0-RELEASE-amd64.iso"

echo ""
echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}Deployment Summary${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""
echo "VMs created (if ISOs were available):"
echo "  200 - Kali Linux (Attack Platform)"
echo "  201 - Windows 10 (Target)"
echo "  202 - Windows Server 2019 (AD/DC Target)"
echo "  203 - Ubuntu Server (Target)"
echo "  204 - Metasploitable 2 (Vulnerable Target)"
echo "  205 - DVWA (Web App Target)"
echo "  206 - pfSense (Network Firewall)"
echo ""
echo -e "${YELLOW}Next Steps:${NC}"
echo "1. Install operating systems on each VM"
echo "2. Configure static IPs (10.99.1.x range)"
echo "3. Run ./configure-ceh-network.sh to set up networking"
echo "4. Run ./snapshot-ceh-lab.sh to create clean snapshots"
echo "5. Begin Module 2 exercises"
echo ""
echo -e "${GREEN}Deployment complete!${NC}"
