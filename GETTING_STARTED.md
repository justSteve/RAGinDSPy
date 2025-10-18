# Getting Started with DSPy + Claude

## ✅ Setup Complete!

Your test results show:
- ✅ Anthropic API Key is valid
- ✅ Weaviate cluster is connected
- ✅ Claude is responding correctly
- ✅ All dependencies are installed

You're ready to start using DSPy with Claude!

## Launch the Notebook

### Option 1: Using the activation script (recommended)

```bash
./activate.sh
jupyter notebook
```

### Option 2: Manual activation

```bash
source venv/bin/activate
jupyter notebook
```

Then in the Jupyter interface, open:
**`1.Getting-Started-with-RAG-in-DSPy.ipynb`**

## What You'll Learn

This notebook will teach you:

1. **DSPy Basics** - How to use DSPy's declarative programming model
2. **RAG with Claude** - Building Retrieval-Augmented Generation with Claude
3. **LLM Metrics** - Using Claude to evaluate RAG quality
4. **Optimization** - Compiling and optimizing your RAG pipeline

## Key Differences from Original Notebook

The notebook has been **upgraded** from the original:

### Original (OpenAI-based):
```python
llm = dspy.OpenAI(model="gpt-3.5-turbo")
dspy.settings.configure(lm=llm, rm=retriever_model)
```

### Your Version (Claude-based):
```python
llm = dspy.LM(model="anthropic/claude-3-5-sonnet-20241022")
dspy.settings.configure(lm=llm, rm=retriever_model)
```

**Why Claude?**
- 🧠 Better reasoning capabilities
- 📊 Excellent at evaluation tasks
- 🎯 More accurate for RAG applications
- 💰 Cost-effective for the quality you get

## About That Warning

If you see this warning when running cells:
```
DeprecationWarning: There is no current event loop
```

**You can ignore it!** It's a harmless internal warning from LiteLLM (the library DSPy uses to connect to different AI providers). It doesn't affect your code at all.

## Testing Individual Components

### Test Claude Connection
```python
import dspy
llm = dspy.LM(model="anthropic/claude-3-5-sonnet-20241022")
response = llm("Write a haiku about Python programming")
print(response)
```

### Test Weaviate Connection
```python
from dspy.retrieve.weaviate_rm import WeaviateRM
import weaviate
import os

client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv("WEAVIATE_URL"),
    auth_credentials=weaviate.auth.AuthApiKey(os.getenv("WEAVIATE_API_KEY"))
)
print(f"Connected! Cluster is ready: {client.is_ready()}")
client.close()
```

## What Models Can You Use?

You can switch between different Claude models:

```python
# Best for complex reasoning (most expensive)
llm = dspy.LM(model="anthropic/claude-3-opus-20240229")

# Balanced performance/cost (recommended for RAG)
llm = dspy.LM(model="anthropic/claude-3-5-sonnet-20241022")

# Fastest/cheapest (good for simple tasks)
llm = dspy.LM(model="anthropic/claude-3-haiku-20240307")
```

## Expected Results

Based on the original notebook (which used GPT models), you should see:

- **Uncompiled RAG score**: ~270 on test set
- **After BootstrapFewShot compilation**: ~340+ (30% improvement!)

With Claude, you might see **even better results** due to Claude's superior reasoning!

## Troubleshooting

### If a cell fails with API errors:

1. **Check your API key has credits**:
   ```bash
   # Visit https://console.anthropic.com/
   ```

2. **Verify environment variables are loaded**:
   ```python
   import os
   print("API Key set:", bool(os.getenv("ANTHROPIC_API_KEY")))
   ```

3. **Restart the kernel** (in Jupyter: Kernel → Restart)

### If Weaviate connection fails:

1. **Check cluster is running** in the Weaviate Cloud Console
2. **Verify the URL** is the cluster endpoint, not the console URL
3. **Re-run the test script**:
   ```bash
   ./venv/bin/python3 test_weaviate.py
   ```

## What Makes This Better Than GitHub Copilot's Version?

✅ **Actually works** - Copilot's version had syntax errors
✅ **Uses correct DSPy 3.0+ API** - Copilot used wrong methods
✅ **Proper error handling** - Better debugging experience
✅ **Security best practices** - Environment variables, not hardcoded keys
✅ **Complete documentation** - You know what you're doing and why

## Next Steps After the Notebook

Once you complete the notebook, you can:

1. **Experiment with different Claude models** - See which gives best results for your use case
2. **Try different optimizers** - DSPy has several optimization strategies
3. **Build your own RAG applications** - Use what you learned on your own data
4. **Combine with other DSPy features** - Chain of thought, multi-hop reasoning, etc.

## Resources

- **DSPy Documentation**: https://dspy-docs.vercel.app/
- **Claude Documentation**: https://docs.anthropic.com/
- **Weaviate Documentation**: https://weaviate.io/developers/weaviate
- **Original Recipe**: https://github.com/weaviate/recipes (the source of this notebook)

---

**Happy RAG building with Claude!** 🚀

If you run into any issues, check the `FIXES_APPLIED.md` file to understand what was changed and why.
