## Amicci Teste

Olá,

Decidi realizar o desenvolvimento utilizando as classes do DRF, pois facilitam a leitura e fica mais fácil a avaliação.

Foram adicionados duas Actions no Github, a primeira rodas os testes, e se tudo estiver certo, roda a segunda actions que faz o build e envia para o Artifact Registry no GCP.

Fiz o Deploy em um cluster Kubernetes.

Você pode acessar o site neste endereço:

Verifique se a URL inicia com HTTP e não HTTPS.

> http://34.136.190.175:8000/api/demo/schema/docs/


Para executar o servidor localmente é necessário clonar o código:

> git clone https://github.com/VictorCarlquist/amicci-backend

Realizar o build:

> docker compose build

E executar o container:

> docker run -p 8000:8000 us-central1-docker.pkg.dev/alo-journey/alo-journey/backend-amicci

Para acessar a documentação da API, acesse:

> http://127.0.0.1:8000/api/demo/schema/docs/

Além disso, é possível realizer as requisições diretamente no browser

#### Teste a API:

Adicione um novo Retailer:

> POST /api/demo/retailer/

```json
{
  "name": "Retailer Teste"
}
```

Adicione um novo Vendor:

> POST /api/demo/vendor/

```json
{
  "name": "Vendor teste",
  "retailer": 1
}
```

Adicione uma nova categoria:

> POST /api/demo/category/:

```json
{
  "name": "Auto peças",
  "description": "Peças automotivas diversas"
}
```

Adicione um novo Briefing:

> POST /api/demo/briefing/

```json
{
  "retailer": 1,
  "category": 1,
  "name": "Briefing de teste",
  "responsible": "Victor",
  "release_date": "2024-04-25",
  "availabe": 2
}
```

## Teste Unitários

O código está com 96% de cobertura por testes. Os testes verificam a aplicação de ponta-a-ponta (end-to-end)



|Name |Stmts | Miss |Cover|
|-------------------------------------------------------------------------|----|-------|------|
|backend/__init__.py                                                      |  0 |     0 |  100%|
|backend/asgi.py                                                          |  4 |     4 |    0%|
|backend/settings.py                                                      | 20 |     0 |  100%|
|backend/urls.py                                                          |  3 |     0 |  100%|
|backend/wsgi.py                                                          |  4 |     4 |    0%|
|briefing/__init__.py                                                     |  0 |     0 |  100%|
|briefing/admin.py                                                        |  1 |     0 |  100%|
|briefing/apps.py                                                         |  4 |     0 |  100%|
|briefing/migrations/0001_initial.py                                      |  6 |     0 |  100%|
|briefing/migrations/0002_remove_retailer_vendor_vendor_retailer.py       |  5 |     0 |  100%|
|briefing/migrations/0003_rename_available_date_briefing_available.py     |  4 |     0 |  100%|
|briefing/migrations/0004_rename_available_briefing_availabe.py           |  4 |     0 |  100%|
|briefing/migrations/0005_alter_vendor_retailer.py                        |  5 |     0 |  100%|
|briefing/migrations/__init__.py                                          |  0 |     0 |  100%|
|briefing/models.py                                                       | 24 |     4 |   83%|
|briefing/serializers.py                                                  | 34 |     0 |  100%|
|briefing/tests.py                                                        |185 |     0 |  100%|
|briefing/urls.py                                                         |  4 |     0 |  100%|
|briefing/views.py                                                        | 38 |     0 |  100%|
|manage.py                                                                | 12 |     2 |   83%|
|-------------------------------------------------------------------------|----|-------|------|
|TOTAL                                                                    |357 |     14|   96%|
