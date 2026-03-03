"""Simple test to verify hello.py runs correctly."""
import subprocess
import sys


def test_hello_runs():
    """Test that hello.py runs without errors."""
    result = subprocess.run(
        [sys.executable, "hello.py"],
        capture_output=True,
        text=True,
        cwd="/Users/majordomo/clawd/test-workflow"
    )
    assert result.returncode == 0, f"Script failed with code {result.returncode}"
    assert "Hello from Minimax Worker!" in result.stdout, f"Unexpected output: {result.stdout}"


def test_main_output():
    """Test that main() outputs the correct greeting."""
    # Import and test directly
    import hello
    import io
    from contextlib import redirect_stdout
    
    f = io.StringIO()
    with redirect_stdout(f):
        hello.main()
    
    output = f.getvalue()
    assert "Hello from Minimax Worker!" in output, f"Unexpected output: {output}"


if __name__ == "__main__":
    test_hello_runs()
    test_main_output()
    print("All tests passed!")
