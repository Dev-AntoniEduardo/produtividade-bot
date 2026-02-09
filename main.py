from fastapi import FastAPI
from app.routes.health import router as health_router

# Cria a aplicação FastAPI (objeto principal do backend)
app = FastAPI(
    title="Produtividade Bot API",
    version="0.1.0"
)

# Inclui as rotas de health
app.include_router(health_router)

# Rota simples para confirmar que a API está rodando
@app.get("/")
def root():
    return {"status": "API rodando com sucesso 🚀"}
