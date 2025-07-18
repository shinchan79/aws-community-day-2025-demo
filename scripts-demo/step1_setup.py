# step1_setup.py - Setup and validate Bedrock connection
import boto3
import json
import os
from colorama import Fore, Style, init
from dotenv import load_dotenv

init()
load_dotenv()

def main():
    print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}STEP 1: SETUP & CONNECTION VALIDATION{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}")
    
    # Get configuration
    region = os.getenv('AWS_REGION', 'ap-southeast-1')
    model_id = os.getenv('MODEL_ID', 'apac.amazon.nova-lite-v1:0')
    
    print(f"\nConfiguration:")
    print(f"  Region: {region}")
    print(f"  Model: {model_id}")
    
    # Initialize clients
    try:
        bedrock_client = boto3.client('bedrock', region_name=region)
        bedrock_runtime = boto3.client('bedrock-runtime', region_name=region)
        print(f"{Fore.GREEN}✓ AWS clients initialized{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}✗ Failed to initialize AWS clients: {e}{Style.RESET_ALL}")
        return False
    
    # Test model access
    print(f"\nTesting Amazon Nova Lite access...")
    try:
        test_request = {
            "messages": [{"role": "user", "content": [{"text": "Hello"}]}],
            "inferenceConfig": {"maxTokens": 10}
        }
        
        response = bedrock_runtime.invoke_model(
            modelId=model_id,
            body=json.dumps(test_request),
            contentType='application/json'
        )
        
        print(f"{Fore.GREEN}✓ Model access validated{Style.RESET_ALL}")
        
    except Exception as e:
        print(f"{Fore.RED}✗ Model access failed: {e}{Style.RESET_ALL}")
        
        if "inference profile" in str(e).lower():
            print(f"\n{Fore.YELLOW}Troubleshooting:{Style.RESET_ALL}")
            print("• Ensure you're in a supported APAC region")
            print("• Check Amazon Nova Lite access permissions")
            print("• Verify inference profile availability")
            
            print(f"\n{Fore.BLUE}Supported regions:{Style.RESET_ALL}")
            regions = ['ap-northeast-1', 'ap-northeast-2', 'ap-southeast-1', 'ap-southeast-2']
            for r in regions:
                status = "✓ (current)" if r == region else "○"
                print(f"  {status} {r}")
        
        return False
    
    print(f"\n{Fore.GREEN}{'='*70}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}STEP 1 COMPLETE - Ready for Guardrails demo!{Style.RESET_ALL}")
    print(f"{Fore.GREEN}{'='*70}{Style.RESET_ALL}")
    print(f"\nNext: Run step2_create_guardrail.py")
    
    return True

if __name__ == "__main__":
    main()