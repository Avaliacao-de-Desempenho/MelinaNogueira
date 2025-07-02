## SEMANA 1: Extração de NFe com API
### Objetivo: Configurar ambiente local, estruturar o projeto e validar o funcionamento básico da API
**02/07 - 04/07**
- **Backlog Semanal**
    - Organizar documentação inicial e plano de projeto.
    - Baixar e instalar dependências (FastAPI, SQLAlchemy, httpx, etc.).
    - Criar a estrutura base do projeto com app/, Dockerfile, docker-compose.yml, .env, etc.
    - Testar execução da API localmente e via Docker (uvicorn).
    - Configurar o ambiente com venv e listar pacotes no requirements.txt.

- **Resultado Esperado**
    - Projeto estruturado, com FastAPI rodando localmente via Docker e documentação inicial pronta.
    - Evolução: 35% - 100%
- **Dúvidas do Aluno/Impedimentos Encontrados**
    - \<DÚVIDAS\>
- **Questões para o Aluno**
    - \<QUESTÕES\>
- **Respostas das Questões**
    - \<RESPOSTAS\>
---
**Anotações**
1. Enviar a imagem (swagger) 2. Receber a imagem 3.Extrair dados (api gemini) 4. Armazenar imagem.

---
## SEMANA 2: Extração de NFe com API
### Objetivo: \<OBJETIVO DA SEMANA\>
**07/07 - 11/07**
- **Backlog Semanal**
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
## SEMANA 3: Extração de NFe com API
### Objetivo: \<OBJETIVO DA SEMANA\>
**14/07 - 17/07**
- **Backlog Semanal**
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
Criar uma API em Python, usando FastAPI, que receba umaimagem (.jpg, .jpeg, .png) ou um PDF de uma Nota Fiscal;salve o Valor Total, Data de Emissão e CNPJ no banco dedados Postgres e retorne os mesmos campos em formato json.
A API e o banco de dados devem rodar localmente em dockere o projeto como um todo deve poder ser iniciado usando o"docker compose". Também é necessário que os dadospersistam mesmo que os dockers sejam pausados oudesligados.
O ambiente local deve estar num ambiente virtual, criadocom o "venv", e os pacotes devem estar listados noarquivo "requirements.txt".
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
    **07/07 (segunda)** - report de progresso eimpedimentos  
    **10/07 (quinta)** - report de progresso eimpedimentos  
    **15/07 (terça)** - report de progresso eimpedimentos  
    **17/07 (quinta, apresentação final)** - apresentaçãodo resultado final  
- Documentar código e processos durante todo o projeto  
- Fazer update diário do relatório  
- Fazer update diário do código  
- O repositório deve ter um nome padrão: \<NOME DOALUNO\>-AVALIAÇÃO
## Avaliação
- Evolução técnica com base nos resultados semanais
- Autonomia no desenvolvimento e impedimentos
- Organização (repositório, report, documentação, git)