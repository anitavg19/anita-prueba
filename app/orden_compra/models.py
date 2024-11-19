from app import db
from sqlalchemy import (BLOB, Table, Column, String, Boolean, Integer, DateTime, ForeignKey, Text, UniqueConstraint,
                        Index, Date, Numeric, Double, func, CheckConstraint)
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime, date
from typing import Optional

class OrdenCompra(db.Model):
    __tablename__ = 'ordenes_compra'

    id_orden_compra: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_proveedor: Mapped[int] = mapped_column(Integer, nullable=False)
    material_solicitado: Mapped[int] = mapped_column(ForeignKey('materiales.id_material'), nullable=False)
    cantidad_ordenada: Mapped[int] = mapped_column(Integer, nullable=False)
    fecha_entrega_esperada: Mapped[Date] = mapped_column(Date, nullable=False)

    def __repr__(self):
        return f"<OrdenCompra {self.id_orden_compra}>"
