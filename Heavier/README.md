# Heavier
## Faça o download dos vídeos do Heavy-R de forma automática!

### Descrição:

##### Este é um simples programa que possui a função de baixar vídeos do site Heavy-R de forma automática, utilizando uma lista de ID's disponível através de uma URL externa ou de forma manual, inserindo as ID's como argumento para o programa.

##### Para que o modo automático funcione, ***é necessário uma URL válida para a lista de ID's no arquivo de configurações!***

##### O programa cria uma pasta no mesmo diretório que está sendo executado e nele cria os diretórios para os vídeos que irá baixar. Você pode escolher o nome do diretório raiz pelo arquivo de configurações do programa ```configs.json```.

##### Ao executar o programa sem qualquer parâmetro ou argumentos, ele irá tentar obter a lista de ID's e, através dessas ID's, irá baixar os vídeos do Heavy-R para a pasta definida no arquivo de configurações.

##### Os vídeos serão baixados em formato '.mp4', com o nome do vídeo original.

##### Aqui estão os possíveis argumentos que poderão ser inseridos na hora de executar o programa e a explicação de cada campo no arquivo de configurações:

    Uso: ./Heavier.py [Argumento] [ID]
    ----------------------------------
    
    Argumentos:
    -----------
    '-h' ou '--help':    Mostra a tela de ajuda
    '-i' ou '--id':      Utiliza a ID inserida como argumento no programa
    
    Arquivo de configurações:
    -------------------------
    list_id_url          Endereço da lista de ID's dos vídeos em formato raw (texto puro)
    template_url_page    Template da página do vídeo
    video_dir            Diretório onde será armazenado os vídeos
    download_max_tries   Número de tentativas máximas para baixar o vídeo em caso de erro

### Instalação:
##### Recomenda-se o uso de uma virtualenv para rodar o programa. Para isso, basta criar uma env e instalar os pacotes descritos no arquivo ```requirements.txt``` e ```requirements-test.txt```. Veja no exemplo abaixo:
```bash
mkdir heavier-env
virtualenv heavier-env --python=python3.5
source heavier-env/bin/activate
pip install -r requirements.txt -r requirements-test.txt
```

##### Após a instalação dos pacotes, basta iniciar o programa:
```bash
python Heavier.py
```

### Testes:
##### Para rodar os testes do programa, certifique-se de ter instalado os pacotes no arquivo ```requirements-test.txt``` e execute o seguinte comando:
```bash
py.test
```
