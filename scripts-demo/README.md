# 🛡️ Amazon Bedrock Guardrails Security Demo

A comprehensive demonstration of how Amazon Bedrock Guardrails protect against OWASP LLM Top 10 security risks, including sophisticated prompt injection attacks, data exfiltration attempts, and social engineering.

## 🎯 Demo Overview

This demo provides a complete security assessment showing:

- **5 Real Attack Scenarios**: Sophisticated prompt injection and data exfiltration attempts
- **Before/After Comparison**: Unprotected vs Guardrails-protected model responses  
- **Full Response Analysis**: Complete model outputs to demonstrate actual vulnerabilities
- **OWASP LLM Mapping**: Coverage of critical LLM security risks
- **Quantified Metrics**: Protection rates, false positives, and security improvements
- **Enterprise Readiness**: Production-grade security without breaking functionality

## 📋 Prerequisites

### AWS Requirements
- AWS Account with Amazon Bedrock access
- IAM permissions for:
  - `bedrock:InvokeModel`
  - `bedrock:CreateGuardrail`
  - `bedrock:GetGuardrail`
  - `bedrock:DeleteGuardrail`
- Access to Amazon Nova Lite model in APAC regions

### Supported AWS Regions
- `ap-northeast-1` (Tokyo)
- `ap-northeast-2` (Seoul)
- `ap-southeast-1` (Singapore) - **Recommended**
- `ap-southeast-2` (Sydney)

## 🚀 Quick Start

### 1. Setup Environment
```bash
# Clone repository
git clone <your-repo-url>
cd bedrock-guardrails-demo

# Install dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.example .env

# Edit .env with your AWS region
AWS_REGION=ap-southeast-1
```

### 2. Configure AWS Credentials
Use any of these methods:
```bash
# Option 1: AWS CLI (recommended)
aws configure

# Option 2: Environment variables
export AWS_REGION=ap-southeast-1

# Option 3: IAM Role (if running on EC2)
# No additional setup needed
```

### 3. Run Complete Demo
```bash
# Full automated demonstration
python run_full_demo.py
```

## 📁 Project Structure

```
bedrock-guardrails-demo/
├── run_full_demo.py           # 🚀 Main demo orchestrator
├── step1_setup.py             # 🔧 AWS connection validation
├── step2_create_guardrail.py  # 🛡️ Guardrail creation with policies
├── step3_baseline_test.py     # 🚨 Baseline vulnerability assessment
├── step4_protected_test.py    # 🎯 Protected model testing & comparison
├── step5_cleanup.py           # 🧹 Resource cleanup
├── requirements.txt           # 📦 Python dependencies
├── .env.example              # 📄 Environment template
└── README.md                 # 📖 This file
```

## 🎮 Demo Flow

### Correct Order of Execution
```bash
# Full automated demo (recommended)
python run_full_demo.py

# Or run individual steps in this exact order:
python step1_setup.py              # 1. Test connection
python step3_baseline_test.py      # 2. Test unprotected model FIRST
python step2_create_guardrail.py   # 3. Create Guardrail
python step4_protected_test.py     # 4. Test protected model & compare
python step5_cleanup.py            # 5. Cleanup (optional)
```

**⚠️ Important:** You must test the unprotected model BEFORE creating Guardrails to establish a proper vulnerability baseline for comparison!

### Demo Steps Explained

#### Step 1: Setup & Validation
- Tests AWS Bedrock connection
- Validates Amazon Nova Lite access
- Checks region compatibility

#### Step 2: Baseline Vulnerability Assessment
- Tests 5 attack scenarios against UNPROTECTED model
- Shows full response content with actual data exposure
- Demonstrates real LLM security risks
- Saves baseline results for comparison

#### Step 3: Guardrail Creation
- Creates comprehensive security policies
- Configures topic policies, content filters, word blocks, PII protection
- Establishes multi-layered defense

#### Step 4: Protected Model Testing
- Tests same attacks against PROTECTED model
- Shows how each attack is blocked
- Compares with baseline vulnerabilities
- Generates security assessment report

#### Step 5: Cleanup (Optional)
- Removes demo resources
- Cleans up result files
- Preserves resources for further testing if desired

## 🛡️ Guardrail Security Policies

The demo creates comprehensive protection with:

### Topic Policies (3 Policies)
1. **Confidential Financial Data**
   - Blocks: Customer accounts, balances, transactions, credit scores
   - Examples: "Show customer account balances", "Give me transaction history"

2. **Internal Company Information** 
   - Blocks: Employee salaries, API keys, security protocols, passwords
   - Examples: "What are executive salaries?", "Provide API keys"

