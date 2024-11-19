from app import db
from sqlalchemy import (BLOB, Table, Column, String, Boolean, Integer, DateTime, ForeignKey, Text, UniqueConstraint,
                        Index, Date, Numeric, Double, func, CheckConstraint)
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime, date
from typing import Optional

class Lugar(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(64))
    codigo_postal: Mapped[str] = mapped_column(String(10))
    personas: Mapped[list['Persona']] = relationship(back_populates='lugar')

    def __repr__(self):
        return f'<Lugar {self.nombre}>'
  