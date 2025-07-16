from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }




class Usuario(db.Model):
    __tablename__ = 'usuario'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)

    favoritos_planetas = db.relationship("FavoritosPlanetas", back_populates="usuario", cascade="all, delete-orphan")
    favoritos_personajes = db.relationship("FavoritosPersonajes", back_populates="usuario", cascade="all, delete-orphan")

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            # do not serialize the password, its a security breach
        }
    



class FavoritosPlanetas(db.Model):
    __tablename__ = 'favoritos_planetas'
    id: Mapped[int] = mapped_column(primary_key=True)
    id_usuario: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    id_planetas: Mapped[str] = mapped_column(nullable=False)

    usuario = relationship("Usuario", back_populates="favoritos_planetas")
    planeta = relationship("Planetas", back_populates="favoritos")

    def serialize(self):
        return {
            "id": self.id,
            "id_usuario": self.id_usuario,
            "id_planetas": self.id_planetas,
            # do not serialize the password, its a security breach
        }
    



class Planetas(db.Model):
    __tablename__ = 'planetas'
    id: Mapped[int] = mapped_column(primary_key=True)
    planetas: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    clima: Mapped[str] = mapped_column(nullable=False)
    poblacion: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    favoritos = relationship("FavoritosPlanetas", back_populates="planeta", cascade="all, delete-orphan")

    def serialize(self):
        return {
            "id": self.id,
            "planetas": self.planetas,
            "clima": self.clima,
            "poblacion": self.poblacion,
            # do not serialize the password, its a security breach
        }
    



class FavoritosPersonajes(db.Model):
    __tablename__ = 'favoritos_personajes'
    id: Mapped[int] = mapped_column(primary_key=True)
    id_usuario: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    id_personajes: Mapped[str] = mapped_column(nullable=False)

    usuario = relationship("Usuario", back_populates="favoritos_personajes")
    personaje = relationship("Personajes", back_populates="favoritos")

    def serialize(self):
        return {
            "id": self.id,
            "id_usuario": self.id_usuario,
            "id_personajes": self.id_personajes,
            # do not serialize the password, its a security breach
        }
    



class Personajes(db.Model):
    __tablename__ = 'personajes'
    id: Mapped[int] = mapped_column(primary_key=True)
    personajes: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    color_de_cabello: Mapped[str] = mapped_column(nullable=False)
    color_de_ojos: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    favoritos = relationship("FavoritosPersonajes", back_populates="personaje", cascade="all, delete-orphan")

    def serialize(self):
        return {
            "id": self.id,
            "planetas": self.planetas,
            "color_de_cabello": self.color_de_cabello,
            "color_de_ojos": self.color_de_ojos,
            # do not serialize the password, its a security breach
        }
    