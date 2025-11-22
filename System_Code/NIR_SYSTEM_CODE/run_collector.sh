#!/bin/bash

echo "Starting data logger..."
nohup python3 "coordinated_script_cptsc.py" > "output_logs.txt" 2>&1 &

echo "Script started in background. Logging to: output_logs.txt"
echo "Use 'tail -f output_logs.txt' to view logs."