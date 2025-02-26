#!/bin/bash

# Customizable Nmap Stealth Scanner for Ethical Hacking
# Author: CEH Student

# Default Configurations (Customize as needed)
TARGET="192.168.110.138"  # Change to your target IP/Domain
SCAN_TYPE="-sS"            # Stealthy SYN Scan (Change to -sT for full connect scan)
PORTS="-p- "               # Scan all 65,535 ports (Modify as needed, e.g., -p 80,443)
TIMING="-T2"               # Timing Template (T0-T5; lower = stealthier)
DECOY="-D RND:10"          # Use 10 random decoy IPs
FRAGMENT="-f"              # Enable packet fragmentation
DATA_LENGTH="--data-length 16"  # Random payload to avoid signature detection
OS_DETECTION="-A"          # Enable OS, service, and script detection
OUTPUT="-oN scan_results.txt"  # Save output to a file
EXTRA_OPTS="--open"        # Show only open ports

# User Input for Customization
echo "Enter target (IP/Domain): "
read -r TARGET
echo "Enter scan type (-sS for stealth, -sT for full, etc.): "
read -r SCAN_TYPE
echo "Enter ports to scan (-p- for all, -p 22,80,443 for specific): "
read -r PORTS
echo "Enter timing template (T0-T5, default T2): "
read -r TIMING
echo "Use decoys? (y/n): "
read -r USE_DECOY

if [[ $USE_DECOY == "y" ]]; then
    echo "How many decoys? (Default 10): "
    read -r DECOY_COUNT
    DECOY="-D RND:$DECOY_COUNT"
else
    DECOY=""
fi

# Construct Nmap Command
NMAP_CMD="nmap $SCAN_TYPE -Pn $PORTS $TIMING $DECOY $FRAGMENT $DATA_LENGTH $OS_DETECTION $EXTRA_OPTS $OUTPUT $TARGET"

# Display and Execute
echo "Running: $NMAP_CMD"
eval $NMAP_CMD
