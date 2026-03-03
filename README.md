# Test Workflow Project

This is a minimal test project to verify the dual worker workflow (Minimax Developer + Kimi Reviewer) is functioning correctly.

## Project Structure

- `hello.py` - Simple Python script that prints a greeting
- `test_hello.py` - Basic test to verify the script works
- `DESIGN.md` - Project requirements and acceptance criteria

## Usage

Run the script:
```bash
python hello.py
```

Run the tests:
```bash
python -m pytest
```

Or simply:
```bash
python -c "import hello; hello.main()"
```

## Purpose

This project demonstrates the automated development workflow:
1. Minimax Worker implements the solution
2. Kimi Reviewer reviews the Pull Request
3. Both workers collaborate via GitHub PRs
