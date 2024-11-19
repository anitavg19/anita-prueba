from app import db
from sqlalchemy import (BLOB, Table, Column, String, Boolean, Integer, DateTime, ForeignKey, Text, UniqueConstraint,
                        Index, Date, Numeric, Double, func, CheckConstraint)
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime, date
from typing import Optional


class BOM(db.Model):  # Lista de Materiales
    __tablename__ = 'bom'

    id_bom: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_producto: Mapped[int] = mapped_column(ForeignKey('productos.id_producto'), nullable=False)
    id_material: Mapped[int] = mapped_column(ForeignKey('materiales.id_material'), nullable=False)
    cantidad_por_producto: Mapped[int] = mapped_column(Integer, nullable=False)

    def __repr__(self):
        return f"<BOM Producto {self.id_producto}, Material {self.id_material}>"
