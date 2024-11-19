from app import db
from sqlalchemy import (BLOB, Table, Column, String, Boolean, Integer, DateTime, ForeignKey, Text, UniqueConstraint,
                        Index, Date, Numeric, Double, func, CheckConstraint)
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime, date
from typing import Optional

class Recurso(db.Model):
    __tablename__ = 'recursos'

    id_recurso: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tipo_recurso: Mapped[str] = mapped_column(String(128), nullable=False)
    disponibilidad: Mapped[int] = mapped_column(Integer, nullable=False)

    def __repr__(self):
        return f"<Recurso {self.tipo_recurso}>"

