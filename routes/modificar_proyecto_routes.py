from flask import redirect, render_template, request, session, url_for
from logic.formProyectos_logic import ProyectosLogic
import bcrypt


class Modificar_proyecto:
    @staticmethod
    def configure_routes(app):
        @app.route("/modificar_proyecto", methods=["GET", "POST"])
        def modificar_proyecto():
            if request.method == "GET":
                logic = ProyectosLogic()
                dataProyectos = logic.getAllProyectos()
                return render_template("modificar_proyecto.html", dataProyectos=dataProyectos)
            elif request.method == "POST":
                logic = ProyectosLogic()
                id = request.form["id"]
                proyecto = logic.getProyectoById(id)
                tipos = request.form.getlist("Coti")
                tipo =""
                for x in tipos:
                    tipo = tipo + " " + x

                tipo = str(tipo)

                if len(tipo)==0:
                    tipo = proyecto["tipo"]
                numero = request.form["fphone"]
                if len(numero)==0:
                    numero = proyecto["numero"]
                fecha_inicio = request.form["datemin"]
                if len(fecha_inicio)==0:
                    fecha_inicio = proyecto["fecha_inicio"]
                fecha_final = request.form["date"]
                if len(fecha_final)==0:
                    fecha_final = proyecto["fecha_final"]
                ubicacion = request.form["floc"]
                if len(ubicacion)==0:
                    ubicacion = proyecto["ubicacion"]
                descripcion = request.form["descripcion"]
                if len(descripcion)==0:
                    descripcion = proyecto["descripcion"]
                comentario = request.form["comentario"]
                if len(comentario) == 0:
                    comentario = proyecto["comentario"]

                formProyecto = {"tipo": tipo, "numero":numero, "fecha_inicio":fecha_inicio, "fecha_final":fecha_final, "ubicacion":ubicacion, "descripcion":descripcion, "comentario":comentario}
                logic.updateProyecto(id, formProyecto)
                dataProyectos = logic.getAllProyectos()
                return render_template("modificar_proyecto.html", dataProyectos=dataProyectos)

                

            

            




