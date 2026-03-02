# Test Workflow Project

A simple Python script demonstrating the dual worker workflow (Minimax Developer + Kimi Reviewer).

## Overview

This project tests the automated development workflow where:
1. **Minimax** (Developer Worker) implements features and creates pull requests
2. **Kimi** (Reviewer Worker) reviews PRs and provides feedback

## Files

- `hello.py` - Simple Python script that prints a greeting
- `test_hello.py` - Basic test to verify the script runs correctly

## Usage

```bash
python hello.py
```

## Testing

```bash
python -m pytest test_hello.py
```

Or run directly:
```bash
python test_hello.py
```

## Purpose

This is a minimal test project to verify the dual worker workflow is functioning correctly.
