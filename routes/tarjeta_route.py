from flask import redirect, render_template, request, session, url_for, flash
from logic.carrito_logic import CarritoLogic
import bcrypt
import requests

class Tarjeta:
    @staticmethod
    def configure_routes(app):
        @app.route("/tarjeta", methods=["GET", "POST"])

        def tarjeta():
            if request.method == "GET":
                return render_template("tarjeta.html")
            elif request.method == "POST":
                restapi = "https://credit-card-auth-api-cerberus.herokuapp.com"
                endpoint = "/card/"
                cardId = request.form["numero"]
                url = f"{restapi}{endpoint}{cardId}"
                response = requests.get(url)
                dataJson = response.json()
                if response == "200":
                    flash("La tarjeta se encuentra activa", "tarjeta")
                else: 
                    flash("Error en la tarjeta")
                endpoint    = "/verify"

                url = f"{restapi}{endpoint}"
                logic = CarritoLogic()
                user = session["login_user"]
                total = logic.getTotalByUser(user)["sum(total)"]
                data = {
                    "name": request.form["nombre"],
                    "number": request.form["numero"],
                    "date": request.form["fecha"],
                    "code": request.form["codigo"],
                    "balance": total
                }

                response = requests.post(url, data=data)
                print(response)
                if response.status_code == 200:
                    dataJson = response.json()
                    if dataJson['response'] == '00':
                        flash("Compra realizada con éxito", "tarjeta")
                    elif dataJson['response'] == '61':
                        flash("Excede el limite de la tarjeta", "tarjeta")
            return redirect('tarjeta')