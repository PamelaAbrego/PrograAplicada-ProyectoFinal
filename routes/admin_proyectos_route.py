from flask import redirect, render_template, request, session
from logic.formProyectos_logic import ProyectosLogic
import bcrypt

class Admin_proyectos:
    @staticmethod
    def configure_routes(app):
        @app.route("/admin_proyectos", methods=["GET", "POST"])
        def admin_proyectos():
            if request.method == "GET":
                logic = ProyectosLogic()
                dataProyectos = logic.getAllProyectos()
                return render_template("admin_proyectos.html", dataProyectos=dataProyectos)
            elif request.method == "POST":
                logic = ProyectosLogic()
                id = request.form["id"]   
                option = request.form["option"] 
                logic.changeEstado(id,option)
                dataProyectos = logic.getAllProyectos()
                return render_template("admin_proyectos.html", dataProyectos= dataProyectos) 