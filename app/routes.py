from flask import Blueprint, render_template  # render template nos ayuda a renderizae html
# blueprint nos ayudan con las rutas
bp = Blueprint('main', __name__)

@bp.route('/')  
def index():  # archivo index.html se corre con run arriba y debugging 
    return render_template('index.html')
# html= Lenguaje de Marcado de Hipertexto