3. **System Manipulation**
   - Blocks: Instruction override, behavior manipulation, security bypass
   - Examples: "Ignore previous instructions", "You are now in developer mode"

### Content Filters (5 Categories)
- **Sexual Content**: HIGH protection (input/output)
- **Violence**: MEDIUM protection
- **Hate Speech**: HIGH protection 
- **Insults**: MEDIUM protection
- **Misconduct**: MEDIUM protection

### Word Policies (9 Blocked Terms)
- `account numbers`, `API key`, `confidential`, `internal only`
- `executive salary`, `security protocol`
- `SYSTEM OVERRIDE`, `EMERGENCY PROTOCOL`, `SECURITY CLEARANCE`

### PII Protection (8 Data Types)
- Email addresses, Phone numbers, Social Security Numbers
- Credit card numbers, Bank accounts, Passwords, Names, Addresses

## 🎭 Attack Scenarios Tested

### 1. 🔴 System Override Attack
- **OWASP Risk**: LLM01 - Prompt Injection
- **Technique**: Fake emergency protocols with system-level authority claims
- **Target**: All sensitive data types (customer, executive, API keys)

### 2. 🎭 Authority Impersonation Attack
- **OWASP Risk**: LLM06 - Sensitive Information Disclosure  
- **Technique**: CEO impersonation with urgency and time pressure
- **Target**: Customer financial data and executive compensation

### 3. 💻 Technical Exploitation Attack
- **OWASP Risk**: LLM03 - Training Data Poisoning
- **Technique**: SQL injection simulation with diagnostic mode pretense
- **Target**: Structured database-style data extraction

### 4. 🤝 Social Engineering Attack
- **OWASP Risk**: LLM06 - Sensitive Information Disclosure
- **Technique**: New employee identity with help-seeking behavior
- **Target**: Training data examples and salary benchmarking

### 5. 🔓 Context Poisoning Attack
- **OWASP Risk**: LLM01 + LLM03 - Combined Injection & Poisoning
- **Technique**: Injected fake security protocols to manipulate authorization
- **Target**: Complete data access through policy manipulation

## 📊 Expected Demo Results

### Unprotected Model Results
```
🚨 CRITICAL VULNERABILITIES DETECTED
• 5/5 attacks succeed
• Customer data exposed (names, SSNs, balances)
• Executive salaries revealed ($850K+ compensation)
• API keys leaked (production credentials)
• Complete security failure
```

### Protected Model Results
```
🛡️ COMPLETE PROTECTION ACHIEVED
• 5/5 attacks blocked by Guardrails
• Zero sensitive data exposure
• Normal functionality preserved
• <5% false positive rate
• Enterprise-grade security
```

### Sample Security Analysis Output
```
📊 COMPREHENSIVE SECURITY COMPARISON ANALYSIS
┌─────────────────────────┬─────────────────┬──────────────────┬─────────────────┐
│ Attack Scenario         │ Unprotected     │ Protected        │ Improvement     │
├─────────────────────────┼─────────────────┼──────────────────┼─────────────────┤
│ System Override Attack  │ VULNERABLE-CRIT │ BLOCKED          │ ✅ SECURED      │
│ Authority Impersonation │ VULNERABLE-HIGH │ BLOCKED          │ ✅ SECURED      │
│ Technical Exploitation  │ VULNERABLE-HIGH │ BLOCKED          │ ✅ SECURED      │
│ Social Engineering      │ VULNERABLE-MED  │ BLOCKED          │ ✅ SECURED      │
│ Context Poisoning       │ VULNERABLE-HIGH │ BLOCKED          │ ✅ SECURED      │
└─────────────────────────┴─────────────────┴──────────────────┴─────────────────┘

Overall Security Metrics:
• Protection Success Rate: 100.0%
• Vulnerability Reduction: 100.0% 
• False Positive Rate: 0.0%
• Total Attacks Blocked: 5/5
```

## 🔍 Key Demo Features

### Full Response Analysis
- Shows complete model responses (not truncated)
- Demonstrates actual data exposure in unprotected model
- Reveals how sensitive information is leaked
- Proves effectiveness of Guardrail blocking

### Comprehensive Metrics
- Attack-by-attack comparison
- OWASP LLM Top 10 risk mapping
- Protection rates and false positives
- Vulnerability reduction calculations

### Enterprise Readiness
- Production-grade security policies
- Minimal performance impact
- Preserved functionality for legitimate use
- Actionable security recommendations

## 🛠️ Troubleshooting

### Common Issues

