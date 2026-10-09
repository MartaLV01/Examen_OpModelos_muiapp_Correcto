from typing import Literal
from pydantic import BaseModel, ConfigDict, Field, field_validator


class Entrada(BaseModel):
    # DONE -> TODO
    id_paquete: str
    peso_kg: float = Field(ge=0, le=30)
    distancia_km: float = Field(ge=0, le=200)
    #pass


    #Elimino los espacios inicio/final del id
    @field_validator("id_paquete")
    @classmethod
    def validar_id(cls, id_paquete):
        id_paquete_strip = id_paquete.strip()
        return id_paquete_strip

    #redondeo a un decimal
    @field_validator("peso_kg")
    @classmethod
    def validar_peso(cls, peso_kg):
        peso_kg_round = round(peso_kg, 1)
        return peso_kg_round


class Salida(BaseModel):
    # DONE->  TODO
    id_paquete: str
    categoria: Literal["normal", "urgente"]
    confianza: float = Field(ge=0, le=1)

    #pass
