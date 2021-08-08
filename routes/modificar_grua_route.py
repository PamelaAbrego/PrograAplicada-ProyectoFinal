from flask import redirect, render_template, request, session
from logic.formGruas_logic import GruasLogic

class Modificar_gruas:
    @staticmethod
    def configure_routes(app):
        @app.route("/modificar_grua", methods=["GET", "POST"])
        def modificar_grua():
            if request.method == "GET":
                logic = GruasLogic()
                dataGruas = logic.getAllFormGruas()
                return render_template("modificar_grua.html", dataGruas=dataGruas)
            elif request.method == "POST":
                logic = GruasLogic()
                id = request.form["ID"]
                modelo = request.form["modelo"]
                cantidad = request.form["cantidad"]
                ubicacion = request.form["ubicacion"]
                fecha = request.form["fecha"]
                tiempo = request.form["tiempo"]
                comentario = request.form["comentario"]
                alquiler = logic.getFormGruaById(id)
                estado = alquiler["estado"]

                if len(modelo) == 0:
                    modelo = alquiler['modelo']
                if len(cantidad) == 0:
                    cantidad = alquiler['cantidad']
                if len(ubicacion) == 0:
                    ubicacion = alquiler['ubicacion']
                if len(fecha) == 0:
                    fecha = alquiler['fecha']
                if len(tiempo) == 0:
                    tiempo = alquiler['tiempo']
                if len(comentario) == 0:
                    comentario = alquiler['comentario']
                
                formGrua = {"modelo": modelo, "cantidad":cantidad, "ubicacion":ubicacion, "fecha":fecha, "tiempo":tiempo, "comentario":comentario, "estado":estado}
                logic.updateFormGrua(id, formGrua)
                dataGruas = logic.getAllFormGruas()
                return render_template("admin_gruas.html", dataGruas= dataGruas)