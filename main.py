from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

from data import produto_repo
from data import cliente_repo
from data import produto_repo
from data import categoria_repo

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

produto_repo.criar_tabela()
cliente_repo.criar_tabela()
produto_repo.criar_tabela()
categoria_repo.criar_tabela()

@app.get("/")
async def get_root():
    produtos = produto_repo.obter_todos()
    response = templates.TemplateResponse("index.html", {"request": {}, "produtos": produtos})
    return response


@app.get("/clientes")
async def get_clientes():
    clientes = cliente_repo.obter_todos()
    response = templates.TemplateResponse("clientes.html", {"request": {}, "clientes": clientes})
    return response

@app.get("/produtos")
async def get_():
    produtos = produto_repo.obter_todos()
    response = templates.TemplateResponse("produtos.html", {"request": {}, "produtos": produtos})
    return response

@app.get("/categorias")
async def get_categorias():
    categorias = categoria_repo.obter_todos()
    response = templates.TemplateResponse("categorias.html", {"request": {}, "categorias": categorias})
    return response

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)