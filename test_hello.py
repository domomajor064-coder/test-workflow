#!/usr/bin/env python3
"""
test_hello.py - Simple test for the hello.py script.

This test verifies that hello.py runs without errors and outputs the correct greeting.
"""

import subprocess
import sys


def test_hello_script():
    """Test that hello.py runs and outputs the correct greeting."""
    result = subprocess.run(
        [sys.executable, "hello.py"],
        capture_output=True,
        text=True
    )
    
    # Check that the script ran successfully
    assert result.returncode == 0, f"Script failed with return code {result.returncode}"
    
    # Check that the output contains the expected greeting
    expected_output = "Hello from Minimax Worker!"
    assert expected_output in result.stdout, f"Expected '{expected_output}' in output, got: {result.stdout}"
    
    print("✅ All tests passed!")


if __name__ == "__main__":
    test_hello_script()
