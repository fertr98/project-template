"""
Test de ejemplo para el módulo src/data/load_data.py
"""

import pytest
import pandas as pd
from src.data.load_data import load_csv
from pathlib import Path


def test_load_csv_file_not_found():
    """Debe lanzar FileNotFoundError si el archivo no existe"""
    with pytest.raises(FileNotFoundError):
        load_csv("data/raw/no_existe.csv")


def test_load_csv_ok(tmp_path):
    """Debe cargar correctamente un CSV válido"""
    # Creamos un CSV temporal
    csv_path = tmp_path / "sample.csv"
    df = pd.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"]})
    df.to_csv(csv_path, index=False)

    # Cargamos el CSV
    loaded = load_csv(csv_path)

    # Comprobamos el contenido
    assert loaded.equals(df)
