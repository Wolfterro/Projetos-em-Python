## Heavy-R Downloader [DESCONTINUADO]

#### Descrição:

###### Este é um simples programa que possui a função de baixar vídeos do site Heavy-R.
###### O programa cria uma pasta no mesmo diretório que está sendo executado e nele cria os diretórios para os vídeos que irá baixar.
###### Ao executar o programa, basta inserir a URL da página do vídeo desejado.
###### Os vídeos serão baixados em formato '.mp4', com o nome do vídeo original (sem espaços).

###### Aqui estão os possíveis argumentos que poderão ser inseridos na hora de executar o programa:


    Uso: ./Heavy-R Downloader.py [Argumento] [URL / ID]
    ---------------------------------------------------
    
    Argumentos:
    -----------
    '-h' ou '--help':    Mostra a tela de ajuda
    '-u' ou '--url':     Utiliza a URL inserida como argumento para o programa
    '-i' ou '--id':      Utiliza a ID inserida como argumento para o programa
    

#### Requisitos:
- Python 2.x
- BeautifulSoup

###### É necessário possuir o BeautifulSoup para que o programa possa funcionar.
###### Caso não tenha o BeautifulSoup, utilize o comando abaixo:

    sudo pip install beautifulsoup4

#### Download:

###### Você poderá baixar o programa com os comandos abaixo:

    git clone https://github.com/Wolfterro/Projetos-em-Python.git
    cd "Projetos-em-Python/Heavy-R Downloader"
    chmod +x "HeavyRDownloader.py"
    ./HeavyRDownloader.py
