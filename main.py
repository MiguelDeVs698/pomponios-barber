
from fastapi import FastAPI, HTTPException # Estou importando a classe FastAPI da biblioteca que acabei de instalar.

app = FastAPI() # Estou criando nossa aplicação. A variável app representa o backend do Pomponios Barber.

from pydantic import BaseModel, Field

@app.get("/")     # Aqui é definido uma rota ou seja: um endereço que o sistema disponibiliza para receber requesições
                  # Get é o responsavel por solicitar informações ao servidor, e o / representa a pagina raiz da API
def inicio():     # Aqui é  criada uma função python chamada inicio
    return {"mensagem": "Bem-vindo ao Pomponios Barber!"} 

# Essa função devolve um dicionário Python que o FastAPI transforma em uma resposta JSON.

servicos = [
    {"id": 1, "nome": "Corte", "preco": 25.00, "duracao": 40},
    {"id": 2, "nome": "Sobrancelha", "preco": 5.00, "duracao": 5},
    {"id": 3, "nome": "Bigode e cavanhaque", "preco": 5.00, "duracao": 5},
    {"id": 4, "nome": "Barba completa", "preco": 10.00, "duracao": 7}
]

@app.get("/servicos")
def listar_servicos():
    return servicos


@app.get("/servicos/{servico_id}")
def buscar_servico(servico_id: int):
    for servico in servicos:
        if servico["id"] == servico_id:
            return servico

    raise HTTPException(
        status_code=404,
        detail="Serviço não encontrado"
    )


class NovoServico(BaseModel):
    nome: str
    preco: float = Field(gt=0)
    duracao: int = Field(gt=0)


@app.post("/servicos", status_code=201)
def cadastrar_servico(novo_servico: NovoServico):
    novo_id = max(servico["id"] for servico in servicos) + 1

    servico = {
        "id": novo_id,
        "nome": novo_servico.nome,
        "preco": novo_servico.preco,
        "duracao": novo_servico.duracao
    }

    servicos.append(servico)

    return servico
