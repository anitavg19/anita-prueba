from app import db
from sqlalchemy import (BLOB, Table, Column, String, Boolean, Integer, DateTime, ForeignKey, Text, UniqueConstraint,
                        Index, Date, Numeric, Double, func, CheckConstraint)
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime, date
from typing import Optional

class CalendarioDeProduccion(db.Model):
    __tablename__ = 'calendario_de_produccion'

    id = db.Column(db.Integer, primary_key=True)
    semana = db.Column(String(20), nullable=False)
    capacidad_disponible = db.Column(Integer, nullable=False)
    produccion_programada = db.Column(Integer, nullable=False)

    def __repr__(self):
        return f'<CalendarioDeProduccion Semana={self.semana}>'
