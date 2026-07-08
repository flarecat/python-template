"""ベースモデル定義"""

from datetime import UTC, datetime
from typing import Any

from sqlalchemy import DateTime, Integer
from sqlalchemy.orm import Mapped, declared_attr, mapped_column

from core.database import Base


def now_utc() -> datetime:
    """UTC現在時刻を取得"""
    return datetime.now(UTC)


class BaseModel(Base):
    """共通ベースモデル"""

    __abstract__ = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, comment="ID")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=now_utc, nullable=False, comment="作成日時"
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=now_utc, onupdate=now_utc, nullable=False, comment="更新日時"
    )

    @declared_attr.directive
    @classmethod
    def __tablename__(cls) -> str:
        """テーブル名を自動生成（クラス名の小文字）"""
        return cls.__name__.lower()

    def to_dict(self) -> dict[str, Any]:
        """辞書形式に変換"""
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}(id={self.id})>"
