import uvicorn
from infraestrutura.api.usuario_api import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)