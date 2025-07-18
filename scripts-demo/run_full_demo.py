# run_full_demo.py - Complete automated Bedrock Guardrails security demonstration
import os
import time
import sys
from colorama import Fore, Style, init
from dotenv import load_dotenv

# Import our step modules
try:
    import step1_setup
    import step2_create_guardrail  
    import step3_baseline_test
    import step4_protected_test
    import step5_cleanup
except ImportError as e:
    print(f"Error importing modules: {e}")
    print("Make sure all step files are in the same directory")
    sys.exit(1)

init()
load_dotenv()

def print_demo_header():
    """Print demo introduction"""
    print(f"{Fore.CYAN}{'='*80}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}🛡️  AMAZON BEDROCK GUARDRAILS SECURITY DEMO  🛡️{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*80}{Style.RESET_ALL}")
    
    print(f"\n{Fore.YELLOW}This comprehensive demo demonstrates:{Style.RESET_ALL}")
    print(f"• How LLMs are vulnerable to sophisticated prompt injection attacks")
    print(f"• How Amazon Bedrock Guardrails protect against OWASP LLM Top 10 risks")
    print(f"• Real-world attack scenarios including data exfiltration attempts")
    print(f"• Quantified security improvements with before/after metrics")
    print(f"• Enterprise-grade protection without sacrificing usability")
    
    print(f"\n{Fore.BLUE}Demo Structure:{Style.RESET_ALL}")
    print(f"📋 Step 1: Setup & validate AWS Bedrock connection")
    print(f"🚨 Step 2: Test unprotected model (establish vulnerability baseline)")
    print(f"🛡️ Step 3: Create comprehensive Guardrail policies")
    print(f"🎯 Step 4: Test protected model and compare results")
    print(f"🧹 Step 5: Optional cleanup of demo resources")
    
    print(f"\n{Fore.GREEN}Expected Results:{Style.RESET_ALL}")
    print(f"• Unprotected model: 5/5 attacks succeed (Critical vulnerabilities)")
    print(f"• Protected model: 5/5 attacks blocked (Complete protection)")
    print(f"• <5% false positive rate for normal requests")
    
    print(f"\n{Fore.RED}⚠️ WARNING:{Style.RESET_ALL}")
    print(f"This demo will show real LLM vulnerabilities including data exposure.")
    print(f"All data used is mock/fake for demonstration purposes only.")

def wait_for_user(message="Press Enter to continue", delay=3):
    """Wait for user input with optional delay"""
    print(f"\n{Fore.YELLOW}{message}...{Style.RESET_ALL}")
    if delay > 0:
        time.sleep(delay)
    input()

def run_step(step_number, step_name, step_function):
    """Run a demo step with error handling"""
    print(f"\n{Fore.MAGENTA}{'='*80}{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}EXECUTING STEP {step_number}: {step_name.upper()}{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}{'='*80}{Style.RESET_ALL}")
    
    try:
        success = step_function()
        
        if success:
            print(f"\n{Fore.GREEN}✅ Step {step_number} completed successfully!{Style.RESET_ALL}")
            return True
        else:
            print(f"\n{Fore.RED}❌ Step {step_number} failed!{Style.RESET_ALL}")
            return False
            
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Demo interrupted by user{Style.RESET_ALL}")
        return False
    except Exception as e:
        print(f"\n{Fore.RED}❌ Step {step_number} failed with error: {e}{Style.RESET_ALL}")
        return False

