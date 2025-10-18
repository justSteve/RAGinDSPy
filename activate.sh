#!/bin/bash
# Activation script for DSPy RAG Project

# Activate the virtual environment
source venv/bin/activate

# Load environment variables if .env file exists
if [ -f .env ]; then
    echo "Loading environment variables from .env file..."
    export $(grep -v '^#' .env | xargs)
else
    echo "Warning: .env file not found. Please create one based on .env.example"
fi

echo "Virtual environment activated!"
echo "Python path: $(which python)"
echo "Python version: $(python --version)"

# Display helpful information
echo ""
echo "To get started:"
echo "1. Copy .env.example to .env and fill in your API keys"
echo "2. Launch Jupyter: jupyter notebook"
echo "3. Open 1.Getting-Started-with-RAG-in-DSPy.ipynb"
echo ""
echo "To deactivate later, run: deactivate"