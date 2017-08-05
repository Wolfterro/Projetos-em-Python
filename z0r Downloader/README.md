## z0r Downloader

#### Descrição:

###### Este é um simples programa que possui a função de baixar animações do site z0r.de.
###### O programa cria uma pasta no mesmo diretório que está sendo executado e nela serão armazenadas as animações.
###### Ao executar o programa, basta inserir a ID da animação desejada.
###### As animações serão baixadas em formato '.swf', com a ID como nome do arquivo.
###### É possível também inserir múltiplas ID's no programa atráves de argumentos pela linha de comando.

###### Aqui estão os possíveis argumentos que poderão ser inseridos na hora de executar o programa:


    Uso: ./z0r-downloader.py [Argumento] [ID] ...
    ---------------------------------------------
    
    Argumentos:
    -----------
    '-h' ou '--help':    Mostra a tela de ajuda
    '-i' ou '--input':   Baixa através de ID's inseridas na linha de comando
    '-r' ou '--range':   Baixa animações entre um valor mínimo e um valor máximo
    '-a' ou '--all':     Baixa TODAS as animações do z0r.de
    
    Exemplo de uso para argumento '-r' ou '--range':
    ------------------------------------------------
    Uso: z0r-downloader.py [-r/--range] [min] [max]

#### Requisitos:
- Python 2.x

#### Download:

###### Você poderá baixar o programa com os comandos abaixo:

    git clone https://github.com/Wolfterro/Projetos-em-Python.git
    cd "Projetos-em-Python/z0r Downloader"
    chmod +x "z0r-downloader.py"
    ./z0r-downloader.py