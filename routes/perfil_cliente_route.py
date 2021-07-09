from flask import redirect, render_template, request, session, flash
from logic.formGruas_logic import GruasLogic
from logic.formProyectos_logic import ProyectosLogic
import bcrypt


class PerfilCliente:
    @staticmethod
    def configure_routes(app):
        @app.route("/perfil_cliente", methods=["GET", "POST"])
        def perfil_cliente():
            if request.method == "GET":
                logicGruas = GruasLogic()
                user = session["login_user"]
                dataGruas = logicGruas.getAllByUser(user)
                logicProyectos = ProyectosLogic()
                dataProyectos = logicProyectos.getAllByUser(user)
                return render_template("perfil_cliente.html", user = user, email= session["login_email"], dataGruas = dataGruas, dataProyectos = dataProyectos)
            elif request.method == "POST":
                pass
            