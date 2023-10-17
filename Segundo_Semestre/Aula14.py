import cx_Oracle
import json

from Aula14_utils import *

login, senha = retorna_credenciais()

conn = conecta_ao_banco(login, senha)
