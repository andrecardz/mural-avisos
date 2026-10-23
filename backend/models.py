from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field

# Os limites acompanham os campos do formulário em index.html.
Prioridade = Literal["normal", "importante"]


class AvisoEntrada(BaseModel):
    """Contrato do JSON recebido no POST."""

    titulo: str = Field(min_length=4, max_length=60)
    mensagem: str = Field(min_length=10, max_length=300)
    autor: str = Field(min_length=3, max_length=50)
    prioridade: Prioridade


class AvisoSaida(AvisoEntrada):
    """Contrato da resposta, com os campos gerados pela API."""

    id: int
    publicado_em: datetime
