# El objetivo es crear una aplicación de "Lista de Tareas" (To-Do List)
# que permita añadir y eliminar tareas.
# Las tareas se almacenarán en una lista en la memoria del servidor.

# Debe poder crearse más tareas en la lista
# Debe poder eliminarse una tarea en la lista
# Debe poder editarse una tarea en específico de la lista
# Deben verse las tareas creadas
# Lista para almacenar las tareas en memoria.
# Puedes inicializarla con algunas tareas de ejemplo.

from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# Lista de tareas en memoria (ahora con estado de completadas)
tareas = [
    {"texto": "Aprender Python", "completada": False},
    {"texto": "Crear un entregable", "completada": False},
    {"texto": "Practicar Flask", "completada": True},
    {"texto": "Crear un glosario", "completada": False},
    {"texto": "Subir materiales a GitHub", "completada": False},
]

@app.route("/")
def home():
    html = """
    <html>
    <head>
        <title>Lista de Tareas</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: cream;
                margin: 0;
                padding:45px;
            }
            h1, h2 {
                text-align: center;
                color: Darkred;
            }
            .container {
                display: flex;
                justify-content: center;
                gap: 40px;
                margin-top: 20px;
            }
            .tasks {
                flex: 1;
                max-width: 500px;
                background-color: #fff7e6;
                padding: 10px;
                border-radius: 20px;
                border: 2px solid #ff9933;
                box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
            }
            .tasks ul {
                list-style: none;
                padding: 0;
            }
            .tasks li {
                padding: 5px 0;
            }
            .tasks a {
                margin-left: 10px;
                color: blue;
                text-decoration: none;
            }
            .tasks a:hover {
                text-decoration: underline;
            }
            .calendar {
                flex: 1;
                max-width: 500px;
                background-color: #fff7e6;
                padding: 20px;
                border-radius: 10px;
                border: 2px solid #ff9933;
                box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
            }
            .calendar h2 {
                color: #cc0000;
            }
            .calendar table {
                width: 100%;
                border-collapse: collapse;
            }
            .calendar th, .calendar td {
                border: 1px solid #999;
                padding: 10px;
                text-align: center;
                border-radius: 5px;
            }
            .calendar th {
                background-color: #ffd699;
            }
            .weekend {
                background-color: #ffe6e6;
                color: #cc0000;
            }
            .fiesta {
                background: linear-gradient(to bottom, #ff9999, #ff4d4d);
                color: red;
                font-weight: bold;
            }
            .calendar td:hover {
                background-color: #cce5ff;
                cursor: pointer;
            }
            .top-image {
                display: block;
                margin: 0 auto 2px auto;
                width: 300px;
                border-radius: 10px;
            }
        </style>
    </head>
    <body>
<div style="display: flex; justify-content: center; gap: 5px; margin-bottom: 20px;">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTltsq-z58pBD5YPSjnzr9OHMJNxXNqnzvyuMPakqZJFECCt4Zru35_nJaE2TYpiP08SQ&usqp=CAU">   
</div>

        <div class="container">
            <!-- Sección de tareas -->
            <div class="tasks">
                <h1>Lista de Tareas</h1>
                <ul>
    """
    # Mostrar tareas con checkbox
    for i, tarea in enumerate(tareas):
        checked = "checked" if tarea["completada"] else ""
        estilo = "text-decoration: line-through; color: gray;" if tarea["completada"] else ""
        html += f"""
        <li>
            <form action='/toggle/{i}' method='post' style='display:inline;'>
                <input type='checkbox' onchange='this.form.submit()' {checked}>
            </form>
            <span style='{estilo}'>{tarea["texto"]}</span>
            - <a href='/editar/{i}'>Editar</a> - <a href='/eliminar/{i}'>Eliminar</a>
        </li>
        """
    html += """
                </ul>
                <h2>Agregar nueva tarea</h2>
                <form action="/agregar" method="post">
                    <input type="text" name="nueva_tarea" required>
                    <input type="submit" value="Agregar">
                </form>
            </div>

            <!-- Sección calendario -->
            <div class="calendar">
                <h2>Calendario Septiembre 2025</h2>
                <table>
                    <tr>
                        <th>Lun</th><th>Mar</th><th>Mié</th><th>Jue</th><th>Vie</th><th>Sáb</th><th>Dom</th>
                    </tr>
                    <tr>
                        <td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td class="weekend">7</td>
                    </tr>
                    <tr>
                        <td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td class="weekend">14</td>
                    </tr>
                    <tr>
                        <td>15</td><td>16</td><td>17</td>
                        <td class="fiesta">18</td>
                        <td class="fiesta">19</td>
                        <td>20</td>
                        <td class="weekend">21</td>
                    </tr>
                    <tr>
                        <td>22</td><td>23</td><td>24</td><td>25</td><td>26</td><td>27</td><td class="weekend">28</td>
                    </tr>
                    <tr>
                        <td>29</td><td>30</td><td></td><td></td><td></td><td></td><td></td>
                    </tr>
                </table>
                <p style="text-align:center; color:#cc0000; margin-top:10px;">🎉 18 y 19: Fiestas Patrias</p>
            </div>
        </div>
    </body>
    </html>
    """
    return html

# Rutas para agregar/editar/eliminar/toggle tareas
@app.route("/agregar", methods=["POST"])
def agregar():
    nueva_tarea = request.form.get("nueva_tarea")
    if nueva_tarea:
        tareas.append({"texto": nueva_tarea, "completada": False})
    return redirect(url_for("home"))

@app.route("/eliminar/<int:index>")
def eliminar(index):
    if 0 <= index < len(tareas):
        tareas.pop(index)
    return redirect(url_for("home"))

@app.route("/editar/<int:index>", methods=["GET", "POST"])
def editar(index):
    if 0 <= index < len(tareas):
        if request.method == "POST":
            nueva_tarea = request.form.get("tarea_editada")
            if nueva_tarea:
                tareas[index]["texto"] = nueva_tarea
            return redirect(url_for("home"))
        return f"""
        <html>
        <body style="background-color: pink; padding:20px;">
            <h1>Editar tarea</h1>
            <form method="post">
                <input type="text" name="tarea_editada" value="{tareas[index]['texto']}" required>
                <input type="submit" value="Guardar">
            </form>
            <a href="/">Volver</a>
        </body>
        </html>
        """
    return redirect(url_for("home"))

@app.route("/toggle/<int:index>", methods=["POST"])
def toggle(index):
    if 0 <= index < len(tareas):
        tareas[index]["completada"] = not tareas[index]["completada"]
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
