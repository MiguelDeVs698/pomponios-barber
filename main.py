
from fastapi import FastAPI # Estou importando a classe FastAPI da biblioteca que acabei de instalar.

app = FastAPI() # Estou criando nossa aplicação. A variável app representa o backend do Pomponios Barber.


@app.get("/") # Aqui é definido uma rota ou seja: um endereço que o sistema disponibiliza para receber requesições
              # Get é o responsavel por solicitar informações ao servidor, e o / representa a pagina raiz da API
def inicio(): # Aqui é  criada uma função python chamada inicio
    return {"mensagem": "Bem-vindo ao Pomponios Barber!"} 

# Essa função devolve um dicionário Python que o FastAPI transforma em uma resposta JSON.