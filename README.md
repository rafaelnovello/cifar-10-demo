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
- production-template.ini

Este modelo de deploy **não é o ideal**, mas é uma forma simples de colocar o projeto em produção. Considere usar uma estratégia de deployment mais apropriada como o uso de nginx/gunicorn.

Para fazer o deploy:

- Altere o arquivo production-template.ini para production.ini
- Se quiser manter um registro das consultas feitas no sistema, habilite o uso do Cloudinary:
  - Faça o cadastro no Cloudinary
  - Insira suas credenciais no arquivo production.ini
  - Remova os comentários

O sistema automaticamente salvará as imagens e suas predições no Cloudinary se as credenciais estiverem presentes.

# Contribuições

Todas as contribuições são bem vindas! Não deixe de compartilhar dúvidas, sugestões, criticas e etc!
