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

# Imports do programa
# ===================
from HeavierDownloader.ConfigReader import ConfigReader

# Classe responsável por estruturar o nome e a localização do download dos vídeos
# ===============================================================================
class VideoStructure(object):
    def __init__(self):
        self.config = ConfigReader()
        self.video_dir = self.config.get_video_dir()
        self._check_video_dir()

    # Tratando o nome da pasta onde o vídeo será armazenado
    # -----------------------------------------------------
    def get_dir_name(self, id_video, video_title):
        forbidden_chars = ["/", "\\"]
        for letter in video_title:
            if letter in forbidden_chars:
                video_title = video_title.replace(letter, "-")

        return "%s-[%s]" % (video_title, id_video)

    # Tratando caminho absoluto do arquivo de vídeo
    # ---------------------------------------------
    def get_video_filename(self, video_dir_name, video_title):
        forbidden_chars = ["/", "\\"]
        for letter in video_title:
            if letter in forbidden_chars:
                video_title = video_title.replace(letter, "-")

        return "%s/%s/%s.mp4" % (self.video_dir, video_dir_name, video_title)

    # Criando pasta do arquivo de vídeo, caso não exista
    # --------------------------------------------------
    def create_video_dir(self, video_dir_name):
        video_dir_path = "%s/%s" % (self.video_dir, video_dir_name)
        if os.path.exists(video_dir_path):
            return False, "ALREADY_EXISTS"
        else:
            try:
                os.makedirs(video_dir_path)
                return True, "OK"
            except OSError:
                return False, "COULD_NOT_BE_CREATED"

    # ------------------
    # Métodos "privados"
    # ------------------

    # Verificando a existência da pasta de vídeos
    # -------------------------------------------
    def _check_video_dir(self):
        video_dir_abs = os.path.abspath(self.video_dir)
        if not os.path.exists(video_dir_abs):
            try:
                os.makedirs(video_dir_abs)
            except OSError as e:
                print("[Heavier] Erro! Não foi possível criar a pasta de Vídeos!")
                print("[Heavier] Erro: %s" % (str(e)))
                sys.exit(8)
