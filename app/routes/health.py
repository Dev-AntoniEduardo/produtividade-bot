from fastapi import APIRouter

# Criamos um router para agrupar rotas de "health"
router = APIRouter()

@router.get("/health")
def health_check():
    """
    Rota de verificação da API.
    Serve para saber se o backend está online.
    """
    return {"status": "ok"}
