from app import db
from sqlalchemy import (BLOB, Table, Column, String, Boolean, Integer, DateTime, ForeignKey, Text, UniqueConstraint,
                        Index, Date, Numeric, Double, Float, func, CheckConstraint)  # Asegúrate de incluir Float aquí
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime, date
from typing import Optional

class CargaTrabajo(db.Model):
    __tablename__ = 'carga_trabajo'

    id_carga: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_centro_trabajo: Mapped[int] = mapped_column(ForeignKey('centros_trabajo.id_centro_trabajo'), nullable=False)
    cantidad_horas_requeridas: Mapped[float] = mapped_column(Float, nullable=False)  # Aquí utilizas Float correctamente
    disponibilidad_recursos: Mapped[int] = mapped_column(Integer, nullable=False)

    def __repr__(self):
        return f"<CargaTrabajo {self.id_carga}>"
