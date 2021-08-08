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
  
                if option == "0" or option == "1":
                    logic.changeEstado(id,option)
                if option == "Modificar":
                    id = request.form["id"]
                    tipo = request.form["tipo"]
                    numero = request.form["numero"]
                    fecha_inicio = request.form["fecha_inicio"]
                    fecha_final = request.form["fecha_final"]
                    ubicacion = request.form["ubicacion"]
                    descripcion = request.form["descripcion"]
                    comentario = request.form["comentario"]
                    proyecto = dict(id = id, tipo = tipo, numero = numero, fecha_inicio = fecha_inicio, fecha_final = fecha_final, ubicacion = ubicacion, descripcion = descripcion , comentario = comentario)
                    return render_template("modificar_proyecto.html", proyecto=proyecto)
                if option == "Eliminar":
                    id = request.form["id"]
                    logic.deleteProyecto(id)
                dataProyectos = logic.getAllProyectos()
                return render_template("admin_proyectos.html", dataProyectos= dataProyectos) 