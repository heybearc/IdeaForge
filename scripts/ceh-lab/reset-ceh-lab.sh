#!/bin/bash
# reset-ceh-lab.sh - Revert all CEH lab VMs to clean state
#
# Purpose: Quickly reset lab to clean snapshots between exercises
# Usage: ./reset-ceh-lab.sh [--no-start]
# Requirements: Run from Proxmox host or via SSH

set -e

# Configuration
VMS=(200 201 202 203 204 205 206)
SNAPSHOT_NAME="clean-state"
START_VMS=true

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# Parse arguments
if [ "$1" == "--no-start" ]; then
    START_VMS=false
fi

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}CEH Lab Reset${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""

# Check if running on Proxmox
if ! command -v qm &> /dev/null; then
    echo -e "${RED}Error: qm command not found. Run this script on Proxmox host.${NC}"
    exit 1
fi

# Warning
echo -e "${YELLOW}WARNING: This will revert all VMs to clean state.${NC}"
echo -e "${YELLOW}Any unsaved work will be lost.${NC}"
echo ""
read -p "Continue? (y/N): " -n 1 -r
echo ""
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Aborted."
    exit 0
fi

echo ""

# Reset VMs
for vm in "${VMS[@]}"; do
    # Check if VM exists
    if ! qm status $vm &> /dev/null; then
        echo -e "${YELLOW}VM $vm does not exist. Skipping.${NC}"
        continue
    fi
    
    # Check if snapshot exists
    if ! qm listsnapshot $vm | grep -q "$SNAPSHOT_NAME"; then
        echo -e "${YELLOW}VM $vm has no '$SNAPSHOT_NAME' snapshot. Skipping.${NC}"
        continue
    fi
    
    echo -e "${GREEN}Resetting VM $vm...${NC}"
    
    # Stop VM if running
    STATUS=$(qm status $vm | awk '{print $2}')
    if [ "$STATUS" == "running" ]; then
        echo "  Stopping VM..."
        qm stop $vm
        sleep 2
    fi
    
    # Rollback to snapshot
    echo "  Rolling back to clean state..."
    qm rollback $vm "$SNAPSHOT_NAME"
    
    # Start VM if requested
    if [ "$START_VMS" = true ]; then
        echo "  Starting VM..."
        qm start $vm
    fi
    
    echo -e "${GREEN}✓ VM $vm reset complete${NC}"
    echo ""
done

echo ""
echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}Reset Summary${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""
echo "All VMs reverted to clean state."
if [ "$START_VMS" = true ]; then
    echo "VMs are starting up..."
else
    echo "VMs are stopped. Start manually when ready."
fi
echo ""
echo -e "${GREEN}Lab reset complete!${NC}"
