#!/usr/bin/env python3
"""
Caption Management App - Run Script

Usage:
    python run.py

Or with uvicorn directly:
    uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
"""
import uvicorn
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

if __name__ == "__main__":
    # Check for required env vars
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("\n⚠️  Warning: ANTHROPIC_API_KEY not set. Caption generation will not work.")
        print("   Copy .env.example to .env and add your API key.\n")

    if not os.getenv("METRICOOL_USER_TOKEN"):
        print("⚠️  Warning: METRICOOL_USER_TOKEN not set. Publishing to Metricool will not work.\n")

    print("🚀 Starting Caption Management App...")
    print("   Dashboard: http://localhost:8000")
    print("   Press Ctrl+C to stop\n")

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
