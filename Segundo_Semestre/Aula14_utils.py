import json

def retorna_credenciais():
    path = r"C:\Users\logonrmlocal\Desktop\COMPUTATIONAL-THINKING-USING-PYTHON\Segundo_Semestre\credenciais.json"

    with open(path, "r") as arquivo:
        dados = json.load(arquivo)
        login = dados["login"]
        senha = dados["senha"]

    return login, senha

def conecta_ao_banco(host="oracle.fiap.com.br", port=1521, sid="ORCL"):
    dsn = cx_Oracle.makedsn(host=host, port=port, sid=sid)
    conn = cx_Oracle.connect(user=login, password=senha, dsn=dsn)
    return conn
