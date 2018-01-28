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
import requests

# Imports do programa
# ===================
from HeavierDownloader.ConfigReader import ConfigReader
from HeavierDownloader.VideoStructure import VideoStructure
from HeavierDownloader.PageScrapper import PageScrapper

# Classe responsável por gerenciar o download dos vídeos
# ======================================================
class DownloadManager(object):
    def __init__(self):
        self.config = ConfigReader()

        self.download_success = []
        self.download_fail = []
        self.tries = 0

    # Baixando por ID inserido no terminal
    # ------------------------------------
    def download_by_id(self, video_ids):
        list_len = len(video_ids)

        print("[Heavier] Lista contém %d itens! " % list_len, end="")
        print("Baixando...\n")

        for i in video_ids:
            try:
                int(i)
            except ValueError:
                print("[Heavier] Erro! ID '%s' não é uma ID válida! Pulando..." % (i))
                status_message = "ID inválida!"
                self.download_fail.append("%s - %s" % (i, status_message))
                continue

            self._prepare_download_process(i)

        print("\n[Heavier] Downloads com sucesso: [%d/%d]" % (len(self.download_success), list_len))
        print("----------------------------------------")
        for success in self.download_success:
            print(success)

        print("\n[Heavier] Downloads com falha: [%d/%d]" % (len(self.download_fail), list_len))
        print("-------------------------------------")
        for fail in self.download_fail:
            print(fail)

    # Baixando por URL de uma lista de ID's especificada no configs.json
    # ------------------------------------------------------------------
    def download_by_config_url(self):
        print("[Heavier] Resgatando lista de ID's...")
        list_id = self._get_id_list()
        list_len = len(list_id)

        print("[Heavier] Lista contém %d itens! " % list_len, end="")
        if list_len > 0:
            print("Baixando...\n")

            for i in list_id:
                try:
                    int(i)
                except ValueError:
                    print("[Heavier] Erro! ID '%s' não é uma ID válida! Pulando..." % (i))
                    status_message = "ID inválida!"
                    self.download_fail.append("%s - %s" % (i, status_message))
                    continue

                self._prepare_download_process(i)

            print("\n[Heavier] Downloads com sucesso: [%d/%d]" % (len(self.download_success), list_len))
            print("----------------------------------------")
            for success in self.download_success:
                print(success)

            print("\n[Heavier] Downloads com falha: [%d/%d]" % (len(self.download_fail), list_len))
            print("-------------------------------------")
            for fail in self.download_fail:
                print(fail)
        else:
            print("Saindo...\n")
            sys.exit(0)

    # ------------------
    # Métodos "privados"
    # ------------------

    # Resgatando lista de ID's
    # ------------------------
    def _get_id_list(self):
        url = self.config.get_url_id_file()

        try:
            content = requests.get(url)
        except requests.exceptions.MissingSchema:
            print("[Heavier] Erro! Não foi possível resgatar lista de ID's!")
            sys.exit(7)

        if content.status_code == 200:
            return content.text.split("\n")
        else:
            print("[Heavier] Erro! Não foi possível resgatar lista de ID's!")
            sys.exit(7)

    # Imprimindo barra de progresso no terminal
    # -----------------------------------------
    def _print_progress_bar(self, downloaded, total, width=50):
        progress = float(downloaded) / float(total)
        bar = ('#' * int(width * progress)).ljust(width)
        percent = progress * 100.0
        to_print = "[Heavier] Baixando: [%s] %.2f%%\r" % (bar, percent)
        print(to_print, end='')
        if round(percent) >= 100:
            print('%s\r' % (' ' * len(to_print)), end='')

    # Baixando arquivo de vídeo
    # -------------------------
    def _download_file(self, response_video, video_filename, video_url):
        if response_video.status_code == 200:
            file = open(video_filename, "wb")
            file_size = response_video.headers['Content-length']
            downloaded = 0

            for data in response_video.iter_content(chunk_size=1024):
                if data:
                    file.write(data)
                    downloaded += len(data)
                    self._print_progress_bar(downloaded, file_size)

            file.close()

            if downloaded != int(file_size):
                print("\n[Heavier] Tamanho: %s bytes | Baixado: %s bytes" % (file_size, downloaded))
                self.tries += 1
                if self.tries >= self.config.get_max_tries():
                    print("[Heavier] Vídeo incompleto ou corrompido! Número de tentativas excedido!")
                    return False, "Número de tentativas excedido!"
                else:
                    print("[Heavier] Vídeo incompleto ou corrompido! Tentando mais uma vez...")
                    response_video = requests.get(video_url, stream=True)
                    return self._download_file(response_video, video_filename, video_url)
            else:
                print("[Heavier] Tamanho: %s bytes | Baixado: %s bytes" % (file_size, downloaded))
                return True, "OK"
        else:
            return False, "Response de vídeo retornou com status %d!" % (response_video.status_code)

    # Iniciando processo de download
    # ------------------------------
    def _download_process(self, id_video, video_url, video_title):
        video_structure = VideoStructure()
        video_dir_name = video_structure.get_dir_name(id_video, video_title)
        video_filename = video_structure.get_video_filename(video_dir_name, video_title)

        dir_created, situation = video_structure.create_video_dir(video_dir_name)

        if dir_created:
            print("[Heavier] Iniciando download de: %s" % (video_dir_name))

            response_video = requests.get(video_url, stream=True)
            return self._download_file(response_video, video_filename, video_url)
        else:
            if situation == "COULD_NOT_BE_CREATED":
                print("[Heavier] Erro! Pasta para o vídeo '%s' não pôde ser criada! Pulando..." % (video_dir_name))
                return False, "Pasta para o vídeo não pôde ser criada!"
            elif situation == "ALREADY_EXISTS":
                print("[Heavier] Erro! Vídeo '%s' já existe! Pulando..." % (video_dir_name))
            return False, "Vídeo já existe!"

    # Preparando para iniciar processo de download
    # --------------------------------------------
    def _prepare_download_process(self, id_video):
        template_url_page = self.config.get_template_url_page()
        template_url_page = template_url_page % id_video

        try:
            req_content_page = requests.get(template_url_page)

            if req_content_page.status_code == 200:
                content_page = req_content_page.text
                scrapper = PageScrapper(content_page)

                video_url = scrapper.get_video_url()
                if video_url != None:
                    video_title = scrapper.get_video_title()

                    download_status, status_message = self._download_process(id_video, video_url, video_title)
                    if download_status:
                        self.download_success.append("%s - %s" % (id_video, status_message))
                    else:
                        self.download_fail.append("%s - %s" % (id_video, status_message))
                else:
                    print("[Heavier] Erro! Não foi possível baixar o vídeo '%s'! Pulando..." % id_video)
                    status_message = "Sem URL de vídeo!"
                    self.download_fail.append("%s - %s" % (id_video, status_message))
            else:
                print("[Heavier] Erro! Não foi possível baixar o vídeo '%s'! Pulando..." % id_video)
                status_message = "Response retornou com status %d!" % (req_content_page.status_code)
                self.download_fail.append("%s - %s" % (id_video, status_message))
        except Exception as e:
            print("[Heavier] Erro! Não foi possível baixar o vídeo '%s'! Pulando..." % id_video)
            print("[Heavier] Erro: %s" % (str(e)))
            status_message = "Erro genérico de código!"
            self.download_fail.append("%s - %s" % (id_video, status_message))
