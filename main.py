from email.mime import base
import pickle
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Rota Raiz
@app.get("/")
def raiz():
    return {"Ola": "Mundo"}

# Criar model
class Usuario(BaseModel):
    #id: int
    nome: str
    numero: int

# Criar base de dados

filename = 'dogs'
# outfile = open(filename,'wb')

# pickle.dump(dogs_dict,outfile)
# outfile.close()

infile = open(filename,'rb')
new_dict = pickle.load(infile)
infile.close()

base_de_dados= []

for i in new_dict.keys():
  for j in new_dict.values():
      base_de_dados.append(Usuario(nome=i, numero=j)) 

print(base_de_dados)

"""  base_de_dados = [
Usuario(nome=i, numero=j),
Usuario(nome=i, numero=j)
] """

# Rota Get All
@app.get("/usuarios")
def get_todos_os_usuarios():
    return base_de_dados

# Rota Get Id
@app.get("/usuarios/{nome_usuario}")
def get_usuario_usando_nome(nome_usuario: str):
    for usuario in base_de_dados:
        if(usuario.nome == nome_usuario):
            return usuario
    
    return {"Status": 404, "Mensagem": "Não encontrou usuario"}

# Rota Insere
@app.post("/usuarios")
def insere_usuario(usuario: Usuario):
    # criar regras de negocio
    base_de_dados.append(usuario)
    return usuario
