import pendulum
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

BASE = declarative_base()


class CreatedAtMixin:
    created_at = sqlalchemy.Column(
        sqlalchemy.types.DateTime(timezone=True),
        default=pendulum.now(),
        server_default=sqlalchemy.text("CURRENT_TIMESTAMP"),
        nullable=False,
    )
