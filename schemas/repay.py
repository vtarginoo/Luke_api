from pydantic import BaseModel,validator,ValidationError, constr
from typing import Optional, List
from model.repay import Repay
from datetime import datetime


class RepaySchema(BaseModel):
    """ Define como um reembolso a ser inserido deve ser representado
    """
    date_insert: constr(strip_whitespace=True)  # Remova espaços em branco extras
    repay: str = "Metrô"
    category: str = "Transporte"
    value: float = 6.50

    @validator("date_insert")
    def validate_date_insert(cls, value):
        try:
            # Tenta converter a string para um objeto datetime
            datetime.strptime(value, "%d/%m/%Y")
        except ValueError:
            # Se houver um erro, levanta uma exceção de validação
            raise ValidationError("Data deve estar no formato DD/MM/YYYY")

        return value

class ListagemRepaySchema(BaseModel):
    """ Define como uma listagem de produtos será retornada.
    """
    repay_list:List[RepaySchema]




def apresenta_repay_list(repay_list: List[Repay]):
    """ Retorna uma representação do repay seguindo o schema definido em
        RepayViewSchema.
    """

    result = []
    for repay in repay_list:
        
        formatted_date1 = repay.date_insert.strftime("%d/%m/%Y")
        
           # Formatar o retorno do Banco de dados para o front end 
        result.append({
            "date_insert": formatted_date1,
            "repay": repay.repay,
            "category": repay.category,
            "value": repay.value,
        })
    return {"repay_list": result}


class RepayViewSchema(BaseModel):
    """ Define como um Repay será retornado. 
    """
    id: int = 1
    date_insert: constr(strip_whitespace=True)  # Remova espaços em branco extras
    repay: str = "Metrô"
    category: str = "Transporte"
    value: float = 6.50

    @validator("date_insert")
    def validate_date_insert(cls, value):
        try:
            # Tenta converter a string para um objeto datetime
            datetime.strptime(value, "%d/%m/%Y")
        except ValueError:
            # Se houver um erro, levanta uma exceção de validação
            raise ValidationError("Data deve estar no formato DD/MM/YYYY")

        return value
    


########### Rotas Importantes para o DEL


class RepayBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no Id do Repay.
    """
    repay_name: str = "Descrição"

class RepayDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    message: str
    id: int
    repay: str

def apresenta_repay(repay: Repay):
    """ Retorna uma representação do produto seguindo o schema definido em
        RepayViewSchema.
    """

    formatted_date = repay.date_insert.strftime("%d/%m/%Y")
    
    return {
        "id": repay.id,
        "date_insert": formatted_date,
        "repay": repay.repay,
        "category": repay.category,
        "value": repay.value,
    }
