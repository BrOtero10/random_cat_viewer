import requests
from typing import TypedDict, Optional
# import os
# from dotenv import load_dotenv

# load_dotenv()

# x_api_key = os.getenv("x-api-key")

class CatImage(TypedDict):
    id: str
    url: str
    width: int
    height: int

def get_random_cat_image() -> Optional[CatImage]:
    """
    Faz uma requisição à TheCatAPI para obter uma imagem aleatória de gato.

    Returns:
        Optional[CatImage]: Um dicionário contendo os seguintes campos:
            - id (str): ID da imagem.
            - url (str): URL da imagem.
            - width (int): Largura da imagem.
            - height (int): Altura da imagem.
        
        Retorna None se ocorrer algum erro durante a requisição ou no processamento dos dados.
    
    Exceções tratadas:
        - requests.exceptions.RequestException: Falha de rede, timeout ou erro HTTP.
        - KeyError, IndexError, ValueError, TypeError: Problemas ao acessar os dados do JSON.
        - demais excessões
    """
    url = "https://api.thecatapi.com/v1/images/search" # url para imagem aleatória
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status() # lança erro se o status != 200

        data = response.json()[0]

        if isinstance(data, list) and len(data) > 0:
            cat_data = data[0]
            return cat_data
        
    except requests.exceptions.RequestException as e:
        print("Erro de conexão ou resposta: ", e)
    except (KeyError, IndexError, ValueError, TypeError) as e:
        print("Erro ao processar os dados: ", e)
    except Exception as e:
        print("Erro: ", e)
    return None # em caso de erro