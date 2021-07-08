from core.pyba_logic import PybaLogic


class ProyectosLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    def insertProyecto(self, fecha_envio, tipo, usuario, numero, fecha_inicio, fecha_final, ubicacion, descripcion, estado):
        database = self.databaseObj
        sql = (
            "INSERT INTO `comsedi`.`form_servicios` (`id`,`fecha_envio`,`tipo`,`usuario`,`numero`,`fecha_inicio`,`fecha_final`,`ubicacion`, `descripcion`, `estado`)"
            + f"VALUES(0, '{fecha_envio}', '{tipo}', '{usuario}', {numero}, '{fecha_inicio}', '{fecha_final}', '{ubicacion}', '{descripcion}', '{estado}' );"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def getProyectoById(self, id):
        database = self.databaseObj
        sql = f"SELECT * FROM comsedi.form_servicios where id = {id};"
        result = database.executeQuery(sql)
        return result

    def updateProyecto(self, id, proyecto):
        database = self.databaseObj
        sql = (
            "UPDATE `comsedi`.`form_servicios` "
            + f"SET `fecha_envio` = '{proyecto['fecha_envio']}', `tipo` = '{proyecto['tipo']}', `usuario` = '{proyecto['usuario']}', `numero` = '{proyecto['numero']}', `fecha_inicio` = '{proyecto['fecha_inicio']}', `fecha_final` = '{proyecto['fecha_final']}', `ubicacion` = '{proyecto['ubicacion']}', `descripcion` = '{proyecto['descripcion']}', `estado` = '{proyecto['estado']}' "
            + f"WHERE `id` = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def deleteProyecto(self, id):
        database = self.databaseObj
        sql = f"DELETE FROM `comsedi`.`form_servicios` WHERE id = {id};"
        rows = database.executeNonQueryRows(sql)
        return rows

    def getAllProyectos(self):
        database = self.databaseObj
        sql = f"SELECT * FROM comsedi.form_servicios;"
        result = database.executeQuery(sql)
        return result

    def getDate(self):
        database = self.databaseObj
        sql = f"SELECT sysdate();"
        result = database.executeQuery(sql)
        return result
