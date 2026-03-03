"""Tests for hello.py script."""
import subprocess
import sys
from io import StringIO


def test_hello_output():
    """Test that hello.py prints the expected greeting."""
    result = subprocess.run(
        [sys.executable, "hello.py"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, f"Script failed with: {result.stderr}"
    assert "Hello from Minimax Worker!" in result.stdout


def test_main_imports():
    """Test that hello module can be imported without errors."""
    import hello
    # Capture stdout
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    hello.main()
    output = sys.stdout.getvalue()
    sys.stdout = old_stdout
    assert "Hello from Minimax Worker!" in output


if __name__ == "__main__":
    test_hello_output()
    test_main_imports()
    print("All tests passed!")
