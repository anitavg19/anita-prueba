from app import db
from sqlalchemy import (BLOB, Table, Column, String, Boolean, Integer, DateTime, ForeignKey, Text, UniqueConstraint,
                        Index, Date, Numeric, Double, Float, func, CheckConstraint)  # Asegúrate de incluir Float aquí
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime, date
from typing import Optional

class CalendarioCapacidad(db.Model):
    __tablename__ = 'calendario_capacidad'

    id_calendario_capacidad: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    fecha: Mapped[Date] = mapped_column(Date, nullable=False)
    horas_laborables: Mapped[float] = mapped_column(Float, nullable=False)
    capacidad_restante: Mapped[float] = mapped_column(Float, nullable=False)

    def __repr__(self):
        return f"<CalendarioCapacidad {self.id_calendario_capacidad}>"
