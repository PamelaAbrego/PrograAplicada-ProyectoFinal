from flask import redirect, render_template, request, session, flash
from logic.usuarios_logic import UsuariosLogic
import bcrypt
import requests


class Login:
    @staticmethod
    def configure_routes(app):
        data = {}
        @app.route("/login", methods=["GET", "POST"])
        def login():
            if request.method == "GET":
                return render_template("login.html")
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
                        userName = request.form["user"]
                        result = logic.checkUser(userName)
                        if len(result) > 0:    
                            password = request.form["password"]
                            userDict = logic.getUserByName(userName)
                            role = userDict["role"]
                            salt = userDict["salt"].encode("utf-8")
                            hashPasswd = bcrypt.hashpw(password.encode("utf-8"), salt)
                            dbPasswd = userDict["password"].encode("utf-8")
                            if len(userName) == 0 or len(password) == 0:
                                flash("Todos los campos son obligatorios.", "login")
                                return redirect("login")
                            else:
                                if hashPasswd == dbPasswd:
                                    session["login_user"] = userName
                                    session["login_email"] = logic.getEmailByName(userName)
                                    session["login_role"] = role
                                    session["loggedIn"] = True
                                    return redirect("principal")
                                else:
                                    flash("Contraseña incorrecta", "login")
                                    return redirect("login")
                                return "posted login"
                        elif len(result) == 0:
                            flash("Todos los campos son obligatorios.", "login")
                            return redirect("login")
                        else:
                            flash("El usuario ingresado no existe.", "login")
                            return redirect("login")
                    return redirect("login")
                else: return "not success"
            else:
                return f"error"
