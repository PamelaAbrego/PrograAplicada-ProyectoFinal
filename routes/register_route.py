from flask import redirect, render_template, request, flash
from logic.usuarios_logic import UsuariosLogic
import bcrypt
import requests

class Register:
    @staticmethod
    def configure_routes(app):
        data = {}
        @app.route("/register", methods=["GET", "POST"])
        def register():
            if request.method == "GET":
                return render_template("register.html")
            elif request.method == "POST":
                data["secret"] = "6LczYSkbAAAAAClYlF0btM-Ng5UZIX7JW1x4JBFq"
                data["response"] = request.form["g-recaptcha-response"]
                response = requests.post(
                    "https://www.google.com/recaptcha/api/siteverify", params=data
                )
                if response.status_code == 200:
                    messageJson = response.json()
                    if messageJson["success"]:
                        logic = UsuariosLogic()
                        user = request.form["user"]
                        role = "Cliente"
                        result = logic.checkUser(user)
                        if len(result) == 0:
                            email = request.form["email"]
                            passwd = request.form["password"]
                            confPasswd = request.form["confPassword"]
                            if passwd == confPasswd:
                                salt = bcrypt.gensalt(rounds=8)
                                strsalt = salt.decode("utf-8")
                                encPassword = passwd.encode("utf-8")
                                hashPasswd = bcrypt.hashpw(encPassword, salt)
                                strPasswd = hashPasswd.decode("utf-8")
                                rows = logic.insertUsuario(user, email, role, strPasswd, strsalt)
                                return redirect("login")
                            else:
                                flash("Las contraseñas ingresadas no coinciden.", "registro")
                                return redirect("register")
                        else:
                            flash("El usuario ya existe.", "registro")
                            return redirect("register")
                    return redirect("login")
                else: return "not success"
            else:
                return f"error"
