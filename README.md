# Pyramid Cifar-10

Pyramid Cifar-10 é uma demo web para demonstrar como uma [rede neural convolucional (CNN)](http://cs231n.github.io/convolutional-networks/) pode categorizar imagens através de um modelo previamente treinado. [Cifar-10](https://www.cs.toronto.edu/~kriz/cifar.html) é o dataset usado no treinamento da rede e consiste em 60 mil imagens separadas em 10 categorias.

# Instalação

Consideramos que a instalação será feita em um "virtualenv"

1. Clone o repositório;

2. Faça a instalação das dependencias:

```
(env)$ pip install -r requirements.txt
```

# Ambiente de desenvolvimento

Para executar o servidor local:

```
(env)$ pserve development.ini
```

Por padrão o servidor local espera conexões na porta 6543

# Deploy em produção

O projeto já inclui os arquivos necessários para o deploy no Heroku. Estes arquivos são:

- Procfile
- run (bash)
- runapp.py
- production.ini

Este modelo de deploy **não é o ideal**, mas é uma forma simples de colocar o projeto em produção. Considere usar uma estratégia de deployment mais apropriada como o uso de nginx/gunicorn.

Para fazer o deploy (heroku):

- Se quiser manter um registro das consultas feitas no sistema, habilite o uso do Cloudinary:
  - Faça o cadastro no Cloudinary
  - Insira suas credenciais no arquivo .env do heroku ([saiba mais](https://devcenter.heroku.com/articles/heroku-local#copy-heroku-config-vars-to-your-local-env-file))
  - altere o parametro `use_cloudinary` no arquivo production.ini
- Faça o deploy com o comando ([saiba mais](https://devcenter.heroku.com/articles/git)):
```
(env)$ git push heroku master
```
 
O sistema automaticamente salvará as imagens e suas predições no Cloudinary se as credenciais estiverem presentes.

# Contribuições

Todas as contribuições são bem vindas! Não deixe de compartilhar dúvidas, sugestões, criticas e etc!
