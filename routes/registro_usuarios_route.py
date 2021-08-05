from flask import redirect, render_template, request, session, flash
from logic.usuarios_logic import UsuariosLogic
import bcrypt


class RegistroUsuarios:
    @staticmethod
    def configure_routes(app):
        @app.route("/registro_usuarios", methods=["GET", "POST"])
        def registro_usuarios():
            if request.method == "GET":
                logic = UsuariosLogic()
                dataUsers = logic.getAllUsers()
                return render_template("registro_usuarios.html", user = session["login_user"], email= session["login_email"], dataUsers=dataUsers)
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
                        flash("**Usuario ingresado correctamente**", "registro_usuarios")
                        return redirect("registro_usuarios")
                    else:
                        flash("Las contraseñas no coinciden.", "registro_usuarios")
                        return redirect("registro_usuarios")
                else:
                    flash("**El usuario ya existe**", "registro_usuarios")
                    return redirect("registro_usuarios")
            return redirect("registro_usuarios")