from flask import redirect, render_template, request, session
from logic.formGruas_logic import GruasLogic

class Admin_gruas:
    @staticmethod
    def configure_routes(app):
        @app.route("/admin_gruas", methods=["GET", "POST"])
        def admin_gruas():
            if request.method == "GET":
                logic = GruasLogic()
                dataGruas = logic.getAllFormGruas()
                return render_template("admin_gruas.html", dataGruas=dataGruas)
            elif request.method == "POST":
                logic = GruasLogic()
                id = request.form["id"]   
                option = request.form["option"] 
                if option == "0" or option == "1":
                    logic.changeEstado(id,option)
                if option == "Modificar":
                    id = request.form["id"]
                    modelo = request.form["modelo"]
                    cantidad = request.form["cantidad"]
                    ubicacion = request.form["ubicacion"]
                    fecha = request.form["fecha"]
                    tiempo = request.form["tiempo"]
                    comentario = request.form["comentario"]
                    grua = dict(id = id, modelo = modelo, cantidad = cantidad, ubicacion = ubicacion, fecha = fecha, tiempo = tiempo, comentario = comentario)
                    return render_template("modificar_grua.html", grua=grua)
                if option == "Eliminar":
                    id = request.form["id"]
                    logic.deleteFormGrua(id)
                dataGruas = logic.getAllFormGruas()
                return render_template("admin_gruas.html", dataGruas= dataGruas)             