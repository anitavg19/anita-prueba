from app import db
from sqlalchemy import (BLOB, Table, Column, String, Boolean, Integer, DateTime, ForeignKey, Text, UniqueConstraint,
                        Index, Date, Numeric, Double, func, CheckConstraint)
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime, date
from typing import Optional

class Material(db.Model):
    __tablename__ = 'materiales'

    id_material: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre_material: Mapped[str] = mapped_column(String(128), nullable=False)
    cantidad_necesaria: Mapped[int] = mapped_column(Integer, nullable=False)
    tiempo_entrega: Mapped[int] = mapped_column(Integer, nullable=False)

    def __repr__(self):
        return f"<Material {self.nombre_material}>"
