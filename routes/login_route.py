from flask import redirect, render_template, request, session, flash
from logic.usuarios_logic import UsuariosLogic
import bcrypt


class Login:
    @staticmethod
    def configure_routes(app):
        @app.route("/login", methods=["GET", "POST"])
        def login():
            if request.method == "GET":
                return render_template("login.html")
            elif request.method == "POST":
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
                else:
                    flash("El usuario ingresado no existe.", "login")
                    return redirect("login")
