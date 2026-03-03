# Test Workflow Project

A simple Python project demonstrating the dual worker workflow (Minimax Developer + Kimi Reviewer).

## Quick Start

```bash
python3 hello.py
```

## Output

```
Hello from Minimax Worker!
```

## Testing

Run the test to verify the script works:

```bash
python3 -c "import subprocess; result = subprocess.run(['python3', 'hello.py'], capture_output=True, text=True); print(result.stdout.strip())"
```

## Project Structure

- `hello.py` - Main script that prints a greeting
- `README.md` - This file
- `DESIGN.md` - Project requirements and acceptance criteria
