from flask import redirect, render_template, request, session, url_for
from logic.formProyectos_logic import ProyectosLogic
import bcrypt


class Proyectos:
    @staticmethod
    def configure_routes(app):
        @app.route("/cotizaciones", methods=["GET", "POST"])
        def cotizaciones():
            if request.method == "GET":
                return render_template("cotizaciones.html")
            elif request.method == "POST":
                role = session["login_role"]
                if role == "Cliente":
                    return redirect("perfil_cliente")
                if role == "Administrador":
                    return redirect("perfil_admin")

        @app.route("/form_proyectos", methods=["GET", "POST"])
        def form_proyectos():
            if request.method == "GET":
                return render_template("form_proyectos.html")
            elif request.method == "POST":
                error1 = None
                error2 = None
                error3 = None
                error4 = None
                error5 = None
                error6 = None
                error7 = None
                error8 = None
                error9 = None
                
                logic = ProyectosLogic()
                fecha_envio = logic.getDate()
                tipo = request.form.getlist("Coti")
                usuario = session["login_user"]
                numero = request.form["fphone"]
                fecha_inicio = request.form["datemin"]
                fecha_final = request.form["date"]
                ubicacion = request.form["floc"]
                descripcion = request.form["detalles"]
                estado = "Enviado" 
                
                
                types = ""
                for x in tipo:
                    types = types + " " + x

                types = str(types)

                fechai = str(fecha_envio[0]["sysdate()"])

                decision = True

                if len(types) == 0:
                    decision = False
                    error1 = "Este es un campo obligatorio"

                if len(numero) == 0:
                    decision = False
                    error2 = "Este es un campo obligatorio"

                elif len(numero) != 8:
                    decision = False
                    error3 = "Ingresa un número telefónico de 8 dígitos"

                if len(fecha_inicio) == 0:
                    decision = False
                    error4 = "Este es un campo obligatorio"

                if len(fecha_final) == 0:
                    decision = False
                    error5 = "Este es un campo obligatorio"

                if len(ubicacion) == 0:
                    decision = False
                    error6 = "Este es un campo obligatorio"

                if descripcion.isspace() == True:
                    decision = False
                    error7 = "Este es un campo obligatorio"

                if len(descripcion) == 0:
                    decision = False
                    error8 = "Este es un campo obligatorio"

                #if len(descripcion) == 2:
                #    decision = False
                #    error9 = "Este es un campo obligatorio"

                if decision == True:
                    confirmation = "Tu formulario fue enviado correctamente"
                    logic.insertProyecto(fechai, types, usuario, numero, fecha_inicio, fecha_final, ubicacion, descripcion, estado)
                    return redirect(url_for("cotizaciones"))

                return render_template("form_proyectos.html", error1=error1, error2=error2, error3=error3, error4=error4, error5=error5, error6=error6, error7=error7, error8=error8)

                

            

            




