#!/usr/bin/env python3
"""Simple test to verify hello.py runs correctly."""
import subprocess
import sys

def test_hello():
    """Test that hello.py prints the correct greeting."""
    result = subprocess.run(
        [sys.executable, "hello.py"],
        capture_output=True,
        text=True,
        cwd="/Users/majordomo/clawd/test-workflow"
    )
    
    expected = "Hello from Minimax Worker!"
    actual = result.stdout.strip()
    
    assert actual == expected, f"Expected '{expected}', got '{actual}'"
    print("✅ Test passed: hello.py outputs correct greeting")

if __name__ == "__main__":
    test_hello()
