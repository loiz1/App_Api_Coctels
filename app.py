# app.py

from flask import Flask, render_template, request, url_for
import requests
app = Flask(__name__)

# Lista de cócteles 
COCKTAILS = [
    {"idDrink": "11007", "strDrink": "Margarita", "strDrinkThumb": "/static/images/mar.png"},
    {"idDrink": "11000", "strDrink": "Mojito", "strDrinkThumb": "/static/images/mojito.png"},
    {"idDrink": "178364", "strDrink": "Vodka Tónica", "strDrinkThumb": "/static/images/vodka.png"},
    {"idDrink": "11005", "strDrink": "Martini Dry", "strDrinkThumb": "/static/images/martini.png"},
    {"idDrink": "17204", "strDrink": "Long Island Iced Tea", "strDrinkThumb": "/static/images/long_island.png"},
    {"idDrink": "11403", "strDrink": "Gin and Tonic", "strDrinkThumb": "/static/images/gin.png"},
    {"idDrink": "11202", "strDrink": "Caipirinha", "strDrinkThumb": "/static/images/caipirinha.png"},
    {"idDrink": "11004", "strDrink": "Whiskey Sour", "strDrinkThumb": "/static/images/sour.png"},
    {"idDrink": "11113", "strDrink": "Bloody Mary", "strDrinkThumb": "/static/images/bloody.png"}
]

# Función para buscar cócteles por nombre
def search_cocktail(name):
    response = requests.get(f'https://www.thecocktaildb.com/api/json/v1/1/search.php?s={name}')
    data = response.json()
    return data['drinks'] if data and data['drinks'] else []

# Función para obtener detalles de un cóctel por ID
def get_cocktail_by_id(idDrink):
    response = requests.get(f'https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={idDrink}')
    data = response.json()
    return data['drinks'][0] if data and data['drinks'] else None 


# Ruta principal
@app.route('/', methods=['GET'])
def index():
    # Obtener cócteles específicos para la galería
    popular_cocktails = COCKTAILS 

    # Manejar búsqueda
    search_query = request.args.get('drink_name')
    if search_query:
        cocktails = search_cocktail(search_query) 
    else:
        cocktails = None
    return render_template('index.html', popular_cocktails=popular_cocktails, cocktails=cocktails, search_query=search_query)


@app.route('/details/<idDrink>')
def details(idDrink):
    cocktail = get_cocktail_by_id(idDrink)

    if not cocktail:
        return render_template('error.html', message=f'Cóctel con ID {idDrink} no encontrado.'), 404
    return render_template('details.html', cocktail=cocktail) 

if __name__ == '__main__':
    app.run(debug=True)