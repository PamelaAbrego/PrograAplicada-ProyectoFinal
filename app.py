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
from routes.principal_route import Principal
from routes.registro_usuarios_route import RegistroUsuarios
from routes.modificar_grua_route import Modificar_gruas
from routes.construccion_materiales_route import ConstruccionMateriales
from routes.poda_materiales_route import PodaMateriales
from routes.electricidad_materiales_route import ElectricidadMateriales
from routes.modificar_proyecto_routes import Modificar_proyecto
from routes.carrito_route import Carrito

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
Principal.configure_routes(app)
RegistroUsuarios.configure_routes(app)
Modificar_gruas.configure_routes(app)
ConstruccionMateriales.configure_routes(app)
PodaMateriales.configure_routes(app)
ElectricidadMateriales.configure_routes(app)
Modificar_proyecto.configure_routes(app)
Carrito.configure_routes(app)


@app.route("/")
def home():
    return render_template("index.html")

def index_materiales():
    return render_template("index_materiales.html")

if __name__ == "__main__":
    app.run(debug=True)
