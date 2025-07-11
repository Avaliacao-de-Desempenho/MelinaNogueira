## SEMANA 1: Extração de NFe com API  
### Objetivo: Configurar ambiente local, estruturar o projeto e validar o funcionamento básico da API  

### Backlog Semanal (02/07 - 04/07)
- **02/07**
    - Organizar documentação inicial e plano de projeto; 
    - Baixar e instalar dependências (FastAPI, SQLAlchemy, httpx, etc.); 
    - Criar a estrutura base do projeto com app/, Dockerfile, docker-compose.yml, .env, etc.

- **03/07**
    - Testar execução da API localmente e via Docker (uvicorn).

- **04/07**
    - Integrar API do Gemini para extração de dados da nota.


- **Resultado Esperado**
    - Projeto estruturado, com FastAPI rodando localmente e via Docker, extração de dados com Gemini;
    - Evolução: **100%**;
    - Equivalente a **80%** do projeto total.

- **Dúvidas do Aluno/Impedimentos Encontrados**
    - \<DÚVIDAS\>
- **Questões para o Aluno**
    - \<QUESTÕES\>
- **Respostas das Questões**
    - \<RESPOSTAS\>

- **Anotações**
    1. Enviar a imagem;  
    2. Extrair dados com API Gemini;
    3. Retornar dados em JSON;
    4. Salvar dados num banco;
    
    API funcionando, integração com Gemini e Docker prontos.

## SEMANA 2: Extração de NFe com API
### Objetivo: Armazenar as informações extraídas em banco PostgreSQL de forma persistente
### Backlog Semanal (07/07 - 11/07)
- **07/07**
    - Criar banco PostgreSQL com persistência usando volumes Docker;
    - Criar endpoint `/upload` que insere os dados extraídos no banco de dados;
    - Ajustar parsing de datas da resposta do Gemini.

- **08/07**
    - Validar persistência após reinício dos containers Docker;
    - Finalizar e revisar documentação.

- **10/07**
    - Adicionar coluna `data_registro`, para saber a data e horário que os dados foram armazenados no banco de dados.

- **11/07**
    - Analisar [pontos de melhoria](#anotações).

- **Resultado Esperado**
    - Dados extraídos da NFe sendo salvos corretamente no banco PostgreSQL e persistindo.
    - Evolução: **100%**
    - Equivalente a **100%** do projeto total.

- **Dúvidas do Aluno/Impedimentos Encontrados**
    - \<DÚVIDAS\>

- **Questões para o Aluno**
    - \<QUESTÕES\>

- **Respostas das Questões**
    - \<RESPOSTAS\>

- **Anotações**
    - Validação de dados: validar os dados retornados do gemini antes de inserir no banco de dados;
    - Tratamento de erros: melhorar o `try/except`, detalhar melhor o erro;
    - Separar o `main.py` em funções menores, exemplo: extração, conversão, inserção e validações.

## SEMANA 3: Extração de NFe com API
### Objetivo: \<OBJETIVO DA SEMANA\>
**14/07 - 17/07**
- **Backlog Semanal**
    - Data de inserção 
    - \<QUEBRAR O OBJETIVO DA SEMANA EM PARTES MENORES\>
- **Resultado Esperado**
    - \<QUAL ENTREGÁVEL SERÁ PRODUZIDO QUANDO O OBJETIVOFOR ALCANÇADO (FINAL DA SEMANA)\>
    - Evolução: \<0% - 100%\>
- **Dúvidas do Aluno/Impedimentos Encontrados**
    - \<DÚVIDAS\>
- **Questões para o Aluno**
    - \<QUESTÕES\>
- **Respostas das Questões**
    - \<RESPOSTAS\>
---
## Descrição do Projeto
Criar uma API em Python, usando FastAPI, que receba uma imagem (.jpg, .jpeg, .png) ou um PDF de uma Nota Fiscal, salve o Valor Total, Data de Emissão e CNPJ no banco de dados Postgres e retorne os mesmos campos em formato json.
A API e o banco de dados devem rodar localmente em docker e o projeto como um todo deve poder ser iniciado usando o"docker compose". Também é necessário que os dados persistam mesmo que os dockers sejam pausados ou desligados.
O ambiente local deve estar num ambiente virtual, criado com o "venv", e os pacotes devem estar listados no arquivo "requirements.txt".
## Stack
- Python
- Postgres
- FastAPI
- Docker
    - Dockerfile
    - Docker compose
- Gemini
    - API
## Referências
- Python
    - https://www.python.org/downloads/
    - https://www.python.org/doc/
    - https://www.alura.com.br/artigos/lidando-com-datas-e-horarios-no-python
- Repositório de pacotes python
    - https://pypi.org/
- Ambiente virtual
    - https://docs.python.org/pt-br/3/library/venv.html
- Docker
    - Dockerfile, build de imagem e rodar container:https://docs.docker.com/build/concepts/dockerfile/
    - Docker compose: https://docs.docker.com/compose/
- FastAPI
    - https://fastapi.tiangolo.com/tutorial/
    - https://fastapi.tiangolo.com/tutorial/first-steps#step-4-define-the-path-operation-function
- Banco de dados
    - https://www.postgresql.org/
    - https://pypi.org/project/SQLAlchemy/
    - https://pypi.org/project/psycopg/
- Gemini
    - https://aistudio.google.com/apikey
    - https://ai.google.dev/gemini-api/docs/image-understanding?hl=pt-br
    - https://ai.google.dev/api/files?hl=pt-br#files_create_image-PYTHON 
## Passo a Passo do Projeto
1. Fazer o setup do ambiente
    - criar repositório
    - instalar dependências
    - instalar docker
1. Criar api do projeto com o FastAPI
1. Fazer a extração de campos com Gemini
1. Adicionar integração com banco de dados
## Benchmarks
- Semana 1
    - setup inicial: repositório, pacotes, docker
    - testar fastapi
    - testar gemini
- Semana 2
    - desenvolver api para fazer extração de campos
- Semana 3
    - integrar com banco de dados
    - finalizar documentação
    - apresentação final
## Diretivas
- **Reuniões**  
    **07/07 (segunda)** - report de progresso e impedimentos  
    **10/07 (quinta)** - report de progresso e impedimentos  
    **15/07 (terça)** - report de progresso e impedimentos  
    **17/07 (quinta, apresentação final)** - apresentaçãodo resultado final  
- Documentar código e processos durante todo o projeto  
- Fazer update diário do relatório  
- Fazer update diário do código  
- O repositório deve ter um nome padrão: \<NOME DOALUNO\>-AVALIAÇÃO
## Avaliação
- Evolução técnica com base nos resultados semanais
- Autonomia no desenvolvimento e impedimentos
- Organização (repositório, report, documentação, git)
