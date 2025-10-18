# DSPy RAG Project Setup

This project has been set up with a Python virtual environment to ensure clean dependency management.

## Project Structure

```
├── venv/                          # Python virtual environment
├── requirements.txt              # Python dependencies
├── .env.example                  # Environment variable template
├── activate.sh                   # Convenient activation script
├── 1.Getting-Started-with-RAG-in-DSPy.ipynb  # Main notebook
└── ...                          # Other project files
```

## Quick Start

### 1. Set up Environment Variables

Copy the example environment file and fill in your API keys:

```bash
cp .env.example .env
# Edit .env with your actual API keys
```

### 2. Activate the Virtual Environment

Use the provided activation script:

```bash
./activate.sh
```

Or manually activate:

```bash
source venv/bin/activate
```

### 3. Verify Installation

```bash
python -c "import dspy; print('DSPy version:', dspy.__version__)"
python -c "import weaviate; print('Weaviate client installed successfully')"
```

### 4. Launch Jupyter Notebook

```bash
jupyter notebook
```

Then open `1.Getting-Started-with-RAG-in-DSPy.ipynb` to get started!

## Dependencies

The virtual environment includes:

- **dspy-ai** (3.0+) - Main DSPy framework for LLM programming with modern API
- **weaviate-client** (4.0+) - Vector database client with v4 API
- **anthropic** - Anthropic Claude API client
- **python-dotenv** - Environment variable management
- **jupyter** - Notebook environment
- **pandas, numpy, matplotlib, seaborn** - Data science libraries
- **ipywidgets** - Interactive notebook widgets

## Environment Variables

Required environment variables (set in `.env` file):

- `ANTHROPIC_API_KEY` - Your Anthropic API key (get from https://console.anthropic.com/)
- `WEAVIATE_URL` - Your Weaviate cluster URL (**Important**: use the actual cluster endpoint like `https://your-cluster.weaviate.network`, NOT the console page URL)
- `WEAVIATE_API_KEY` - Your Weaviate API key

**Note**: GitHub Copilot previously put placeholder/incorrect values in the .env file. Make sure to use your actual credentials!

## Deactivation

To deactivate the virtual environment when you're done:

```bash
deactivate
```

## Troubleshooting

If you encounter any issues:

1. Ensure you're in the virtual environment: `which python` should point to `venv/bin/python`
2. Check that all environment variables are set: `echo $ANTHROPIC_API_KEY`
3. Reinstall dependencies if needed: `pip install -r requirements.txt`

## Security Notes

- Never commit `.env` files to version control
- The notebook has been updated to use environment variables instead of hardcoded API keys
- Keep your API keys secure and rotate them regularly