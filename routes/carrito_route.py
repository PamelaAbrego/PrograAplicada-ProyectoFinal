from flask import redirect, render_template, request, session, url_for
from logic.carrito_logic import CarritoLogic
import bcrypt
import requests

class Carrito:
    @staticmethod
    def configure_routes(app):
        @app.route("/carrito", methods=["GET", "POST"])

        def carrito():
            if request.method == "GET":
                logic = CarritoLogic()
                user = session["login_user"]
                carrito = logic.getAllForUser(user)
                total = logic.getTotalByUser(user)["sum(total)"]
                return render_template("carrito.html", carrito = carrito, total = total)
            elif request.method == "POST":
                logic = CarritoLogic()
                id = request.form["id"]
                logic.deleteById(id)
                user = session["login_user"]
                carrito = logic.getAllForUser(user)
                total = logic.getTotalByUser(user)["sum(total)"]
                return render_template("carrito.html", carrito = carrito, total = total)