#!/bin/bash

echo "🚀 Setting up Python development environment..."

# Install Python dependencies if requirements.txt exists
if [ -f "/workspace/requirements.txt" ]; then
    echo "📦 Installing Python dependencies from requirements.txt..."
    pip install --user -r /workspace/requirements.txt
else
    echo "ℹ️  No requirements.txt found, skipping dependency installation"
fi

# Set up git hooks if pre-commit is configured
if [ -f "/workspace/.pre-commit-config.yaml" ]; then
    echo "🪝 Setting up pre-commit hooks..."
    pre-commit install
else
    echo "ℹ️  No .pre-commit-config.yaml found, skipping pre-commit setup"
fi

# Create common directories if they don't exist
mkdir -p /workspace/tests
mkdir -p /workspace/logs
mkdir -p /workspace/coverage
mkdir -p /workspace/src

echo "✅ Development environment setup complete!"
echo ""
echo "Available development commands:"
echo "  pytest-all       - Run all tests"
echo "  pytest-cov       - Run tests with coverage"
echo "  ruff-check       - Check code with Ruff"
echo "  ruff-fix         - Fix code issues with Ruff"
echo "  ruff-format      - Format code with Ruff"
echo "  mypy-check       - Type check with mypy"
echo "  black-format     - Format code with Black"
echo "  isort-format     - Sort imports with isort"
echo ""
echo "Database connection:"
echo "  DATABASE_URL: $DATABASE_URL"
echo ""
