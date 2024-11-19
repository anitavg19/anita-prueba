from app import db
from sqlalchemy import (BLOB, Table, Column, String, Boolean, Integer, DateTime, ForeignKey, Text, UniqueConstraint,
                        Index, Date, Numeric, Double, func, CheckConstraint)
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime, date
from typing import Optional

class OrdenProduccion(db.Model):
    __tablename__ = 'orden_produccion'

    id_orden: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    producto_asociado: Mapped[int] = mapped_column(ForeignKey('productos.id_producto'), nullable=False)
    fecha_inicio_produccion: Mapped[Date] = mapped_column(Date, nullable=False)
    fecha_fin_produccion: Mapped[Date] = mapped_column(Date, nullable=False)
    cantidad_ordenada: Mapped[int] = mapped_column(Integer, nullable=False)

    def __repr__(self):
        return f"<OrdenProduccion {self.id_orden}>"
