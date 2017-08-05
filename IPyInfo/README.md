## IPyInfo

#### Descrição:

###### Este é um simples programa que possui a função de mostrar e verificar as informações de um endereço IP, seja o IP externo do usuário ou outro IP externo.
###### Ao executar o programa sem usar opções, ele irá mostrar as informações do endereço IP do usuário: o seu endereço IP externo, hostname, cidade, região, endereço (estimado), latitude/longitude e organização.
###### É possível também inserir um endereço IP para que o programa possa verificar suas informações e mostrar ao usuário.

###### Aqui estão os possíveis argumentos que poderão ser inseridos na hora de executar o programa:


    Uso: ./IPyInfo.py [OPÇÕES] [IP]
    -------------------------------
    
    Opções:
    -------
    '-h' ou '--help':  Mostra o menu de ajuda.
    '-i' ou '--ip':    Mostra as informações do endereço IP selecionado.
    
#### Requisitos:
- Python 2.x

#### Download:

###### Você poderá baixar o programa com os comandos abaixo:

    git clone https://github.com/Wolfterro/Projetos-em-Python.git
    cd "Projetos-em-Python/IPyInfo"
    chmod +x "IPyInfo.py"
    ./IPyInfo.py