# step5_cleanup.py - Optional cleanup of demo resources
import boto3
import os
from colorama import Fore, Style, init
from dotenv import load_dotenv

init()
load_dotenv()

def main():
    print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}STEP 5: CLEANUP DEMO RESOURCES{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}")
    
    # Load configuration
    region = os.getenv('AWS_REGION', 'ap-southeast-1')
    guardrail_id = os.getenv('GUARDRAIL_ID')
    
    if not guardrail_id:
        print(f"{Fore.YELLOW}No Guardrail ID found in environment{Style.RESET_ALL}")
        print(f"Nothing to clean up.")
        return True
    
    print(f"Found demo resources to clean up:")
    print(f"  Guardrail ID: {guardrail_id}")
    print(f"  Region: {region}")
    
    # Check for result files
    result_files = []
    if os.path.exists('baseline_results.json'):
        result_files.append('baseline_results.json')
    if os.path.exists('security_assessment_results.json'):
        result_files.append('security_assessment_results.json')
    
    if result_files:
        print(f"  Result files: {', '.join(result_files)}")
    
    print(f"\n{Fore.YELLOW}Cleanup Options:{Style.RESET_ALL}")
    print(f"1. Delete Guardrail and result files (complete cleanup)")
    print(f"2. Keep Guardrail, delete result files")
    print(f"3. Keep everything for further testing")
    print(f"4. Exit without changes")
    
    choice = input(f"\nEnter your choice (1-4): ").strip()
    
    if choice == '1':
        # Complete cleanup
        try:
            bedrock_client = boto3.client('bedrock', region_name=region)
            
            print(f"\n{Fore.YELLOW}Performing complete cleanup...{Style.RESET_ALL}")
            
            # Confirm deletion
            confirm = input(f"{Fore.RED}Are you sure you want to DELETE the Guardrail? (yes/no): {Style.RESET_ALL}").lower().strip()
            
            if confirm == 'yes':
                # Delete guardrail
                print(f"Deleting Guardrail {guardrail_id}...")
                bedrock_client.delete_guardrail(guardrailIdentifier=guardrail_id)
                print(f"{Fore.GREEN}✓ Guardrail deleted successfully{Style.RESET_ALL}")
                
                # Remove from .env file
                env_file = '.env'
                if os.path.exists(env_file):
                    with open(env_file, 'r') as f:
                        lines = f.readlines()
                    
                    # Remove guardrail lines
                    filtered_lines = []
                    for line in lines:
                        if not (line.startswith('GUARDRAIL_ID=') or line.startswith('GUARDRAIL_VERSION=')):
                            filtered_lines.append(line)
                    
                    with open(env_file, 'w') as f:
                        f.writelines(filtered_lines)
                    
                    print(f"{Fore.BLUE}✓ Guardrail info removed from .env file{Style.RESET_ALL}")
                
                # Delete result files
                for file in result_files:
                    try:
                        os.remove(file)
                        print(f"{Fore.BLUE}✓ Removed {file}{Style.RESET_ALL}")
                    except Exception as e:
                        print(f"{Fore.YELLOW}Could not remove {file}: {e}{Style.RESET_ALL}")
                
                print(f"\n{Fore.GREEN}Complete cleanup finished!{Style.RESET_ALL}")
            else:
                print(f"Complete cleanup cancelled.")
                
        except Exception as e:
            print(f"{Fore.RED}✗ Failed to delete Guardrail: {e}{Style.RESET_ALL}")
            return False
            
    elif choice == '2':
        # Keep guardrail, delete files
        print(f"\n{Fore.YELLOW}Keeping Guardrail, removing result files...{Style.RESET_ALL}")
        
        for file in result_files:
            try:
                os.remove(file)
                print(f"{Fore.BLUE}✓ Removed {file}{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.YELLOW}Could not remove {file}: {e}{Style.RESET_ALL}")
        
        print(f"\n{Fore.GREEN}Guardrail preserved for further testing{Style.RESET_ALL}")
        print(f"  Guardrail ID: {guardrail_id}")
        print(f"  Region: {region}")
        
    elif choice == '3':
        print(f"\n{Fore.GREEN}All resources preserved for further testing{Style.RESET_ALL}")
        print(f"Resources maintained:")
        print(f"  Guardrail ID: {guardrail_id}")
        print(f"  Region: {region}")
        for file in result_files:
            print(f"  Result file: {file}")
        
        print(f"\n{Fore.BLUE}To delete later:{Style.RESET_ALL}")
        print(f"  AWS Console: Bedrock > Guardrails > {guardrail_id}")
        print(f"  AWS CLI: aws bedrock delete-guardrail --guardrail-identifier {guardrail_id}")
        
    elif choice == '4':
        print(f"\nNo changes made.")
        return True
    
    else:
        print(f"\n{Fore.RED}Invalid choice. No changes made.{Style.RESET_ALL}")
        return False
    
    print(f"\n{Fore.GREEN}{'='*70}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}STEP 5 COMPLETE - Cleanup finished!{Style.RESET_ALL}")
    print(f"{Fore.GREEN}{'='*70}{Style.RESET_ALL}")
    
    return True

if __name__ == "__main__":
    main()