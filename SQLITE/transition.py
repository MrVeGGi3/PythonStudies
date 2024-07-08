import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meubanco.db")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

try:
    cursor.execute("INSERT INTO clientes(nome, email) VALUES (?,?)", ("Teste 1","teste1@gmail.com"))
    cursor.execute("INSERT INTO clientes(id, nome, email) VALUES (?,?,?)", (2 ,"Teste 2","teste2@gmail.com"))
except Exception as exc:
    print(f"Erro!:{exc}")
    conexao.rollback()
finally:
    conexao.commit()