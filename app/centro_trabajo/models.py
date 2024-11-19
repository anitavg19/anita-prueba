from app import db
from sqlalchemy import (BLOB, Table, Column, String, Boolean, Integer, DateTime, ForeignKey, Text, UniqueConstraint,
                        Index, Date, Numeric, Double, func, CheckConstraint)
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime, date
from typing import Optional

class CentroTrabajo(db.Model):
    __tablename__ = 'centros_trabajo'

    id_centro_trabajo: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre_centro_trabajo: Mapped[str] = mapped_column(String(128), nullable=False)
    capacidad_teorica: Mapped[int] = mapped_column(Integer, nullable=False)
    capacidad_real: Mapped[int] = mapped_column(Integer, nullable=False)

    def __repr__(self):
        return f"<CentroTrabajo {self.nombre_centro_trabajo}>"
