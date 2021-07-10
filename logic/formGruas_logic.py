from core.pyba_logic import PybaLogic


class GruasLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    def insertFormGrua(self, usuario, modelo, cantidad, ubicacion, fecha, tiempo, estado):
        database = self.databaseObj
        
        sql = (
            "INSERT INTO `comsedi`.`form_gruas` (`id`, `usuario`, `modelo`, `cantidad`, `ubicacion`, `fecha`, `tiempo`, `estado`)"
            + f"VALUES(0, '{usuario}', '{modelo}', '{cantidad}', '{ubicacion}', '{fecha}', '{tiempo}', '{estado}' );"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def getFormGruaById(self, id):
        database = self.databaseObj
        sql = f"SELECT * FROM comsedi.form_gruas where id = {id};"
        result = database.executeQuery(sql)
        return result

    def updateFormGrua(self, id, formGrua):
        database = self.databaseObj
        sql = (
            "UPDATE `comsedi`.`form_gruas` "
            + f"SET `usuario` = '{formGrua['usuario']}', `modelo` = '{formGrua['modelo']}', `cantidad` = '{formGrua['cantidad']}', `ubicacion` = '{formGrua['ubicacion']}', `fecha` = '{formGrua['fecha']}', `tiempo` = '{formGrua['tiempo']}', `estado` = '{formGrua['estado']}' "
            + f"WHERE `id` = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def deleteFormGrua(self, id):
        database = self.databaseObj
        sql = f"DELETE FROM `comsedi`.`form_gruas` WHERE id = {id};"
        rows = database.executeNonQueryRows(sql)
        return rows

    def getAllFormGruas(self):
        database = self.databaseObj
        sql = f"SELECT * FROM comsedi.form_gruas;"
        result = database.executeQuery(sql)
        return result

    def getAllByUser(self, user):
        database = self.databaseObj
        sql = f"SELECT * FROM comsedi.form_gruas where usuario like '{user}';"
        result = database.executeQuery(sql)
        return result

    def changeEstado(self,id,option):
        database = self.databaseObj
        if option == '0':
            cambio = "Rechazado"
        elif option == '1':
            cambio = "Aceptado"
        
        sql = (
            "UPDATE `comsedi`.`form_gruas` "
            + f"SET `estado` = '{cambio}' "
            + f"WHERE `id` = {id};"
        )

        rows = database.executeNonQueryRows(sql)
        return rows