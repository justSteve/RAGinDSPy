#!/usr/bin/env python3
"""
Test script to verify Weaviate credentials and connection
"""
import os
import sys

def test_connections():
    try:
        # Load environment variables
        from dotenv import load_dotenv
        load_dotenv()
        
        import weaviate
        import dspy
        
        # Test Anthropic API key
        anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
        if not anthropic_api_key:
            print("❌ ANTHROPIC_API_KEY not found in environment variables")
            return False
        else:
            print("✅ Found ANTHROPIC_API_KEY")
        
        weaviate_url = os.getenv("WEAVIATE_URL")
        weaviate_api_key = os.getenv("WEAVIATE_API_KEY")
        
        if not weaviate_url:
            print("❌ WEAVIATE_URL not found in environment variables")
            return False
            
        if not weaviate_api_key:
            print("❌ WEAVIATE_API_KEY not found in environment variables")
            return False
            
        print(f"🔗 Connecting to Weaviate cluster: {weaviate_url}")

        # Add https:// if not present
        if not weaviate_url.startswith('http'):
            weaviate_url = f'https://{weaviate_url}'
            print(f"   Added https:// scheme: {weaviate_url}")

        # Test connection using v3 API (DSPy's WeaviateRM requires v3)
        client = weaviate.Client(
            url=weaviate_url,
            auth_client_secret=weaviate.AuthApiKey(api_key=weaviate_api_key)
        )
        
        # Test if we can access the cluster
        if client.is_ready():
            print("✅ Successfully connected to Weaviate!")
            
            # Check if the required collection exists (v3 API)
            schema = client.schema.get()
            collection_names = [cls['class'] for cls in schema.get('classes', [])]

            if "WeaviateBlogChunk" in collection_names:
                print("✅ Found 'WeaviateBlogChunk' collection - ready for DSPy!")
            else:
                print("⚠️  'WeaviateBlogChunk' collection not found")
                print(f"Available collections: {collection_names}")
                print("You may need to import the blog data first.")
            
            # v3 client doesn't need explicit close
            
            # Test Claude connection
            print("\n🤖 Testing Claude/Anthropic connection...")
            try:
                # DSPy 3.0+ uses dspy.LM with provider/model format
                # API key is read from ANTHROPIC_API_KEY environment variable
                claude_llm = dspy.LM(
                    model="anthropic/claude-3-5-sonnet-20241022",
                    max_tokens=100
                )
                test_response = claude_llm("Say 'Hello from Claude!' and nothing else.")
                # test_response is typically a list in DSPy
                response_str = str(test_response)
                if test_response and ("Claude" in response_str or "Hello" in response_str or "hello" in response_str.lower()):
                    print(f"✅ Claude connection successful!")
                    print(f"   Response: {test_response}")
                else:
                    print(f"⚠️  Claude responded but unexpectedly: {test_response}")
                return True
            except Exception as claude_error:
                print(f"❌ Claude connection failed: {str(claude_error)}")
                print(f"   Make sure:")
                print(f"   1. ANTHROPIC_API_KEY is set in your .env file")
                print(f"   2. You have the 'anthropic' package installed: pip install anthropic")
                print(f"   3. Your API key is valid and has credits")
                return False
                
        else:
            print("❌ Connected but cluster is not ready")
            return False
            
    except ImportError:
        print("❌ Missing python-dotenv. Install with: pip install python-dotenv")
        return False
    except Exception as e:
        print(f"❌ Connection failed: {str(e)}")
        return False

if __name__ == "__main__":
    print("🧪 Testing DSPy Setup with Claude and Weaviate...")
    print("=" * 60)
    
    if test_connections():
        print("\n🎉 Your setup is working correctly!")
        print("You can now run the DSPy notebook with Claude.")
    else:
        print("\n🔧 Please check your credentials and try again.")
        print("\nTroubleshooting:")
        print("1. Get Anthropic API key from: https://console.anthropic.com/")
        print("2. Verify your WEAVIATE_URL and WEAVIATE_API_KEY in .env")
        print("3. Check that your Weaviate cluster is running")
        print("4. Ensure you have internet connectivity")