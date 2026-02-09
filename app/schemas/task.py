from pydantic import BaseModel
from typing import Optional


class TaskCreate(BaseModel):
    """
    Dados que o usuário envia para CRIAR uma tarefa.
    Ex: title e description.
    """
    title: str
    description: Optional[str] = None


class Task(TaskCreate):
    """
    Modelo completo de uma tarefa (o que a API retorna).
    Herdamos TaskCreate para reaproveitar title/description.
    """
    id: int
    completed: bool = False
