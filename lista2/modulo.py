"""Módulo desenvolvido para cuidar da leitura de arquivos JSON."""

import json

def carrega_conteudos_json(arquivo: str) -> dict:
    """
    Carrega o conteúdo de um arquivo `json` e retorna na forma de um dicionário
    Python.

    Parameters
    ----------
    arquivo:
        Uma string contendo o nome do arquivo.

    Returns
    -------
    dict:
        Um dicionário representando os conteúdos do arquivo `json`.

    Raises
    ------
    TypeError:
        O parâmetro `arquivo` não era uma string.
    FileNotFoundError:
        O arquivo não pode ser encontrado.
    IsADirectoryError:
        A string passada representa um diretório.
    PermissionError:
        Não há autorização para acessar o arquivo.
    OSError:
        Houve um problema do Sistema Operacional durante a leitura do arquivo.
    json.JSONDecodeError:
        Os conteúdos dentro do arquivo não estavam no formato de um `json`.
    """
    if not isinstance(arquivo, str):
        raise TypeError
    with open(arquivo, "r") as arquivo_json:
        dicionario = json.load(arquivo_json)
    return dicionario
