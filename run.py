# Renderizar htmls desde la función app que creamos en _init_.py 
# from app import create_app si hubieramos usado la versión de renderizar htmls
# app = create_app()

# Versión simple
# from app import app
from app import app
if __name__ == '__main__':
    app.run(debug=True)
    # debug es el proceso de identificar, analizar y corregir errores o fallas (conocidos como bugs) 
    # en el código de un software o sistema
    # quedó este como url http://127.0.0.1:5000