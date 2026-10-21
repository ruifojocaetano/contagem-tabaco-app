"""Gera funcionarias.json (lista de nomes para escolher na app) a partir de Funcionarias.xlsx (um nome por linha, sem cabeçalho).

Uso: python gerar_funcionarias.py [Funcionarias.xlsx]
O ficheiro fica fora do git (nomes de pessoas); sem ele a app deixa escrever o nome à mão.
"""
import json
import sys
from pathlib import Path

import pandas as pd

ORIGEM = Path(__file__).with_name("Funcionarias.xlsx")
SAIDA = Path(__file__).with_name("funcionarias.json")


def main():
    f = Path(sys.argv[1]) if len(sys.argv) > 1 else ORIGEM
    d = pd.read_excel(f, header=None, usecols=[0])
    nomes = sorted({" ".join(str(n).split()).upper() for n in d[0].dropna() if str(n).strip()})
    SAIDA.write_text(json.dumps(nomes, ensure_ascii=False), encoding="utf-8")
    print(len(nomes), "nomes ->", SAIDA)


if __name__ == "__main__":
    main()
