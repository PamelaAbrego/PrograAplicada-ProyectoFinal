from flask import Flask, render_template, request, redirect, session
from logic.usuarios_logic import UsuariosLogic
from flask_cors import CORS, cross_origin
import bcrypt
from routes.register_route import Register
from routes.login_route import Login
from routes.perfil_cliente_route import PerfilCliente
from routes.perfil_admin_route import PerfilAdmin
from routes.Proyectos_route import Proyectos
from routes.gruas_route import Gruas
from routes.admin_gruas_route import Admin_gruas
from routes.admin_proyectos_route import Admin_proyectos

app = Flask(__name__)
app.secret_key = "VibranioProyecto123!!"
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"
Register.configure_routes(app)
Login.configure_routes(app)
PerfilCliente.configure_routes(app)
PerfilAdmin.configure_routes(app)
Proyectos.configure_routes(app)
Gruas.configure_routes(app)
Admin_gruas.configure_routes(app)
Admin_proyectos.configure_routes(app)


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


@app.route("/cotizaciones")
def cotizaciones():
    return render_template("cotizaciones.html")


@app.route("/mision_vision")
def mision_vision():
    return render_template("mision_vision.html")



if __name__ == "__main__":
    app.run(debug=True)
