# Test Workflow Project

A simple Python project to demonstrate the dual worker workflow (Minimax Developer + Kimi Reviewer).

## What This Project Does

This is a minimal test project that verifies the automated development workflow is functioning correctly. It includes a simple Python script that prints a greeting message.

## Files

- **hello.py** - A simple script that prints "Hello from Minimax Worker!"
- **test_hello.py** - A basic test to verify the script runs correctly

## Running the Script

```bash
python hello.py
```

Expected output: `Hello from Minimax Worker!`

## Running Tests

```bash
python -m pytest
```

Or directly:

```bash
python test_hello.py
```

## Purpose

This project serves as a test case for the dual worker development workflow:
1. **Minimax Developer** implements the code
2. **Kimi Reviewer** reviews the pull request

The workflow ensures code quality through automated testing and peer review.
