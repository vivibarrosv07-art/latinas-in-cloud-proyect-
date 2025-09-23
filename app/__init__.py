from flask import Flask  # inicializamos flask

# Versión simple (con el archivo run)
# app = Flask(__name__)


# @app.route('/')
# inicializamos la ruta (pusimos la inicial/,
# pero se le puede poner cualquier cosa después como ruta)
# def index():
    # creamos la función, aquí fue index
#    return "Hola, Flask! Esta es la versión simple"

# Renderizar HTMLS (se refiere al proceso de generar una salida visual o
# auditiva a partir de datos o código,
# como crear imágenes, videos
# o sonidos a partir de modelos 3D, o transformar el
# código de una página web en su representación visible en el navegador)


# renderizar htmls
def create_app():
    app = Flask(__name__)

    # Importar rutas dentro de la función (con el archivo routes))
    from . import routes
    app.register_blueprint(routes.bp)

    return app
