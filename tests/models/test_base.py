"""ベースモデルのテスト"""

from datetime import UTC

from sqlalchemy import String
from sqlalchemy.orm import Mapped, Session, mapped_column

from models.base import BaseModel, now_utc
from models.user import User


class Sample(BaseModel):
    """__tablename__ 自動生成の確認用モデル"""

    value: Mapped[str] = mapped_column(String(50), nullable=False, comment="値")


def test_now_utc_returns_aware_utc_datetime() -> None:
    """now_utc がタイムゾーン付き（UTC）の現在時刻を返すこと"""
    result = now_utc()
    assert result.tzinfo == UTC


def test_tablename_is_generated_from_class_name() -> None:
    """__tablename__ がクラス名の小文字で自動生成されること"""
    assert Sample.__tablename__ == "sample"


def test_timestamps_are_set_on_flush(db_session: Session) -> None:
    """created_at / updated_at がINSERT時に自動設定されること"""
    user = User(email="test@example.com", name="テスト太郎")
    db_session.add(user)
    db_session.flush()

    assert user.created_at is not None
    assert user.created_at.tzinfo == UTC
    assert user.updated_at is not None
    assert user.updated_at.tzinfo == UTC


def test_to_dict_contains_all_columns(db_session: Session) -> None:
    """to_dict が全カラムを含む辞書を返すこと"""
    user = User(email="test@example.com", name="テスト太郎")
    db_session.add(user)
    db_session.flush()

    result = user.to_dict()

    assert set(result) == {"id", "email", "name", "is_active", "created_at", "updated_at"}
    assert result["email"] == "test@example.com"
    assert result["name"] == "テスト太郎"
