from app import db
from sqlalchemy import (BLOB, Table, Column, String, Boolean, Integer, DateTime, ForeignKey, Text, UniqueConstraint,
                        Index, Date, Numeric, Double, func, CheckConstraint)
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime, date
from typing import Optional

class Persona(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    numero_identidad: Mapped[str] = mapped_column(String(20))
    nombre: Mapped[str] = mapped_column(String(64))
    apellidos: Mapped[str] = mapped_column(String(64))
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    correo: Mapped[str] = mapped_column(String(120))
    cantidad_mascotas = db.Column(db.Integer, nullable=False)
    semana_inicio: Mapped[str] = mapped_column(String(10))
    lugar_id: Mapped[int] = mapped_column(Integer, ForeignKey('lugar.id'))
    lugar: Mapped['Lugar'] = relationship(back_populates='personas')



    def __repr__(self):
        return f'<Persona {self.nombre} {self.apellidos}>'
