# Getting Your Anthropic Claude API Key

This project has been configured to use **Claude** instead of OpenAI! Claude 3.5 Sonnet is excellent for RAG applications and often provides more thoughtful, detailed responses.

## 🔑 How to Get Your Claude API Key

### Step 1: Sign up for Anthropic Console
1. Go to [https://console.anthropic.com/](https://console.anthropic.com/)
2. Sign up with your email address
3. Verify your email

### Step 2: Add Credits (Required)
- Anthropic requires you to add credits to your account before using the API
- Go to "Billing" in the console
- Add at least $5-10 to start (Claude is very cost-effective)
- **Pricing**: Claude 3.5 Sonnet costs about $3 per million input tokens

### Step 3: Generate API Key
1. In the console, go to "API Keys"
2. Click "Create Key" 
3. Give it a name like "DSPy-RAG-Project"
4. Copy the generated key (starts with `sk-ant-`)

### Step 4: Configure Your Project
Add your key to the `.env` file:
```bash
ANTHROPIC_API_KEY=sk-ant-your-actual-key-here
```

## 🤖 Claude Models Available

The project is configured to use **Claude 3.5 Sonnet**, but you can easily switch:

### Claude 3.5 Sonnet (Default)
- **Model**: `claude-3-5-sonnet-20241022`
- **Best for**: Most tasks, excellent reasoning, coding
- **Cost**: ~$3/million input tokens

### Claude 3 Opus (Premium)
- **Model**: `claude-3-opus-20240229` 
- **Best for**: Most complex tasks, highest quality
- **Cost**: ~$15/million input tokens

### Claude 3 Haiku (Fast & Cheap)
- **Model**: `claude-3-haiku-20240307`
- **Best for**: Simple tasks, speed, cost optimization
- **Cost**: ~$0.25/million input tokens

## 🔄 Switching Models

To change models, edit the notebook cell:
```python
# Change this line in the notebook:
llm = dspy.Claude(model="claude-3-5-sonnet-20241022")

# To use Opus (highest quality):
llm = dspy.Claude(model="claude-3-opus-20240229")

# Or Haiku (fastest/cheapest):
llm = dspy.Claude(model="claude-3-haiku-20240307")
```

## 💰 Cost Estimation

For this DSPy RAG tutorial, expect approximately:
- **$0.50-2.00** for running through the entire notebook
- **Claude 3.5 Sonnet** provides excellent value for money
- **Claude Haiku** would cost ~$0.10-0.30 for the full tutorial

## 🧪 Test Your Setup

Run the test script to verify everything works:
```bash
python test_weaviate.py
```

## 🆚 Why Claude vs OpenAI?

**Advantages of Claude:**
- Often more thoughtful and detailed responses
- Better at following complex instructions
- Strong reasoning capabilities  
- Competitive pricing
- No waitlists or access restrictions

**Perfect for DSPy because:**
- Excellent at chain-of-thought reasoning
- Great at evaluation tasks (used in the metric functions)
- Strong few-shot learning performance
- Handles complex prompts well

You're all set to run a powerful RAG system with Claude! 🚀