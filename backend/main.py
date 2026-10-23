from datetime import datetime

from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from models import AvisoEntrada, AvisoSaida

app = FastAPI(title="Mural de Avisos Acadêmicos", version="1.0.0")

# Libera o front-end servido na porta 5500 a chamar esta API.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500", "http://127.0.0.1:5500"],
    allow_methods=["*"],
    allow_headers=["*"],
)

avisos: list[AvisoSaida] = []


@app.get("/api/avisos", response_model=list[AvisoSaida])
def listar_avisos():
    return avisos


@app.post(
    "/api/avisos",
    response_model=AvisoSaida,
    status_code=status.HTTP_201_CREATED,
)
def publicar_aviso(dados: AvisoEntrada):
    aviso = AvisoSaida(
        id=len(avisos) + 1,
        publicado_em=datetime.now(),
        **dados.model_dump(),
    )
    avisos.append(aviso)
    return aviso
