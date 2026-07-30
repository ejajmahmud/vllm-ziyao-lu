# Standardized AI / vLLM / Agent Test Harness
import os
import sys

def init_environment():
    print("[AI Runner] Initializing environment config...")
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass

def run_agent():
    print("[AI Runner] Running agent pipeline execution...")
    openai_key = os.getenv("OPENAI_API_KEY")
    vllm_url = os.getenv("VLLM_API_URL")
    
    if not openai_key and not vllm_url:
        print("[AI Warning] Neither OPENAI_API_KEY nor VLLM_API_URL is configured.")
        print("[AI Info] Please set the environment variables to run actual calls.")
        return
        
    print("[AI Runner] Pipeline configured successfully. Ready for evaluation.")

if __name__ == "__main__":
    init_environment()
    run_agent()
