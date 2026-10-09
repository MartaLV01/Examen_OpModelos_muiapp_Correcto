import csv
from pathlib import Path
import joblib
from .contracts import Entrada, Salida


def leer_csv(ruta: Path) -> list[Entrada]:
    # DONE-> TODO
    reader_csv = []
    with open(ruta, "r") as f:
        reader_csv = csv.DictReader(f)

    for row in reader_csv:
        # cada row debe pasar el contrato, se llama a contracts
        # si error lanza ValueError
        try:
            Entrada(row)
        except:
            raise ValueError

    #raise NotImplementedError


def preprocesar(entrada: Entrada) -> list[float]:
    # DONE TODO
    #Entrada es id, kg y distancia de una fila, no quiero id
    #El round lo hice en mi contract
    contenido = []
    contenido.append(entrada.peso_kg)
    contenido.append(entrada.distancia_km)
    return contenido
    #raise NotImplementedError


def cargar_modelo(ruta: Path):
    # TODO

    modelo = joblib.load(ruta)
    modelo.prededir(modelo)

    raise NotImplementedError


def predecir(entrada: Entrada, modelo) -> Salida:
    # TODO
    raise NotImplementedError


def guardar_csv(resultados: list[Salida], ruta: Path) -> None:
    # TODO
    raise NotImplementedError


def ejecutar(entrada: Path, modelo: Path, salida: Path) -> None:
    # TODO
    raise NotImplementedError


if __name__ == "__main__":
    ejecutar(
        Path("data/raw/paquetes.csv"),
        Path("models/modelo.joblib"),
        Path("resultados.csv"),
    )
