"""Импорты класса Base и всех моделей для Alembic."""
from app.core.db import Base  # noqa
from .user import User  # noqa
from .charityproject import CharityProject  # noqa
from .donation import Donation  # noqa
