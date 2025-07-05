#!/bin/bash

echo "Setting up Amazon Bedrock Guardrails Demo Environment"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is required but not installed."
    exit 1
fi

# Check if AWS CLI is configured
if ! aws sts get-caller-identity &> /dev/null; then
    echo "Error: AWS CLI is not configured. Please run 'aws configure' first."
    exit 1
fi

# Install Python dependencies
echo "Installing Python dependencies..."
pip3 install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "Creating .env file..."
    echo "AWS_REGION=us-east-1" > .env
    echo "MODEL_ID=anthropic.claude-sonnet-4-20250514-v1:0" >> .env
fi

# Check Bedrock model access
echo "Checking Bedrock model access..."
python3 -c "
import boto3
try:
    client = boto3.client('bedrock', region_name='us-east-1')
    models = client.list_foundation_models()
    print('✓ Bedrock access confirmed')
except Exception as e:
    print(f'✗ Bedrock access failed: {e}')
"

echo "Setup complete! Run 'python3 bedrock_guardrails_demo.py' to start the demo."