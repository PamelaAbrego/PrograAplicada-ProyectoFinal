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
                logic.changeEstado(id,option)
                dataGruas = logic.getAllFormGruas()
                return render_template("admin_gruas.html", dataGruas= dataGruas)             