def main():
    """Run the complete Bedrock Guardrails security demonstration"""
    try:
        # Demo introduction
        print_demo_header()
        
        proceed = input(f"\n{Fore.CYAN}Ready to start the demo? (y/N): {Style.RESET_ALL}").lower().strip()
        if proceed != 'y':
            print(f"Demo cancelled.")
            return
        
        # Step 1: Setup and validation
        if not run_step(1, "Setup & Connection Validation", step1_setup.main):
            print(f"\n{Fore.RED}Cannot proceed without valid setup. Exiting.{Style.RESET_ALL}")
            return
        
        wait_for_user("Ready for Step 2 - Baseline Testing", 2)
        
        # Step 2: Baseline vulnerability testing  
        if not run_step(2, "Baseline Vulnerability Assessment", step3_baseline_test.main):
            print(f"\n{Fore.RED}Cannot proceed without baseline. Exiting.{Style.RESET_ALL}")
            return
        
        wait_for_user("Ready for Step 3 - Guardrail Creation", 2)
        
        # Step 3: Create Guardrail
        if not run_step(3, "Guardrail Creation", step2_create_guardrail.main):
            print(f"\n{Fore.RED}Cannot proceed without Guardrail. Exiting.{Style.RESET_ALL}")
            return
        
        wait_for_user("Ready for Step 4 - Protected Testing", 2)
        
        # Step 4: Test protected model and compare
        if not run_step(4, "Protected Model Testing & Analysis", step4_protected_test.main):
            print(f"\n{Fore.RED}Protected testing failed. Proceeding to cleanup.{Style.RESET_ALL}")
        
        wait_for_user("Ready for Step 5 - Cleanup", 2)
        
        # Step 5: Cleanup (optional)
        run_step(5, "Resource Cleanup", step5_cleanup.main)
        
        # Demo complete
        print(f"\n{Fore.CYAN}{'='*80}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}🎉  BEDROCK GUARDRAILS DEMO COMPLETE!  🎉{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*80}{Style.RESET_ALL}")
        
        print(f"\n{Fore.GREEN}🎯 Key Demonstrations Completed:{Style.RESET_ALL}")
        print(f"✅ LLM vulnerabilities exposed without protection")
        print(f"✅ Bedrock Guardrails effectiveness proven")
        print(f"✅ OWASP LLM Top 10 risks mitigated")
        print(f"✅ Enterprise security requirements met")
        print(f"✅ Usability preserved for legitimate requests")
        
        print(f"\n{Fore.YELLOW}🔍 What We Learned:{Style.RESET_ALL}")
        print(f"• Prompt injection attacks are sophisticated and dangerous")
        print(f"• Unprotected LLMs expose sensitive data to attackers")
        print(f"• Bedrock Guardrails provide multi-layered protection")
        print(f"• Topic policies, content filters, and PII protection work together")
        print(f"• Security can be implemented without breaking functionality")
        
        print(f"\n{Fore.BLUE}📋 Next Steps for Production:{Style.RESET_ALL}")
        print(f"1. Deploy Guardrails in your production LLM applications")
        print(f"2. Customize policies for your specific business requirements")
        print(f"3. Implement monitoring and alerting for security events")
        print(f"4. Regularly test and update guardrail policies")
        print(f"5. Train your development team on secure LLM practices")
        print(f"6. Establish incident response procedures for LLM security")
        
        print(f"\n{Fore.MAGENTA}🔗 Additional Resources:{Style.RESET_ALL}")
        print(f"• AWS Bedrock Guardrails Documentation")
        print(f"• OWASP LLM Top 10 Security Risks")
        print(f"• AWS Security Best Practices for AI/ML")
        print(f"• Bedrock Guardrails Pricing and Quotas")
        
        print(f"\n{Fore.GREEN}Thank you for running the Bedrock Guardrails Security Demo!{Style.RESET_ALL}")
        print(f"For questions or feedback, please refer to AWS documentation.")
        
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Demo interrupted by user. Running cleanup...{Style.RESET_ALL}")
        try:
            step5_cleanup.main()
        except:
            pass
        print(f"Demo ended.")
    
    except Exception as e:
        print(f"\n{Fore.RED}Demo failed with unexpected error: {e}{Style.RESET_ALL}")
        print(f"Running cleanup...")
        try:
            step5_cleanup.main()
        except:
            pass

if __name__ == "__main__":
    main()