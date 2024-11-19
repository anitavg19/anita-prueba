from app import db
from sqlalchemy import (BLOB, Table, Column, String, Boolean, Integer, DateTime, ForeignKey, Text, UniqueConstraint,
                        Index, Date, Numeric, Double, func, CheckConstraint)
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime, date
from typing import Optional

class Producto(db.Model):
    __tablename__ = 'productos'

    id_producto: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre_producto: Mapped[str] = mapped_column(String(128), nullable=False)
    demanda_planeada: Mapped[int] = mapped_column(Integer, nullable=True)
    fecha_entrega: Mapped[date] = mapped_column(Date, nullable=True)
    cantidad_producir: Mapped[int] = mapped_column(Integer, nullable=True)

    def __repr__(self):
        return f"<Producto {self.nombre_producto}>"
