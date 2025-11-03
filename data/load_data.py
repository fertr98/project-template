"""
Módulo: load_data.py
Descripción: funciones para cargar y mostrar datos desde archivos CSV o rutas externas.
"""

import pandas as pd
from pathlib import Path


def load_csv(file_path: str) -> pd.DataFrame:
    """
    Carga un archivo CSV y devuelve un DataFrame de pandas.
    
    Args:
        file_path (str): ruta al archivo CSV.
    
    Returns:
        pd.DataFrame: contenido del CSV cargado.
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"No se encontró el archivo: {file_path}")
    
    df = pd.read_csv(path)
    print(f"✅ Cargado correctamente: {file_path} ({df.shape[0]} filas, {df.shape[1]} columnas)")
    return df


if __name__ == "__main__":
    # Ejemplo de uso (solo de prueba)
    example_path = "data/raw/ejemplo.csv"
    print("Ejecutando ejemplo de carga de datos...")
    try:
        df = load_csv(example_path)
    except FileNotFoundError:
        print("⚠️ No se encontró el archivo de ejemplo. Crea 'data/raw/ejemplo.csv' para probar.")
