from flask import redirect, render_template, request, session
from logic.formGruas_logic import GruasLogic
import bcrypt


class Gruas:
    @staticmethod
    def configure_routes(app):
        @app.route("/gruas", methods=["GET"])
        def gruas():
            if request.method == "GET":
                return render_template("gruas.html")

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
                usuario = "Username"
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
                    return render_template("perfil_cliente.html", confirmation=confirmation)

                return render_template("form_gruas.html", error1=error1, error2=error2, error3=error3, error4=error4, error5=error5)
                

            
