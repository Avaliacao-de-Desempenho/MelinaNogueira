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
    - Analisar pontos de melhoria.

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
### Objetivo: Melhorias na projeto
### Backlog Semanal (14/07 - 17/07)
- **14/07**
    - Implementar a validação de dados;
    - Fazer tratamento de erros.

- **15/07**
    - Dividir o main.py em funções;
    - Estudar Cloud Run, Cloud Build e postgres no Cloud SQL.

- **Resultado Esperado**
    - Melhorias implementadas com sucesso e estudo básico sobre os serviços Cloud.
    - Evolução: **90%**

- **Dúvidas do Aluno/Impedimentos Encontrados**
    - \<DÚVIDAS\>

- **Questões para o Aluno**
    - \<QUESTÕES\>

- **Respostas das Questões**
    - \<RESPOSTAS\>

- **Anotações**

 `Cloud Run`: serviço do Google Cloud que permite executar aplicações em containers diretamente na infraestrutura, sem precisar se preocupar com servidores, balanceamento de carga, nem escalabilidade pois o Cloud Run cuida de tudo isso automaticamente.

É recomendado para APIs, backends, webhooks e serviços leves que não precisam rodar 24h por dia.

Aplicação: você empacota sua API FastAPI em um container, faz o deploy no Cloud Run e recebe uma URL pública para consumir a API.
      
`Cloud Build`: ferramenta de CI/CD que automatiza todo o processo de build e deploy da sua aplicação. É comumente usada na criação de pipelines de build automatizadas, facilitando o desenvolvimento, testes e publicação de aplicações.

Recomendado para construir imagens Docker com seu código, rodar testes automaticamente, fazer o deploy direto no Cloud Run ou outros serviços, e integrar com GitHub para deploy automático a cada push.

Aplicação: você faz push no GitHub → o Cloud Build executa o cloudbuild.yaml → cria a imagem Docker → faz o deploy no Cloud Run.

`Cloud SQL com PostgreSQL`: serviço de banco de dados relacional gerenciado do Google Cloud, você pode usar PostgreSQL, MySQL ou SQL Server, e ele cuida de atualizações, backups, disponibilidade e escalabilidade.

Recomendado para armazenar os dados da sua aplicação, como usuários, produtos ou as notas fiscais extraídas pela API.

Aplicação: você cria uma instância PostgreSQL no Cloud SQL, conecta sua API FastAPI a ela, e a aplicação passa a ler/gravar os dados diretamente no banco na nuvem.

`Fluxo`:
1- Api 2- Cloud Build (docker e deploy) 3- Cloud Run (executar a api na nuvem) 4- Cloud SQL (api se conecta com o db no cloud).

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

- Google Cloud
    - https://cloud.google.com/run/docs/overview/what-is-cloud-run
    - https://cloud.google.com/build/docs
    - https://cloud.google.com/sql/docs/introduction

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