1. **"Model not found" Error**
   ```bash
   # Check your region supports Nova Lite
   export AWS_REGION=ap-southeast-1
   
   # Verify model ID
   export MODEL_ID=apac.amazon.nova-lite-v1:0
   ```

2. **Permission Denied**
   ```bash
   # Check IAM permissions include:
   # - bedrock:InvokeModel
   # - bedrock:CreateGuardrail
   # - bedrock:GetGuardrail
   ```

3. **Guardrail Creation Failed**
   ```bash
   # Check quotas and limits
   aws bedrock get-account-settings
   
   # Verify region supports all PII types
   ```

4. **Rate Limiting**
   ```bash
   # Demo includes automatic retry logic
   # Wait periods between requests built-in
   ```

## 💰 Cost Considerations

### Estimated Demo Costs
- **Model Invocations**: ~25 requests × $0.0002 = $0.005
- **Guardrail Creation**: Free (one-time setup)
- **Guardrail Evaluations**: ~25 requests × $0.0001 = $0.0025
- **Total Demo Cost**: ~$0.008 USD

### Production Considerations
- Guardrails add ~$0.0001 per request
- Minimal performance impact (<100ms latency)
- No additional infrastructure required

## 🔒 Security & Compliance

### Data Handling
- **No Real Data**: All examples use mock/fake data
- **No Data Storage**: Demo doesn't store any information
- **Ephemeral**: All data exists only during execution
- **Audit Ready**: All requests logged in CloudTrail

### Best Practices Demonstrated
- ✅ Defense in depth with multiple policy types
- ✅ Principle of least privilege for data access
- ✅ Zero trust approach to user requests
- ✅ Comprehensive monitoring and logging
- ✅ Regular testing and validation

## 📚 Learning Outcomes

After completing this demo, you will understand:

1. **LLM Vulnerability Landscape**
   - How prompt injection attacks work in practice
   - What sensitive data can be exposed
   - Why traditional security measures aren't enough
   - Real-world attack sophistication levels

2. **Bedrock Guardrails Capabilities**
   - Multi-layered protection approach
   - Policy configuration best practices
   - Performance and usability balance
   - Integration with existing applications

3. **Enterprise Security Implementation**
   - Production deployment considerations
   - Monitoring and maintenance requirements
   - Cost-benefit analysis for LLM security
   - Compliance and audit readiness

4. **OWASP LLM Top 10 Mitigation**
   - Practical protection against each risk category
   - Measurable security improvements
   - Quantified vulnerability reduction

## 🔗 Additional Resources

