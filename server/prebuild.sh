#!/bin/bash
# Pre-deployment script for Render
# This script runs before the main build

echo "🔧 Starting pre-build setup..."

# Check Python version
python --version

# Upgrade pip
echo "📦 Upgrading pip..."
pip install --upgrade pip

echo "✅ Pre-build setup complete!"
