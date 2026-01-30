#!/bin/bash
# snapshot-ceh-lab.sh - Create clean snapshots for all CEH lab VMs
#
# Purpose: Create "clean-state" snapshots for easy lab reset
# Usage: ./snapshot-ceh-lab.sh
# Requirements: Run from Proxmox host or via SSH

set -e

# Configuration
VMS=(200 201 202 203 204 205 206)
SNAPSHOT_NAME="clean-state"
DESCRIPTION="Clean state before exercises - $(date '+%Y-%m-%d %H:%M:%S')"

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}CEH Lab Snapshot Creation${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""

# Check if running on Proxmox
if ! command -v qm &> /dev/null; then
    echo -e "${RED}Error: qm command not found. Run this script on Proxmox host.${NC}"
    exit 1
fi

# Create snapshots
for vm in "${VMS[@]}"; do
    # Check if VM exists
    if ! qm status $vm &> /dev/null; then
        echo -e "${YELLOW}VM $vm does not exist. Skipping.${NC}"
        continue
    fi
    
    # Check if VM is running
    STATUS=$(qm status $vm | awk '{print $2}')
    if [ "$STATUS" != "running" ]; then
        echo -e "${YELLOW}VM $vm is not running. Start it first to create snapshot.${NC}"
        continue
    fi
    
    echo -e "${GREEN}Creating snapshot for VM $vm...${NC}"
    
    # Delete old snapshot if exists
    if qm listsnapshot $vm | grep -q "$SNAPSHOT_NAME"; then
        echo "  Deleting old snapshot..."
        qm delsnapshot $vm "$SNAPSHOT_NAME"
    fi
    
    # Create new snapshot
    qm snapshot $vm "$SNAPSHOT_NAME" --description "$DESCRIPTION"
    echo -e "${GREEN}✓ Snapshot created for VM $vm${NC}"
    echo ""
done

echo ""
echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}Snapshot Summary${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""
echo "Snapshots created for all running VMs."
echo "Snapshot name: $SNAPSHOT_NAME"
echo ""
echo -e "${YELLOW}To revert to clean state:${NC}"
echo "  ./reset-ceh-lab.sh"
echo ""
echo -e "${YELLOW}To revert a single VM:${NC}"
echo "  qm rollback <vmid> $SNAPSHOT_NAME"
echo ""
echo -e "${GREEN}Snapshot creation complete!${NC}"
