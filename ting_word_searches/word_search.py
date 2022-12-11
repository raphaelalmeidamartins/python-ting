from ting_file_management.queue import Queue


def exists_word(word: str, queue: Queue, include_content: bool = False):
    result = []

    for file_index, file in enumerate(queue, start=1):
        found_lines = [
            {"conteudo": line, "linha": line_index}
            if include_content
            else {"linha": line_index}

            for line_index, line
            in enumerate(file["linhas_do_arquivo"], start=1)
            if word.lower() in line.lower()
        ]

        if not len(found_lines):
            continue

        result.append({
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": found_lines,
        })

    return result


def search_by_word(word: str, queue: Queue):
    return exists_word(word, queue, True)