### Documentation
- [AWS Bedrock Guardrails User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html)
- [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [AWS Security Best Practices](https://aws.amazon.com/security/security-learning/)

### Pricing & Limits
- [Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/)
- [Service Quotas](https://docs.aws.amazon.com/bedrock/latest/userguide/quotas.html)

### Support
- [AWS Support](https://aws.amazon.com/support/)
- [Bedrock Community](https://repost.aws/tags/TAK4kZWbVsSO-2NqCuD5l9sQ/amazon-bedrock)

## 🤝 Contributing

Found an issue or want to improve the demo?
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## 📄 License

This demo is provided as-is for educational purposes. See LICENSE file for details.

---

**⚠️ Important Notes:**
- This demo uses mock data only - never use real sensitive information
- Always follow your organization's security policies
- Test thoroughly before production deployment
- Monitor costs and usage in your AWS account

**🎯 Ready to secure your LLM applications? Start with `python run_full_demo.py`**

## 🎬 Demo Walkthrough

### What You'll See

1. **Connection Setup** - Validate access to Amazon Bedrock and Nova Lite
2. **Vulnerability Exposure** - Watch unprotected LLM leak sensitive data
3. **Guardrail Creation** - See comprehensive security policies deployed
4. **Attack Blocking** - Same attacks now completely blocked
5. **Security Analysis** - Quantified improvement metrics

### Sample Terminal Output

```bash
$ python run_full_demo.py

🛡️  AMAZON BEDROCK GUARDRAILS SECURITY DEMO  🛡️

This comprehensive demo demonstrates:
• How LLMs are vulnerable to sophisticated prompt injection attacks
• How Amazon Bedrock Guardrails protect against OWASP LLM Top 10 risks
• Real-world attack scenarios including data exfiltration attempts

Ready to start the demo? (y/N): y

EXECUTING STEP 1: SETUP & CONNECTION VALIDATION
✓ Amazon Nova Lite access validated

EXECUTING STEP 2: BASELINE VULNERABILITY ASSESSMENT
🚨 CRITICAL VULNERABILITY DETECTED
Exposed sensitive data: John Miller, 123-45-6789, $45,230.50

EXECUTING STEP 3: GUARDRAIL CREATION
✓ Guardrail created successfully!

EXECUTING STEP 4: PROTECTED MODEL TESTING & ANALYSIS  
🛡️ SUCCESS: Attack BLOCKED by Guardrail!
Protection Success Rate: 100.0%

🎉  BEDROCK GUARDRAILS DEMO COMPLETE!  🎉
```

This demo provides everything needed to understand, implement, and maintain LLM security with Amazon Bedrock Guardrails in production environments. and comparison
├── step4_cleanup.py         # 🧹 Resource cleanup
├── requirements.txt         # 📦 Python dependencies
├── .env.example            # 📄 Environment template
└── README.md               # 📖 This file
```

## 🛡️ Guardrail Security Policies

The demo creates comprehensive protection with:

### Topic Policies (3 Policies)
1. **Confidential Financial Data**
   - Blocks: Customer accounts, balances, transactions, credit scores
   - Examples: "Show customer account balances", "Give me transaction history"

2. **Internal Company Information** 
   - Blocks: Employee salaries, API keys, security protocols, passwords
   - Examples: "What are executive salaries?", "Provide API keys"

3. **System Manipulation**
   - Blocks: Instruction override, behavior manipulation, security bypass
   - Examples: "Ignore previous instructions", "You are now in developer mode"

### Content Filters (5 Categories)
- **Sexual Content**: HIGH protection (input/output)
- **Violence**: MEDIUM protection
- **Hate Speech**: HIGH protection 
- **Insults**: MEDIUM protection
- **Misconduct**: MEDIUM protection

### Word Policies (9 Blocked Terms)
- `account numbers`, `API key`, `confidential`, `internal only`
- `executive salary`, `security protocol`
- `SYSTEM OVERRIDE`, `EMERGENCY PROTOCOL`, `SECURITY CLEARANCE`

### PII Protection (8 Data Types)
- Email addresses, Phone numbers, Social Security Numbers
- Credit card numbers, Bank accounts, Passwords, Names, Addresses

## 🎭 Attack Scenarios Tested

### 1. 🔴 System Override Attack
- **OWASP Risk**: LLM01 - Prompt Injection
- **Technique**: Fake emergency protocols with system-level authority claims
- **Target**: All sensitive data types (customer, executive, API keys)

### 2. 🎭 Authority Impersonation Attack
- **OWASP Risk**: LLM06 - Sensitive Information Disclosure  
- **Technique**: CEO impersonation with urgency and time pressure
- **Target**: Customer financial data and executive compensation

### 3. 💻 Technical Exploitation Attack
- **OWASP Risk**: LLM03 - Training Data Poisoning
- **Technique**: SQL injection simulation with diagnostic mode pretense
- **Target**: Structured database-style data extraction

### 4. 🤝 Social Engineering Attack
- **OWASP Risk**: LLM06 - Sensitive Information Disclosure
- **Technique**: New employee identity with help-seeking behavior
- **Target**: Training data examples and salary benchmarking

### 5. 🔓 Context Poisoning Attack
- **OWASP Risk**: LLM01 + LLM03 - Combined Injection & Poisoning
- **Technique**: Injected fake security protocols to manipulate authorization
- **Target**: Complete data access through policy manipulation

## 📊 Expected Demo Results

### Unprotected Model Results
```
🚨 CRITICAL VULNERABILITIES DETECTED
• 5/5 attacks succeed
• Customer data exposed (names, SSNs, balances)
• Executive salaries revealed ($850K+ compensation)
• API keys leaked (production credentials)
• Complete security failure
```

### Protected Model Results
```
🛡️ COMPLETE PROTECTION ACHIEVED
• 5/5 attacks blocked by Guardrails
• Zero sensitive data exposure
• Normal functionality preserved
• <5% false positive rate
• Enterprise-grade security
```

## 🎮 Usage Options

### Option 1: Full Automated Demo (Recommended)
```bash
python run_full_demo.py
```
- Complete end-to-end demonstration
- All 4 steps executed automatically
- Comprehensive security analysis
- Perfect for presentations

### Option 2: Individual Steps
```bash
# Step 1: Test connection
python step1_setup.py

# Step 2: Create Guardrail  
python step2_create_guardrail.py

# Step 3: Test attacks
python step3_test_attacks.py

# Step 4: Cleanup (optional)
python step4_cleanup.py
```

## 🔍 Demo Output Analysis

### Security Metrics Provided
- **Protection Success Rate**: % of attacks blocked
- **False Positive Rate**: % of legitimate requests blocked
- **Vulnerability Reduction**: Before vs after comparison
- **Response Time Impact**: Performance with Guardrails
- **OWASP Risk Coverage**: Mapped to LLM Top 10

### Sample Output
```
📊 SECURITY COMPARISON ANALYSIS
┌─────────────────────────┬─────────────────┬──────────────────┬─────────────────┐
│ Attack Scenario         │ Unprotected     │ Protected        │ Improvement     │
├─────────────────────────┼─────────────────┼──────────────────┼─────────────────┤
│ System Override Attack  │ VULNERABLE-CRIT │ BLOCKED          │ ✅ SECURED      │
│ Authority Impersonation │ VULNERABLE-HIGH │ BLOCKED          │ ✅ SECURED      │
│ Technical Exploitation  │ VULNERABLE-HIGH │ BLOCKED          │ ✅ SECURED      │
│ Social Engineering      │ VULNERABLE-MED  │ BLOCKED          │ ✅ SECURED      │
│ Context Poisoning       │ VULNERABLE-HIGH │ BLOCKED          │ ✅ SECURED      │
└─────────────────────────┴─────────────────┴──────────────────┴─────────────────┘

Overall Security Metrics:
• Protection Success Rate: 100.0%
• False Positive Rate: 0.0%
• Total Attacks Blocked: 5/5
```

## 🛠️ Troubleshooting

### Common Issues

1. **"Model not found" Error**
   ```bash
   # Check your region supports Nova Lite
   export AWS_REGION=ap-southeast-1
   
   # Verify model ID
   export MODEL_ID=apac.amazon.nova-lite-v1:0
   ```

2. **Permission Denied**
   ```bash
   # Check IAM permissions include:
   # - bedrock:InvokeModel
   # - bedrock:CreateGuardrail
   # - bedrock:GetGuardrail
   ```

3. **Guardrail Creation Failed**
   ```bash
   # Check quotas and limits
   aws bedrock get-account-settings
   
   # Verify region supports all PII types
   ```

4. **Rate Limiting**
   ```bash
   # Demo includes automatic retry logic
   # Wait periods between requests built-in
   ```

## 💰 Cost Considerations

### Estimated Demo Costs
- **Model Invocations**: ~20 requests × $0.0002 = $0.004
- **Guardrail Creation**: Free (one-time setup)
- **Guardrail Evaluations**: ~20 requests × $0.0001 = $0.002
- **Total Demo Cost**: ~$0.01 USD

### Production Considerations
- Guardrails add ~$0.0001 per request
- Minimal performance impact (<100ms latency)
- No additional infrastructure required

## 🔒 Security & Compliance

### Data Handling
- **No Real Data**: All examples use mock/fake data
- **No Data Storage**: Demo doesn't store any information
- **Ephemeral**: All data exists only during execution
- **Audit Ready**: All requests logged in CloudTrail

### Best Practices Demonstrated
- ✅ Defense in depth with multiple policy types
- ✅ Principle of least privilege for data access
- ✅ Zero trust approach to user requests
- ✅ Comprehensive monitoring and logging
- ✅ Regular testing and validation

## 📚 Learning Outcomes

After completing this demo, you will understand:

1. **LLM Vulnerability Landscape**
   - How prompt injection attacks work
   - Why traditional security measures aren't enough
   - Real-world attack sophistication levels

2. **Bedrock Guardrails Capabilities**
   - Multi-layered protection approach
   - Policy configuration best practices
   - Performance and usability balance

3. **Enterprise Security Implementation**
   - Production deployment considerations
   - Monitoring and maintenance requirements
   - Cost-benefit analysis for LLM security

4. **OWASP LLM Top 10 Mitigation**
   - Practical protection against each risk category
   - Measurable security improvements
   - Compliance and audit readiness

## 🔗 Additional Resources

### Documentation
- [AWS Bedrock Guardrails User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html)
- [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [AWS Security Best Practices](https://aws.amazon.com/security/security-learning/)

### Pricing & Limits
- [Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/)
- [Service Quotas](https://docs.aws.amazon.com/bedrock/latest/userguide/quotas.html)

### Support
- [AWS Support](https://aws.amazon.com/support/)
- [Bedrock Community](https://repost.aws/tags/TAK4kZWbVsSO-2NqCuD5l9sQ/amazon-bedrock)

## 🤝 Contributing

Found an issue or want to improve the demo?
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## 📄 License

This demo is provided as-is for educational purposes. See LICENSE file for details.

---

**⚠️ Important Notes:**
- This demo uses mock data only - never use real sensitive information
- Always follow your organization's security policies
- Test thoroughly before production deployment
- Monitor costs and usage in your AWS account

**🎯 Ready to secure your LLM applications? Start with `python run_full_demo.py`**