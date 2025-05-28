#!/usr/bin/env python3
"""
Script to run both FastAPI backend and Streamlit frontend
"""
import subprocess
import sys
import time
import threading
import os

def run_fastapi():
    """Run the FastAPI backend server"""
    print("🚀 Starting FastAPI backend...")
    try:
        # Use the virtual environment's python
        python_path = os.path.join('.venv', 'bin', 'python') if os.path.exists('.venv') else sys.executable
        subprocess.run([
            python_path, "-m", "uvicorn", 
            "app.main:app", 
            "--host", "0.0.0.0", 
            "--port", "8000",
            "--reload"
        ], check=True)
    except KeyboardInterrupt:
        print("\n🛑 FastAPI backend stopped")
    except Exception as e:
        print(f"❌ Error running FastAPI: {e}")

def run_streamlit():
    """Run the Streamlit frontend"""
    print("🎨 Starting Streamlit frontend...")
    time.sleep(3)  # Give FastAPI time to start
    try:
        # Use the virtual environment's python
        python_path = os.path.join('.venv', 'bin', 'python') if os.path.exists('.venv') else sys.executable
        subprocess.run([
            python_path, "-m", "streamlit", 
            "run", "streamlit_app.py",
            "--server.port", "8501",
            "--server.address", "0.0.0.0"
        ], check=True)
    except KeyboardInterrupt:
        print("\n🛑 Streamlit frontend stopped")
    except Exception as e:
        print(f"❌ Error running Streamlit: {e}")

def main():
    print("🦁 Animal Safety Checker - Starting Application")
    print("=" * 50)
    
    # Check if .env file exists
    if not os.path.exists('.env'):
        print("⚠️  Warning: .env file not found!")
        print("   Make sure to create a .env file with your PERPLEXITY_API_KEY")
        print("   Example: PERPLEXITY_API_KEY=your_api_key_here")
        print()
    
    # Check if virtual environment exists
    if not os.path.exists('.venv'):
        print("⚠️  Warning: Virtual environment not found!")
        print("   Run 'uv sync' to create the virtual environment first")
        return
    
    try:
        # Start FastAPI in a separate thread
        fastapi_thread = threading.Thread(target=run_fastapi, daemon=True)
        fastapi_thread.start()
        
        # Start Streamlit in main thread
        run_streamlit()
        
    except KeyboardInterrupt:
        print("\n🛑 Shutting down application...")
        sys.exit(0)

if __name__ == "__main__":
    main() 