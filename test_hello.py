#!/usr/bin/env python3
"""Simple test for hello.py to verify it runs correctly."""

import subprocess
import sys

def test_hello_output():
    """Test that hello.py outputs the expected greeting."""
    result = subprocess.run(
        [sys.executable, "hello.py"],
        capture_output=True,
        text=True,
        cwd="/Users/majordomo/clawd/test-workflow"
    )
    
    assert result.returncode == 0, f"Script failed with code {result.returncode}"
    assert "Hello from Minimax Worker!" in result.stdout, f"Unexpected output: {result.stdout}"
    print("✅ Test passed: hello.py outputs correctly")

if __name__ == "__main__":
    test_hello_output()
    print("All tests passed!")
