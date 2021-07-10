from flask import redirect, render_template, request, session, url_for
from logic.formGruas_logic import GruasLogic
import bcrypt


class Gruas:
    @staticmethod
    def configure_routes(app):
        @app.route("/gruas", methods=["GET", "POST"])
        def gruas():
            if request.method == "GET":
                return render_template("gruas.html")
            elif request.method == "POST":
                role = session["login_role"]
                if role == "Cliente":
                    return redirect("perfil_cliente")
                if role == "Administrador":
                    return redirect("perfil_admin")

        @app.route("/form_gruas", methods=["GET", "POST"])
        def form_gruas():
            if request.method == "GET":
                return render_template("form_gruas.html")
            elif request.method == "POST":
                error1 = None
                error2 = None
                error3 = None
                error4 = None
                error5 = None
                
                logic = GruasLogic()
                usuario = session["login_user"]
                modelo = request.form["modelo"]
                cantidad = request.form["cantidad"]
                ubicacion = request.form["ubicacion"]
                fecha = request.form["fecha"]
                tiempo = request.form["tiempo"]
                estado = "Enviado"

                decision = True

                if len(modelo) == 0:
                    decision = False
                    error1 = "Este es un campo obligatorio"

                if len(cantidad) == 0:
                    decision = False
                    error2 = "Este es un campo obligatorio"

                if len(ubicacion) == 0:
                    decision = False
                    error3 = "Este es un campo obligatorio"

                if len(fecha) == 0:
                    decision = False
                    error4 = "Este es un campo obligatorio"

                if len(tiempo) == 0:
                    decision = False
                    error5 = "Este es un campo obligatorio"

                if decision == True:
                    confirmation = "Tu formulario fue enviado correctamente"
                    logic.insertFormGrua(usuario, modelo, cantidad, ubicacion, fecha, tiempo, estado)
                    return redirect(url_for("perfil_cliente"))

                return render_template("form_gruas.html", error1=error1, error2=error2, error3=error3, error4=error4, error5=error5)
                

            
