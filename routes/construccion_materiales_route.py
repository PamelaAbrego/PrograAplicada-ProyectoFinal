from flask import redirect, render_template, request, session, url_for
from logic.formGruas_logic import GruasLogic
import bcrypt
import requests

class ConstruccionMateriales:
    @staticmethod
    def configure_routes(app):
        @app.route("/construccion_materiales", methods=["GET", "POST"])

        def construccion_materiales():
            if request.method == "GET":
                response = requests.get("https://apiprogra.herokuapp.com/construccion/equipo")
                equipo = []
                if response.status_code == 200:
                    equipo = response.json()
                response = requests.get("https://apiprogra.herokuapp.com/construccion/material")
                materiales = []
                if response.status_code == 200:
                    materiales = response.json()    
                response = requests.get("https://apiprogra.herokuapp.com/construccion/herramienta")
                herramientas = []
                if response.status_code == 200:
                    herramientas = response.json()                
                return render_template("construccion_materiales.html", equipo=equipo, materiales=materiales, herramientas=herramientas)
            elif request.method == "POST":
                pass
