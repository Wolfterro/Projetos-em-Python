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
import os
import sys
import json

# Classe responsável por ler o arquivo de configurações em formato .json
# ======================================================================
class ConfigReader(object):
    def __init__(self, file_path="configs.json"):
        self.file_path = file_path
        self.check_file()

    # Verificando existência do arquivo de configurações
    # --------------------------------------------------
    def check_file(self):
        path = os.path.abspath(self.file_path)
        if not os.path.exists(path):
            print("[Heavier] Erro! Arquivo de configurações não existe!")
            sys.exit(4)
        else:
            try:
                file = open(self.file_path, "r")
                self.contents = file.read()
                file.close()
            except OSError:
                print("[Heavier] Erro! Não foi possível acessar arquivo de configurações!")
                sys.exit(5)

    # Resgatando URL da lista de ID's
    # -------------------------------
    def get_url_id_file(self):
        data = json.loads(self.contents)
        if "list_id_url" in data:
            return data['list_id_url']
        else:
            print("[Heavier] Erro! Não foi possível resgatar a URL da lista de ID's!")
            sys.exit(6)

    # Resgatando template da URL da página de vídeos
    # ----------------------------------------------
    def get_template_url_page(self):
        data = json.loads(self.contents)
        if "template_url_page" in data:
            return data['template_url_page']
        else:
            print("[Heavier] Erro! Não foi possível resgatar a URL da página!")
            sys.exit(6)

    # Resgatando nome da pasta de vídeos
    # ----------------------------------
    def get_video_dir(self):
        data = json.loads(self.contents)
        if "video_dir" in data:
            return data['video_dir']
        else:
            print("[Heavier] Erro! Não foi possível determinar a pasta de Vídeos!")
            sys.exit(6)

    # Resgatando número máximo de tentativas de download
    # --------------------------------------------------
    def get_max_tries(self):
        data = json.loads(self.contents)
        if "download_max_tries" in data:
            return data['download_max_tries']
        else:
            return 3    # Default
