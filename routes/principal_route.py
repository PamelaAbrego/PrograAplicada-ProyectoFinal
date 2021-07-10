from flask import redirect, render_template, request, session, flash
import bcrypt

class Principal:
    @staticmethod
    def configure_routes(app):
        @app.route("/principal", methods=["GET", "POST"])
        def principal():
            if request.method == "GET":
                return render_template("principal.html")
            elif request.method == "POST":
                role = session["login_role"]
                if role == "Cliente":
                    return redirect("perfil_cliente")
                if role == "Administrador":
                    return redirect("perfil_admin")