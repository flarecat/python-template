"""データベース設定・接続管理"""

import os
from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

# 環境変数からデータベースURLを取得
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg://dev_user:dev_password@postgres:5432/dev_db")

# PostgreSQL接続時のみタイムゾーンをUTCに固定する
_connect_args: dict[str, str] = {"options": "-c timezone=UTC"} if DATABASE_URL.startswith("postgresql") else {}

# SQLAlchemy エンジン作成
engine = create_engine(
    DATABASE_URL,
    echo=False,  # SQLログ出力（開発時はTrueに変更可能）
    pool_pre_ping=True,  # 接続チェック
    connect_args=_connect_args,
)

# セッションファクトリ
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# ベースクラス
class Base(DeclarativeBase):
    """SQLAlchemy モデルのベースクラス"""


def get_db() -> Generator[Session]:
    """
    データベースセッション取得（FastAPI Depends用）

    Yields:
        Session: データベースセッション
    """
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


def init_db() -> None:
    """データベース初期化（開発用）"""
    Base.metadata.create_all(bind=engine)


def get_db_session() -> Session:
    """同期用データベースセッション取得"""
    return SessionLocal()
