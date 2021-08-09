from core.pyba_logic import PybaLogic


class ProyectosLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    def insertProyecto(self, fecha_envio, tipo, usuario, numero, fecha_inicio, fecha_final, ubicacion, descripcion, estado):
        database = self.databaseObj
        sql = (
            "INSERT INTO `heroku_de080cfa793afc7`.`form_servicios` (`id`, `fecha_envio`,`tipo`,`usuario`,`numero`,`fecha_inicio`,`fecha_final`,`ubicacion`, `descripcion`, `estado`)"
            + f"VALUES(0, '{fecha_envio}', '{tipo}', '{usuario}', {numero}, '{fecha_inicio}', '{fecha_final}', '{ubicacion}', '{descripcion}', '{estado}' );"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def getProyectoById(self, id):
        database = self.databaseObj
        sql = f"SELECT * FROM heroku_de080cfa793afc7.form_servicios where id = {id};"
        result = database.executeQuery(sql)
        return result[0]

    def updateProyecto(self, id, proyecto):
        database = self.databaseObj
        sql = (
            "UPDATE `heroku_de080cfa793afc7`.`form_servicios` "
            + f"SET `tipo` = '{proyecto['tipo']}', `numero` = '{proyecto['numero']}', `fecha_inicio` = '{proyecto['fecha_inicio']}', `fecha_final` = '{proyecto['fecha_final']}', `ubicacion` = '{proyecto['ubicacion']}', `descripcion` = '{proyecto['descripcion']}',`comentario` = '{proyecto['comentario']}'"
            + f"WHERE `id` = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def deleteProyecto(self, id):
        database = self.databaseObj
        sql = f"DELETE FROM `heroku_de080cfa793afc7`.`form_servicios` WHERE id = {id};"
        rows = database.executeNonQueryRows(sql)
        return rows

    def getAllProyectos(self):
        database = self.databaseObj
        sql = f"SELECT * FROM heroku_de080cfa793afc7.form_servicios;"
        result = database.executeQuery(sql)
        return result

    def getDate(self):
        database = self.databaseObj
        sql = f"SELECT sysdate();"
        result = database.executeQuery(sql)
        return result

    def getAllByUser(self, user):
        database = self.databaseObj
        sql = f"SELECT * FROM heroku_de080cfa793afc7.form_servicios where usuario like '{user}';"
        result = database.executeQuery(sql)
        return result

    def changeEstado(self,id,option):
        database = self.databaseObj
        if option == '0':
            cambio = "Rechazado"
        elif option == '1':
            cambio = "Aceptado"
        
        sql = (
            "UPDATE `heroku_de080cfa793afc7`.`form_servicios` "
            + f"SET `estado` = '{cambio}' "
            + f"WHERE `id` = {id};"
        )

        rows = database.executeNonQueryRows(sql)
        return rows