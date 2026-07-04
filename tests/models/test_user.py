"""ユーザーモデルのテスト"""

from sqlalchemy import select
from sqlalchemy.orm import Session

from models.user import User


def test_tablename_is_users() -> None:
    """テーブル名が明示的に users であること"""
    assert User.__tablename__ == "users"


def test_create_user_sets_defaults(db_session: Session) -> None:
    """ユーザー作成時にデフォルト値が設定されること"""
    user = User(email="test@example.com", name="テスト太郎")
    db_session.add(user)
    db_session.flush()

    assert user.id is not None
    assert user.is_active is True


def test_query_active_users(db_session: Session) -> None:
    """有効フラグでの絞り込みができること"""
    db_session.add(User(email="active@example.com", name="有効ユーザー"))
    db_session.add(User(email="inactive@example.com", name="無効ユーザー", is_active=False))
    db_session.flush()

    active_users = db_session.scalars(select(User).where(User.is_active.is_(True))).all()

    assert len(active_users) == 1
    assert active_users[0].email == "active@example.com"


def test_repr_contains_key_fields(db_session: Session) -> None:
    """__repr__ に主要フィールドが含まれること"""
    user = User(email="test@example.com", name="テスト太郎")
    db_session.add(user)
    db_session.flush()

    assert repr(user) == f"<User(id={user.id}, email=test@example.com, name=テスト太郎)>"
