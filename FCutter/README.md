## FCutter

### Descrição:

##### Este é um simples programa que possui a função de realizar cortes em arquivos de multimídia utilizando o FFmpeg para realizar este procedimento.
##### Ao invocar o programa com os arquivos fonte e destino como argumentos, o programa irá pedir ao usuário para inserir o tempo inicial de corte e o tempo final de corte.
##### O usuário poderá inserir o tempo em segundos ou em formato HH:mm:ss.
##### Caso o tempo de duração do corte seja igual a zero, o corte será descartado!

##### Aqui estão os possíveis argumentos que poderão ser inseridos na hora de executar o programa:

    Uso: ./FCutter.py <Arquivo Fonte> <Arquivo Destino>
    ---------------------------------------------------
    
    Opções:
    -------
    '-h' ou '--help':  Mostra o menu de ajuda.


#### Requisitos:
- Python 2.x
- FFmpeg

#### Download:

##### Você poderá baixar o programa com os comandos abaixo:

    git clone https://github.com/Wolfterro/Projetos-em-Python.git
    cd "Projetos-em-Python/FCutter"
    ./FCutter.py