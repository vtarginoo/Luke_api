from flask_openapi3 import OpenAPI, Info, Tag
from sqlalchemy.exc import IntegrityError
from flask_cors import CORS
from flask import redirect

from model import Session, Repay
from schemas import *


info = Info(title="Repay API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)


# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
repay_tag = Tag(name="Repay", description="Adição, visualização e remoção de repay à base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


############################

######## Rota de Adição de Reembolso

############################



@app.post('/repay', tags=[repay_tag],
          responses={"200": RepayViewSchema, "409": ErrorSchema, "400": ErrorSchema})

def add_repay(form: RepaySchema):
    """Adiciona um novo Reembolso à base de dados

    Retorna uma representação dos Repays.
    """
    repay = Repay(
        date_insert = form.date_insert,
        repay=form.repay,
        category=form.category,
        value=form.value )

    try:
        # criando conexão com a base
        session = Session()
        # adicionando repay
        session.add(repay)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        return apresenta_repay(repay), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Repay de mesmo nome já salvo na base :/"
        return {"message": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        return {"message": error_msg}, 400


############################

######## Rota de Get List

############################


@app.get('/repay_list', tags=[repay_tag],
         responses={"200": ListagemRepaySchema, "404": ErrorSchema})

def get_repay_list():
    """Faz a busca por todos os Reeembolsos cadastrados

    Retorna uma representação da listagem de repay.
    """
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    repay_list = session.query(Repay).all()

    if not repay_list:
        # se não há repay cadastrados
        return {"repay_list": []}, 200
    else:
        # retorna a representação de repay
        print(repay_list)
        return apresenta_repay_list(repay_list), 200



############################

######## Rota de Busca

############################

@app.get('/repay', tags=[repay_tag],
         responses={"200": RepayViewSchema, "404": ErrorSchema})

def get_repay(query: RepayBuscaSchema):
    """Faz a busca por um Reembolso a partir da Descrição (repay) do Reembolso

    Retorna uma representação do repay.
    """
    repay_name = query.repay_name
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    repay = session.query(Repay).filter(Repay.repay == repay_name).first()

    if not repay:
        # se o repay não foi encontrado
        error_msg = "Repay não encontrado na base :/"
        return {"message": error_msg}, 404
    else:
        # retorna a representação de repay
        return apresenta_repay(repay), 200


############################

######## Rota de Delete

############################
@app.delete('/repay', tags=[repay_tag],
            responses={"200": RepayDelSchema, "404": ErrorSchema})
def del_repay(query: RepayBuscaSchema):
      
      
    """Deleta um Reembolso a partir da Descrição(repay) informado

    Retorna uma mensagem de confirmação da remoção.
    """
    repay_name = query.repay_name
    app.logger.info(f"Attempting to delete Repay with name: {repay_name}")
    
    # criando conexão com a base
    session = Session()
    
    # Busca o Repay antes de excluir
    repay_to_delete = session.query(Repay).filter(Repay.repay == repay_name).first()

    if repay_to_delete:
        # Salvando o nome do Repay antes de excluí-lo
        repay_id = repay_to_delete.id

        # fazendo a remoção
        session.delete(repay_to_delete)
        session.commit()

        # retorna a representação da mensagem de confirmação
        return {"message": "Repay removido", "id": repay_id, "repay": repay_name}
    else:
        # se o repay não foi encontrado
        error_msg = "Repay não encontrado na base :/"
        return {"message": error_msg}, 404