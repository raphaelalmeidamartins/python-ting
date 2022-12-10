from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file, queue: Queue):
    for item in queue:
        if item["nome_do_arquivo"] == path_file:
            return None

    file_lines = txt_importer(path_file)

    file_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_lines),
        "linhas_do_arquivo": file_lines,
    }

    queue.enqueue(file_dict)
    print(file_dict)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
