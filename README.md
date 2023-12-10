# API LUKE

O Projeto da Luke é o início de um Workflow NoCode. Inicialmente o MVP feito neste projeto é referente à um processo muito comum em empresas que majoritariamente é realizado via Excel, o Processo de Reembolso.

Neste projeto a pessoa pode inputar informações referentes ao seu reembolso Data que foi feito o pagamento, Descrição do Reembolso, Categoria da despesa e também o Valor que foi gasto.

A ideia é que a partir do preenchimento desse formulário esse processo vire um WorkFlow que consiga ir direto para aprovação de o usuário que é entendido gestor da pessoa que é cliente do processo e também para o financeiro, tendo a aprovação de ambas as partes a pessoa recebe uma confirmação. Ou caso não tenha, a pessoa recebe um formulário acusando os reembolsos que não foram aceito e tendo a oportunidade de contestação.

Como foi dito anteriormente, a ideia é ter um ótimo WorkFlow tendo um processo como base. e que futuramente as pessoas possam construir seu próprio processo, tendo em vista que não todo processo de reembolso funciona de maneira igual em empresas.

O objetivo desse MVP é trazer a primeira funcionalidade da Luke preenchimento de reembolso padronizado sem que haja necessidade de envio de Planilhas de Excel. Então um processo que se torna pesado para o financeiro passa a se tornar mais leve. Usando um front-end para Luke e requisições HTTP via as APIs.

---

## Como executar

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte.

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.
