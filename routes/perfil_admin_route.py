from flask import redirect, render_template, request, session, flash
from logic.usuarios_logic import UsuariosLogic
import bcrypt


class PerfilAdmin:
    @staticmethod
    def configure_routes(app):
        @app.route("/perfil_admin", methods=["GET", "POST"])
        def perfil_admin():
            if request.method == "GET":
                logic = UsuariosLogic()
                dataUsers = logic.getAllUsers()
                return render_template("perfil_admin.html", user = session["login_user"], email= session["login_email"], dataUsers=dataUsers)
            elif request.method == "POST":
                logic = UsuariosLogic()
                user = request.form["user"]
                role = request.form.get("Cliente")
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
                        flash("**Usuario ingresado correctamente**", "perfil_admin")
                    else:
                        flash("Las contraseñas no coinciden.", "perfil_admin")
                else:
                    flash("**El usuario ya existe**", "perfil_admin")
                    return redirect("perfil_admin")
            return redirect("perfil_admin")