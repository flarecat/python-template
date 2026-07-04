# ============================================
# Python 3.14 Development Environment
# ============================================
FROM python:3.14-slim

# Install system dependencies for development
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    dnsutils \
    gnupg2 \
    git \
    build-essential \
    ca-certificates \
    sudo \
    nano \
    vim \
    wget \
    gh \
    procps \
    tree \
    htop \
    jq \
    zip \
    unzip \
    openssh-client \
    postgresql-client \
    lsof \
    supervisor \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Japanese fonts for Playwright/Chromium screenshots
RUN apt-get update && apt-get install -y --no-install-recommends \
    fontconfig \
    fonts-ipafont-gothic \
    fonts-takao-gothic \
    && fc-cache -f -v \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set timezone to Asia/Tokyo
RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && echo 'Asia/Tokyo' > /etc/timezone

# Install Node.js (required for MCP servers and other tools)
RUN curl -fsSL https://deb.nodesource.com/setup_22.x | bash - \
    && apt-get install -y nodejs \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install MCP Chrome Bridge and Chrome DevTools MCP Server
RUN npm install -g mcp-chrome-bridge chrome-devtools-mcp@latest

# Install Google Chrome for MCP Chrome DevTools
RUN wget -q -O /tmp/google-chrome-key.pub https://dl-ssl.google.com/linux/linux_signing_key.pub \
    && gpg --dearmor -o /usr/share/keyrings/google-chrome-keyring.gpg /tmp/google-chrome-key.pub \
    && rm /tmp/google-chrome-key.pub \
    && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-chrome-keyring.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN useradd -m -s /bin/bash vscode \
    && usermod -aG sudo vscode \
    && echo 'vscode ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# Install Python development tools
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# Set working directory
WORKDIR /workspace

# Change ownership of workspace
RUN chown -R vscode:vscode /workspace

# Switch to non-root user
USER vscode

# ~/.local/bin（Claude Code・pip --userツール）を非対話プロセスからも参照可能にする
ENV PATH="/home/vscode/.local/bin:${PATH}"

# Set up development environment variables and shell configuration
RUN echo 'export EDITOR=nano' >> ~/.bashrc && \
    echo 'export PYTHONDONTWRITEBYTECODE=1' >> ~/.bashrc && \
    echo 'export PYTHONUNBUFFERED=1' >> ~/.bashrc && \
    echo 'alias ll="ls -alF"' >> ~/.bashrc && \
    echo 'alias la="ls -A"' >> ~/.bashrc && \
    echo 'alias l="ls -CF"' >> ~/.bashrc && \
    echo 'alias grep="grep --color=auto"' >> ~/.bashrc && \
    echo 'alias ..="cd .."' >> ~/.bashrc && \
    echo 'alias ...="cd ../.."' >> ~/.bashrc

# Install Claude Code CLI (native installer, auto-updates in background)
RUN curl -fsSL https://claude.ai/install.sh | bash

# Install development-specific Python packages
RUN pip install --no-cache-dir --user \
    pytest \
    pytest-asyncio \
    pytest-cov \
    pytest-mock \
    pytest-xdist \
    mypy \
    ruff \
    pre-commit \
    ipython \
    jupyterlab \
    bandit \
    detect-secrets \
    python-dotenv \
    pip-audit \
    pyright \
    alembic \
    sqlalchemy \
    "psycopg[binary]" \
    flaretool

# Add comprehensive development aliases
RUN echo '# Testing aliases' >> ~/.bashrc && \
    echo 'alias pytest-all="python -m pytest tests/"' >> ~/.bashrc && \
    echo 'alias pytest-cov="python -m pytest tests/ --cov-report=html"' >> ~/.bashrc && \
    echo '# Type checking aliases' >> ~/.bashrc && \
    echo 'alias mypy-check="mypy ."' >> ~/.bashrc && \
    echo '# Code quality aliases (Ruff統一)' >> ~/.bashrc && \
    echo 'alias ruff-check="ruff check ."' >> ~/.bashrc && \
    echo 'alias ruff-fix="ruff check --fix ."' >> ~/.bashrc && \
    echo 'alias ruff-format="ruff format ."' >> ~/.bashrc && \
    echo '# Database aliases' >> ~/.bashrc && \
    echo 'alias db-migrate="cd /workspace/src && alembic upgrade head"' >> ~/.bashrc && \
    echo 'alias db-revision="cd /workspace/src && alembic revision --autogenerate -m"' >> ~/.bashrc && \
    echo 'alias db-downgrade="cd /workspace/src && alembic downgrade -1"' >> ~/.bashrc && \
    echo '# Git aliases' >> ~/.bashrc && \
    echo 'alias gs="git status"' >> ~/.bashrc && \
    echo 'alias ga="git add"' >> ~/.bashrc && \
    echo 'alias gc="git commit"' >> ~/.bashrc && \
    echo 'alias gp="git push"' >> ~/.bashrc && \
    echo 'alias gl="git log --oneline"' >> ~/.bashrc

# Set up Python environment for development
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set up git configuration placeholders (will be overridden by user)
RUN git config --global --add safe.directory /workspace && \
    git config --global init.defaultBranch main

# Create directories for development
RUN mkdir -p /workspace/logs /workspace/coverage /workspace/tests-reports

# Switch to root for final setup
USER root

# Install Playwright system dependencies and browsers
RUN pip install --no-cache-dir playwright && \
    playwright install-deps && \
    playwright install chromium

# Copy supervisor configuration
COPY .devcontainer/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Create supervisor log directory
RUN mkdir -p /var/log/supervisor

# Create startup script for Chrome DevTools
RUN echo '#!/bin/bash' > /usr/local/bin/start-chrome-devtools.sh && \
    echo 'google-chrome-stable --headless --disable-gpu --no-sandbox --remote-debugging-port=9222 --disable-dev-shm-usage --disable-software-rasterizer --disable-extensions about:blank > /dev/null 2>&1 &' >> /usr/local/bin/start-chrome-devtools.sh && \
    echo 'echo "Chrome DevTools started on port 9222"' >> /usr/local/bin/start-chrome-devtools.sh && \
    chmod +x /usr/local/bin/start-chrome-devtools.sh

# Add Chrome alias
RUN echo '# Chrome DevTools alias' >> /home/vscode/.bashrc && \
    echo 'alias start-chrome="start-chrome-devtools.sh"' >> /home/vscode/.bashrc && \
    echo 'alias stop-chrome="pkill -f \"chrome.*remote-debugging\""' >> /home/vscode/.bashrc

# Switch back to vscode user
USER vscode

CMD ["sleep", "infinity"]
