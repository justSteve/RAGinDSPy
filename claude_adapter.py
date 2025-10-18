# Custom Claude adapter for DSPy
import os
import dspy
from typing import Optional, List, Dict, Any
import anthropic

class ClaudeAdapter(dspy.OpenAI):
    """
    Custom Claude adapter for DSPy that wraps Anthropic's Claude API
    to work with DSPy's interface expectations.
    """
    
    def __init__(
        self,
        model: str = "claude-3-5-sonnet-20241022",
        api_key: Optional[str] = None,
        max_tokens: int = 1000,
        temperature: float = 0.0,
        **kwargs
    ):
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature
        
        # Initialize Anthropic client
        self.client = anthropic.Anthropic(
            api_key=api_key or os.getenv("ANTHROPIC_API_KEY")
        )
        
        # Store conversation history for DSPy compatibility
        self.history = []
        
        # Don't call super().__init__ as we're not actually using OpenAI
        
    def __call__(self, prompt: str, **kwargs) -> str:
        """Main interface for DSPy compatibility"""
        try:
            # Extract any additional parameters
            max_tokens = kwargs.get('max_tokens', self.max_tokens)
            temperature = kwargs.get('temperature', self.temperature)
            
            # Make the API call to Claude
            response = self.client.messages.create(
                model=self.model,
                max_tokens=max_tokens,
                temperature=temperature,
                messages=[{"role": "user", "content": prompt}]
            )
            
            # Extract the text response
            if response.content and len(response.content) > 0:
                result = response.content[0].text
            else:
                result = ""
            
            # Store in history for DSPy's inspect_history functionality
            self.history.append({
                "prompt": prompt,
                "response": result,
                "model": self.model,
                "kwargs": kwargs
            })
            
            return result
            
        except Exception as e:
            print(f"Claude API Error: {e}")
            return f"Error: {str(e)}"
    
    def generate(self, prompt: str, **kwargs) -> List[str]:
        """Generate method for DSPy compatibility"""
        response = self.__call__(prompt, **kwargs)
        return [response]
    
    def inspect_history(self, n: int = 1) -> None:
        """Inspect recent API calls - DSPy compatibility"""
        recent_history = self.history[-n:] if n > 0 else self.history
        
        for i, entry in enumerate(recent_history, 1):
            print(f"\n=== Claude API Call {i} ===")
            print(f"Model: {entry['model']}")
            print(f"Prompt: {entry['prompt']}")
            print(f"Response: {entry['response']}")
            if entry['kwargs']:
                print(f"Parameters: {entry['kwargs']}")

# Create a convenient function to create Claude instances
def Claude(model: str = "claude-3-5-sonnet-20241022", **kwargs) -> ClaudeAdapter:
    """
    Create a Claude adapter instance for use with DSPy.
    
    Args:
        model: Claude model name (default: claude-3-5-sonnet-20241022)
        **kwargs: Additional parameters passed to ClaudeAdapter
    
    Returns:
        ClaudeAdapter instance that works with DSPy
    """
    return ClaudeAdapter(model=model, **kwargs)

# Add to dspy namespace for convenience
dspy.Claude = Claude
dspy.ClaudeAdapter = ClaudeAdapter

print("✅ Claude adapter for DSPy loaded successfully!")
print("Usage: llm = dspy.Claude(model='claude-3-5-sonnet-20241022')")