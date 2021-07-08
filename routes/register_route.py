from flask import redirect, render_template, request, flash
from logic.usuarios_logic import UsuariosLogic
import bcrypt


class Register:
    @staticmethod
    def configure_routes(app):
        @app.route("/register", methods=["GET", "POST"])
        def register():
            if request.method == "GET":
                return render_template("register.html")
            elif request.method == "POST":
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
                        flash("No pudimos verificar las credenciales", "registro")
                        flash("Verifica que los datos esten correctos", "registro")
                        return redirect("register")
                else:
                    return redirect("register")
            return redirect("login")
