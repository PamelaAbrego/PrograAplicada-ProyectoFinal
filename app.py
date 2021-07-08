from flask import Flask, render_template, request, redirect, session
from logic.usuarios_logic import UsuariosLogic
from flask_cors import CORS, cross_origin
import bcrypt
from routes.register_route import Register
from routes.login_route import Login
from routes.perfil_cliente_route import PerfilCliente
from routes.perfil_admin_route import PerfilAdmin
from routes.Proyectos_route import Proyectos


app = Flask(__name__)
app.secret_key = "VibranioProyecto123!!"
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"
Register.configure_routes(app)
Login.configure_routes(app)
PerfilCliente.configure_routes(app)
PerfilAdmin.configure_routes(app)
Proyectos.configure_routes(app)




@app.route("/")
def home():
    return render_template("index.html")


@app.route("/principal")
def principal():
    return render_template("principal.html")


@app.route("/contacto")
def contacto():
    return render_template("contacto.html")


@app.route("/capacitaciones")
def capacitaciones():
    return render_template("capacitaciones.html")



@app.route("/gruas")
def gruas():
    return render_template("gruas.html")


@app.route("/cotizaciones")
def cotizaciones():
    return render_template("cotizaciones.html")


@app.route("/mision_vision")
def mision_vision():
    return render_template("mision_vision.html")


@app.route("/admin_gruas")
def admin_gruas():
    return render_template("admin_gruas.html")


@app.route("/form_gruas")
def form_gruas():
    return render_template("form_gruas.html")


#@app.route("/proyectos")
#def proyectos():
#    return render_template("proyectos.html")


#@app.route("/form_proyectos")
#def form_proyectos():
#    return render_template("form_proyectos.html")


@app.route("/admin_proyectos")
def admin_proyectos():
    return render_template("admin_proyectos.html")


if __name__ == "__main__":
    app.run(debug=True)
