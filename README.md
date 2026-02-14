# Python 開発テンプレート

モダンなツールと設定で構成された Python
3.12 開発テンプレート。DevContainer サポート付き。

## 特徴

### 開発環境

- **Python 3.12** - 最新の安定版 Python
- **DevContainer** - Docker 内の完全な VS Code 開発環境
- **PostgreSQL 15** - 開発用データベース（オプション）

### コード品質

- **Ruff** - 高速なリンター・フォーマッター（Black、isort、多数の flake8 プラグインを統合）
- **mypy** - 静的型チェッカー
- **pytest** - カバレッジサポート付きテストフレームワーク
- **pre-commit** - コミット前の自動コード品質チェック

### セキュリティ

- **detect-secrets** - 機密情報の誤コミット防止
- **bandit** - Pythonセキュリティ脆弱性スキャナー
- **pip-audit** - 依存関係の脆弱性チェック

### AI 開発支援

- **Claude Code** - AI支援開発環境
- **Chrome DevTools MCP** - ブラウザ自動操作・テスト
- **Context7 MCP** - 最新ライブラリドキュメント参照

## クイックスタート

### DevContainer を使用（推奨）

1. [Docker](https://www.docker.com/) と
   [VS Code](https://code.visualstudio.com/) をインストール
2. [Dev Containers 拡張機能](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)をインストール
3. このリポジトリを VS Code で開く
4. **重要**: `.devcontainer/.env.example` を `.devcontainer/.env`
   にコピーし、必要に応じて編集
   ```bash
   cp .devcontainer/.env.example .devcontainer/.env
   ```
5. プロンプトが表示されたら「コンテナーで再度開く」をクリック

すべてのツールがインストールされた開発環境が自動的にセットアップされます。

### PostgreSQL の有効/無効の切り替え

このテンプレートでは、PostgreSQL を使用する場合と使用しない場合の両方をサポートしています。

#### PostgreSQL を使用する場合（デフォルト）

`.devcontainer/devcontainer.json`
を使用してコンテナを起動します。PostgreSQL が自動的に起動します。

#### PostgreSQL を使用しない場合

1. `.devcontainer/devcontainer.json` を `.devcontainer/devcontainer.json.bak`
   にリネーム
2. `.devcontainer/devcontainer-no-db.json` を `.devcontainer/devcontainer.json`
   にコピー
   ```bash
   mv .devcontainer/devcontainer.json .devcontainer/devcontainer.json.bak
   cp .devcontainer/devcontainer-no-db.json .devcontainer/devcontainer.json
   ```
3. VS Code でコンテナを再起動

### 複数プロジェクトでの同時使用

このテンプレートから複数のプロジェクトを作成し、同一端末で同時に起動する場合:

1. まず、`.devcontainer/.env.example` を `.devcontainer/.env` にコピー
   ```bash
   cp .devcontainer/.env.example .devcontainer/.env
   ```
2. 各プロジェクトの `.devcontainer/.env` ファイルで `COMPOSE_PROJECT_NAME`
   を**一意の値**に設定
   ```bash
   COMPOSE_PROJECT_NAME=my-project-name
   ```
3. これにより、各プロジェクトのコンテナ名が `my-project-name-app-1`,
   `my-project-name-postgres-1` のように一意になります

**注意**: `COMPOSE_PROJECT_NAME`
を設定しない場合、プロジェクトのディレクトリ名がコンテナ名のプレフィックスとして使用されます。

### 手動セットアップ

```bash
# 仮想環境を作成
python3.12 -m venv .venv
source .venv/bin/activate  # Windows の場合: .venv\Scripts\activate

# 依存関係をインストール
pip install -r requirements.txt

# 開発ツールをインストール
pip install pytest pytest-cov mypy ruff black isort pre-commit
```

## Git 設定と GitHub 認証

DevContainer の初回起動後、Git とGitHub の設定を行います。

### Git ユーザー情報の設定

```bash
# ユーザー名を設定
git config --global user.name "Your Name"

# メールアドレスを設定
git config --global user.email "your.email@example.com"

# 設定を確認
git config --global --list
```

### GitHub 認証

GitHub CLI を使用して GitHub にログインします：

```bash
# GitHub にログイン
gh auth login

# プロンプトに従って選択:
# - What account do you want to log into? → GitHub.com
# - What is your preferred protocol for Git operations? → HTTPS (推奨)
# - Authenticate Git with your GitHub credentials? → Yes
# - How would you like to authenticate GitHub CLI? → Login with a web browser (推奨)
#   または Paste an authentication token (トークンを持っている場合)

# 認証状態を確認
gh auth status
```

**注意**: ログイン時にブラウザが開き、ワンタイムコードの入力が求められます。コードをコピーしてブラウザに貼り付けて認証を完了してください。

## 開発コマンド

DevContainer には一般的なタスク用の便利なエイリアスが含まれています：

### テスト

```bash
pytest-all      # すべてのテストを実行
pytest-cov      # カバレッジレポート付きでテストを実行
```

### コード品質

```bash
ruff-check      # Ruff でコードをチェック
ruff-fix        # Ruff でコードの問題を修正
ruff-format     # Ruff でコードをフォーマット
mypy-check      # mypy で型チェック
black-format    # Black でコードをフォーマット
isort-format    # isort でインポートをソート
```

### Git

```bash
gs              # git status
ga              # git add
gc              # git commit
gp              # git push
gl              # git log --oneline
```

## プロジェクト構造

```
.
├── .devcontainer/          # DevContainer 設定
│   ├── Dockerfile          # 開発環境セットアップ
│   ├── docker-compose.yml  # サービス（PostgreSQL など）
│   ├── devcontainer.json   # VS Code 設定と拡張機能
│   ├── setup.sh            # 作成後のセットアップスクリプト
│   └── .env.example        # 環境変数テンプレート
├── .claude/                # Claude Code 設定
│   ├── settings.json       # 権限とMCPサーバー設定
│   └── commands/           # カスタムコマンド
├── src/                    # ソースコード
│   ├── alembic/            # データベースマイグレーション
│   ├── core/               # コア機能（DB設定など）
│   └── models/             # データベースモデル
├── tests/                  # テストファイル
├── .gitignore              # Git 除外パターン
├── .pre-commit-config.yaml # pre-commit設定
├── .secrets.baseline       # detect-secretsベースライン
├── .mcp.json               # MCPサーバー設定
├── pyproject.toml          # Python プロジェクト設定
├── requirements.txt        # Python 依存関係
├── CLAUDE.md               # Claude Code開発ガイドライン
└── README.md               # このファイル
```

## 設定

### Ruff

Ruff は [pyproject.toml](pyproject.toml) で設定されています：

- 行の長さ：120 文字
- ターゲット：Python 3.12
- 統合：リント、フォーマット、インポートソート

### mypy

型チェック設定は [pyproject.toml](pyproject.toml) にあります：

- Python バージョン：3.12
- 名前空間パッケージ有効
- インポートエラー無視（調整可能）

### pytest

テスト設定は [pyproject.toml](pyproject.toml) にあります：

- テストディレクトリ：`tests/`
- カバレッジレポート：ターミナルと HTML
- マーカー：`slow`、`integration`、`unit`

## セキュリティ

### pre-commit フック

コミット前に自動でコード品質チェックとセキュリティスキャンを実行します。

**設定ファイル**: `.pre-commit-config.yaml`

**自動実行されるチェック**:

- ファイル末尾の改行チェック
- 行末の空白削除
- YAML/JSON/TOML 構文チェック
- 大きなファイルの追加防止
- マージコンフリクトマーカーチェック
- Ruff によるリント・フォーマット
- mypy による型チェック
- Prettier によるフォーマット
- **detect-secrets による機密情報検出**

**初回セットアップ**:

```bash
# DevContainer起動時に自動実行されます
pre-commit install
```

**手動実行**:

```bash
# 全ファイルに対して実行
pre-commit run --all-files
```

### detect-secrets

パスワード、APIキー、トークンなどの機密情報が誤ってコミットされることを防ぎます。

**ベースラインファイル**: `.secrets.baseline`

**使い方**:

```bash
# ベースラインを更新（新しい秘密情報を許可する場合）
detect-secrets scan --baseline .secrets.baseline

# スキャン実行
detect-secrets scan
```

**注意**: 新しく秘密情報と判定された場合、コミットがブロックされます。意図的に含める場合は、ベースラインファイルを更新してください。

## Chrome DevTools MCP

ブラウザの自動操作とテストを Claude Code から直接実行できます。

### 機能

- ページのナビゲーションと操作
- スクリーンショット取得
- ネットワークリクエストの監視
- コンソールログの取得
- パフォーマンス分析

### 起動方法

```bash
# Chrome DevTools を起動
start-chrome

# 停止
stop-chrome
```

### 設定

**MCPサーバー設定**: `.mcp.json`

Chrome
DevTools は起動時に自動的にバックグラウンドで起動されます（supervisord による管理）。

## データベース

DevContainer には PostgreSQL
15 が含まれています（PostgreSQL を有効にしている場合）。

データベース設定は `.devcontainer/.env` ファイルでカスタマイズできます:

- **ホスト**：`postgres`（コンテナ内から）
- **ポート**：`5432`
- **データベース**：`${POSTGRES_DB}` (デフォルト: `dev_db`)
- **ユーザー**：`${POSTGRES_USER}` (デフォルト: `dev_user`)
- **パスワード**：`${POSTGRES_PASSWORD}` (デフォルト: `dev_password`)
- **接続文字列**：`postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@postgres:5432/${POSTGRES_DB}`

以下でアクセス：

```bash
psql -h postgres -U ${POSTGRES_USER} -d ${POSTGRES_DB}
```

または VS Code の Database Client 拡張機能を使用。

### ⚠️ 本番環境での注意事項

**重要**: コード内のデフォルト値は開発環境専用です。本番環境では必ず環境変数を設定してください。

- `DATABASE_URL` 環境変数で接続文字列を上書き
- デフォルトパスワード (`dev_password`) は絶対に本番で使用しない
- 強固なパスワードとアクセス制限を設定

## VS Code 拡張機能

DevContainer では以下の拡張機能が自動的にインストールされます：

### Python 開発

- Python (ms-python.python)
- Pylance (ms-python.vscode-pylance)
- Ruff (charliermarsh.ruff)
- mypy (ms-python.mypy-type-checker)
- Black Formatter (ms-python.black-formatter)
- isort (ms-python.isort)

### データベース

- SQLTools (mtxr.sqltools)
- PostgreSQL Driver (mtxr.sqltools-driver-pg)
- Database Client (cweijan.vscode-database-client2)

### Git & GitHub

- GitLens (eamodio.gitlens)
- GitHub Pull Requests (github.vscode-pull-request-github)
- Git History (donjayamanne.githistory)
- Git Graph (mhutchie.git-graph)

### ユーティリティ

- EditorConfig (editorconfig.editorconfig)
- Code Spell Checker (streetsidesoftware.code-spell-checker)
- REST Client (humao.rest-client)
- Markdown All in One (yzhang.markdown-all-in-one)
- Claude Code (anthropic.claude-code)

## Claude Code

### カスタムコマンド

`.claude/commands/` にカスタムコマンドが用意されています：

- `/check-ruff` - Ruff でコード品質チェック
- `/create-branch` - 新しいブランチを作成
- `/pr` - プルリクエストを作成

### MCP サーバー

`.mcp.json` で以下の MCP サーバーが設定されています：

- **Context7** - 最新ライブラリドキュメントの参照
- **Chrome DevTools** - ブラウザ自動操作とテスト

設定ファイル: `.claude/settings.json`, `.mcp.json`

## コントリビューション

1. フィーチャーブランチを作成
2. 変更を加える
3. テストを実行：`pytest-all`
4. コード品質をチェック：`ruff-check`
5. コードをフォーマット：`ruff-format`
6. 型チェック：`mypy-check`
7. コミット（pre-commit フックが自動実行されます）
8. プッシュ

**注意**: コミット時に pre-commit フックが自動実行され、コード品質とセキュリティチェックが行われます。チェックに失敗した場合は、修正してから再度コミットしてください。

## ライセンス

MIT License - このテンプレートをプロジェクトで自由に使用できます。
