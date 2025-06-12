# models/cocktail_model.py
import requests

BASE_URL = "https://www.thecocktaildb.com/api/json/v1"
# Usamos la clave de prueba '1' para desarrollo/educación
API_KEY_TEST = "1"

def search_cocktail_by_name(drink_name):
    """
    Busca cócteles por nombre en la TheCocktailDB API.
    """
    # URL del endpoint de búsqueda por nombre
    url = f"{BASE_URL}/{API_KEY_TEST}/search.php?s={drink_name}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get('drinks') 

    except requests.exceptions.RequestException as e:
        print(f"Error al llamar a la API de TheCocktailDB: {e}")
        return None
    except Exception as e:
        print(f"Ocurrió un error inesperado en el modelo de cócteles: {e}")
        return None