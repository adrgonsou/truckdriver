# Teste Backend

### Cenário
Em um terminal chegam para carga e descarga cerca de mil caminhões por dia, nem todos os caminhões saem do terminal carregados para voltar a seu lugar de origem. Muitos dos nossos amigos caminhoneiros são motoristas autônomos e alguns deles tem seu próprio veiculo.

### Tipos de Caminhões

| Tipos de caminhões     | Código |
|------------------------|--------| 
| Caminhão 3/4           | 1      |
| Caminhão Toco          | 2      |
| Caminhão Truck         | 3      |
| Carreta Simples        | 4      |
| Carreta Eixo Extendido | 5      |

### Desafio
Precisamos criar uma api para para cadastrar os motoristas que chegam nesse terminal e saber mais informações sobre eles. 
- Precisamos saber nome, idade, sexo, se possui veiculo, tipo da ​ CNH​, se está carregado, tipo do veiculo que está dirigindo.
- Precisamos saber a origem e destino de cada caminhoneiro. Será necessário pegar a latitude e longitude de cada origem e destino.
- Precisamos de um método para consultar todos os motoristas que não tem carga para voltar ao seu destino de origem.
- Precisamos saber quantos caminhões passam carregados pelo terminal durante o dia, semana e mês.
- Precisamos saber quantos caminhoneiros tem veiculo próprio.
- Mostrar uma lista de origem e destino agrupado por cada um dos tipos.
- Será necessário atualizar os registros dos caminhoneiros.
- Criar testes unitários para validar

### Requisitos Mínimos
* Criar um repositório publico para que possamos avaliar os seus códigos (​ Github​ , ​ GitLab​ , etc...).
* O projeto deve conter um arquivo ​ README​ explicando como o mesmo funciona e explicando como fazer para rodar a aplicação.
* Você pode utilizar a linguagem que preferir, porém será considerado um diferencial se for feito em Python​.
* Siga os verbos do HTTP.
* O padrão de resposta das apis devem ser em ​ JSON​ .
* Fique a vontade para adicionar os recursos que achar necessário.


### Como rodar a aplicação
* Instalar o [Docker] seguindo os procedimentos informados de acordo com seu sistema operacional
* Baixar o código fonte do projeto

### Utilizando Docker Compose
Na pasta da aplicação executar os comandos:
```
docker-compose build
docker-compose up
```
<img src="images/Homepage.png" align="center"/>

### Utilizando Docker
Na na pasta do aplicaçao executar os comandos:
(*repositório do [Docker Hub]*)
```
**docker build** -t "adgonsou/truckpad:latest" . 
docker push adgonsou/truckpad:latest
docker run -p 5000:5000 adgonsou/truckpad:latest
```

<img src="images/Homepage.png" align="center"/>

**Teste se a aplicação subiu com curl ou browser:**
* curl -v "http://localhost:5000/"
* Ou acessando o link no navegador http://localhost:5000



### Healthcheck
WT??????

### Autoria
Adriano Gonçalves de Souza
adriano.g.souza@gmail.com

[Docker]: https://docs.docker.com/install/
[Docker Hub]: https://hub.docker.com/
[here]: https://medium.com/@daniel.carlier/how-to-build-a-simple-flask-restful-api-with-docker-compose-2d849d738137
