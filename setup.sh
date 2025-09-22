#!/bin/bash

echo "Setting up YouTube Transcript Fetcher..."

# Install system dependencies
echo "Installing system dependencies..."
sudo apt update
sudo apt install -y python3.12-venv python3-pip

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment and install dependencies
echo "Installing Python dependencies..."
source venv/bin/activate
pip install -r requirements.txt

echo "Setup complete!"
echo ""
echo "To use the script:"
echo "1. Activate the virtual environment: source venv/bin/activate"
echo "2. Run the script: python3 get_transcript.py 'YOUTUBE_URL'"
echo "3. Deactivate when done: deactivate"