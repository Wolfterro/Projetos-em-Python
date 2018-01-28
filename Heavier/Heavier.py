#!/usr/bin/env python3

'''
The MIT License (MIT)

Copyright (c) 2018 Wolfgang Almeida

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

# Imports gerais
# ==============
import sys

# Imports do programa
# ===================
from HeavierDownloader.DownloadManager import DownloadManager

#----------------------------------------
# Criado por: Wolfterro
# Versão: 2.0 - Python 3.x
# Data: 20/01/2018
#----------------------------------------

# Versão do programa
# ==================
VERSION = "2.0"

# Classe responsável por iniciar os processos de download dos vídeos
# ==================================================================
class Heavier(object):
    def __init__(self):
        self.DownloadManager = DownloadManager()

    def manual_download(self, video_ids):
        self.DownloadManager.download_by_id(video_ids)

    def auto_download(self):
        self.DownloadManager.download_by_config_url()

# Menu de ajuda
# -------------
def help():
    usage = "Uso: %s [Argumento] [ID]" % (str(sys.argv[0]))
    print(usage)
    print("-" * len(usage) + "\n")

    print("Argumentos opcionais:")
    print("---------------------")
    print("-h || --help\t\tMostra esta tela de ajuda")
    print("-i || --id\t\tUtiliza a ID inserida como argumento no programa\n")

    print("Arquivo de configurações:")
    print("-------------------------")
    print("list_id_url\t\tEndereço da lista de ID's dos vídeos em formato raw (texto puro)")
    print("template_url_page\tTemplate da página do vídeo")
    print("video_dir\t\tDiretório onde será armazenado os vídeos")
    print("download_max_tries\tNúmero de tentativas máximas para baixar o vídeo em caso de erro\n")

# Método principal do programa
# ----------------------------
def main():
    argc = len(sys.argv)

    print("========================")
    print("# Heavier - Versão %s #" % (VERSION))
    print("========================\n")

    if argc < 2:
        heavier = Heavier()
        heavier.auto_download()
    elif argc == 2:
        if str(sys.argv[1]) == "-h" or str(sys.argv[1]) == "--help":
            help()
        elif str(sys.argv[1]) == "-i" or str(sys.argv[1]) == "--id":
            print("[Heavier] Erro! É necessário ao menos uma id!")
            print("Uso: ./Heavier.py [Argumento] [ID]")
            sys.exit(1)
        else:
            print("[Heavier] Erro! Argumento desconhecido!")
            print("Uso: ./Heavier.py [Argumento] [ID]")
            sys.exit(2)
    elif argc > 2:
        if str(sys.argv[1]) == "-h" or str(sys.argv[1]) == "--help":
            help()
        elif str(sys.argv[1]) == "-i" or str(sys.argv[1]) == "--id":
            video_ids = []
            for i in range(2, argc):
                video_ids.append(str(sys.argv[i]))

            heavier = Heavier()
            heavier.manual_download(video_ids)
        else:
            print("[Heavier] Erro! Argumento desconhecido!")
            print("Uso: ./Heavier.py [Argumento] [ID]")
            sys.exit(2)

# Inicializando método principal
# ------------------------------
if __name__ == '__main__':
    main()
