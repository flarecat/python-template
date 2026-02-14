"""ユーザーモデル"""

from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column

from models.base import BaseModel


class User(BaseModel):
    """ユーザー"""

    __tablename__ = "users"

    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False, comment="メールアドレス")
    name: Mapped[str] = mapped_column(String(100), nullable=False, comment="名前")
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False, comment="有効フラグ")

    def __repr__(self) -> str:
        return f"<User(id={self.id}, email={self.email}, name={self.name})>"
