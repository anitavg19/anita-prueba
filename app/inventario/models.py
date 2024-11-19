from app import db
from sqlalchemy import (BLOB, Table, Column, String, Boolean, Integer, DateTime, ForeignKey, Text, UniqueConstraint,
                        Index, Date, Numeric, Double, func, CheckConstraint)
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime, date
from typing import Optional

class Inventario(db.Model):
    __tablename__ = 'inventario'

    id_inventario: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_material: Mapped[int] = mapped_column(Integer, nullable=False)
    cantidad_disponible: Mapped[int] = mapped_column(Integer, nullable=False)
    cantidad_requerida: Mapped[int] = mapped_column(Integer, nullable=False)
    fecha_reabastecimiento: Mapped[Date] = mapped_column(Date, nullable=True)

    def __repr__(self):
        return f"<Inventario {self.id_inventario}>"
