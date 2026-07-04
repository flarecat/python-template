"""テスト共通フィクスチャ"""

from collections.abc import Generator

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

import models  # noqa: F401  Base.metadataへ全モデルを登録するためにインポート
from core.database import Base


@pytest.fixture
def db_session() -> Generator[Session]:
    """SQLiteインメモリDBを使った独立したテスト用セッション

    Yields:
        Session: テスト用データベースセッション
    """
    engine = create_engine("sqlite://")
    Base.metadata.create_all(bind=engine)
    session_factory = sessionmaker(bind=engine)
    with session_factory() as session:
        yield session
    engine.dispose()
