---
description: 現在のブランチの変更内容を確認してデフォルトブランチに対してPRを作成
---

# Let's Pull Request

現在のリポジトリーの修正内容を確認してデフォルトブランチに対して、PRを出してください。
今回の依頼に限りgit操作を許可します。
次回以降のgit操作はルールに基づいて確認してください。

リポジトリのデフォルトブランチは必ず見てください。mainではない可能性があるため必ず確認。
比較する際はPRを出すブランチと比較してください。

デフォルトブランチを取得するコマンド：
`gh repo view --json defaultBranchRef -q '.defaultBranchRef.name'`

## PRラベル

PR作成時に以下から適切なラベルを選択してください（最大5つ）：

- `enhancement`: 新機能・機能追加
- `bugfix`: バグ修正
- `refactor`: リファクタリング
- `documentation`: ドキュメント更新
- `test`: テスト追加・修正
- `ci`: CI/CD関連
- `dependencies`: 依存関係の更新
- `security`: セキュリティ関連
- `performance`: パフォーマンス改善
