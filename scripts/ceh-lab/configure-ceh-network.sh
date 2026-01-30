#!/bin/bash
# configure-ceh-network.sh - Configure isolated CEH lab network
#
# Purpose: Set up isolated VLAN for CEH lab on Proxmox
# Usage: ./configure-ceh-network.sh
# Requirements: Run on Proxmox host with root privileges

set -e

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}CEH Lab Network Configuration${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""

# Check if running as root
if [ "$EUID" -ne 0 ]; then
    echo -e "${RED}Error: This script must be run as root${NC}"
    exit 1
fi

# Check if running on Proxmox
if ! command -v qm &> /dev/null; then
    echo -e "${RED}Error: qm command not found. Run this script on Proxmox host.${NC}"
    exit 1
fi

echo -e "${YELLOW}This script will:${NC}"
echo "1. Create isolated bridge vmbr99 (10.99.1.0/24)"
echo "2. Configure firewall rules to block external access"
echo "3. Verify network isolation"
echo ""
read -p "Continue? (y/N): " -n 1 -r
echo ""
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Aborted."
    exit 0
fi

echo ""

# Step 1: Create bridge
echo -e "${GREEN}Step 1: Creating isolated bridge vmbr99${NC}"

# Check if bridge already exists
if ip link show vmbr99 &> /dev/null; then
    echo -e "${YELLOW}Bridge vmbr99 already exists. Skipping creation.${NC}"
else
    # Add bridge configuration to /etc/network/interfaces
    cat >> /etc/network/interfaces << EOF

# CEH Lab Isolated Network
auto vmbr99
iface vmbr99 inet static
    address 10.99.1.1
    netmask 255.255.255.0
    bridge_ports none
    bridge_stp off
    bridge_fd 0
    # NO gateway = no internet access
    # NO routing = no LAN access
EOF

    # Bring up the bridge
    ifup vmbr99
    echo -e "${GREEN}✓ Bridge vmbr99 created${NC}"
fi

echo ""

# Step 2: Configure firewall rules
echo -e "${GREEN}Step 2: Configuring firewall rules${NC}"

# Block CEH VLAN from production networks
iptables -A FORWARD -s 10.99.1.0/24 -d 10.92.0.0/16 -j DROP
iptables -A FORWARD -s 10.99.1.0/24 -o vmbr0 -j DROP

# Block CEH VLAN from internet
iptables -A FORWARD -s 10.99.1.0/24 -o eth0 -j DROP

# Save iptables rules
iptables-save > /etc/iptables/rules.v4

echo -e "${GREEN}✓ Firewall rules configured${NC}"
echo ""

# Step 3: Verify isolation
echo -e "${GREEN}Step 3: Verifying network isolation${NC}"

# Check bridge exists
if ip link show vmbr99 &> /dev/null; then
    echo -e "${GREEN}✓ Bridge vmbr99 exists${NC}"
else
    echo -e "${RED}✗ Bridge vmbr99 not found${NC}"
fi

# Check IP address
if ip addr show vmbr99 | grep -q "10.99.1.1"; then
    echo -e "${GREEN}✓ Bridge has correct IP (10.99.1.1)${NC}"
else
    echo -e "${RED}✗ Bridge IP incorrect${NC}"
fi

# Check firewall rules
if iptables -L FORWARD -n | grep -q "10.99.1.0/24"; then
    echo -e "${GREEN}✓ Firewall rules active${NC}"
else
    echo -e "${YELLOW}⚠ Firewall rules may not be active${NC}"
fi

echo ""
echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}Network Configuration Complete${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""
echo "CEH Lab Network Details:"
echo "  Bridge: vmbr99"
echo "  Network: 10.99.1.0/24"
echo "  Gateway: 10.99.1.1 (Proxmox host)"
echo "  Isolation: Complete (no internet, no LAN access)"
echo ""
echo -e "${YELLOW}VM IP Assignments:${NC}"
echo "  10.99.1.10 - Kali Linux (Attack)"
echo "  10.99.1.20 - Windows 10 (Target)"
echo "  10.99.1.22 - Windows Server 2019 (Target)"
echo "  10.99.1.30 - Ubuntu Server (Target)"
echo "  10.99.1.40 - Metasploitable 2 (Target)"
echo "  10.99.1.50 - DVWA (Web App)"
echo ""
echo -e "${YELLOW}Next Steps:${NC}"
echo "1. Configure static IPs on each VM"
echo "2. Test connectivity between VMs (ping 10.99.1.x)"
echo "3. Verify no internet access (ping 8.8.8.8 should fail)"
echo "4. Create clean snapshots (./snapshot-ceh-lab.sh)"
echo ""
echo -e "${GREEN}Network setup complete!${NC}"
