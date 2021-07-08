from flask import redirect, render_template, request, session, flash
from logic.usuarios_logic import UsuariosLogic
import bcrypt


class PerfilCliente:
    @staticmethod
    def configure_routes(app):
        @app.route("/perfil_cliente", methods=["GET", "POST"])
        def perfil_cliente():
            if request.method == "GET":
                return render_template("perfil_cliente.html", user = session["login_user"], email= session["login_email"])
            elif request.method == "POST":
                pass
            