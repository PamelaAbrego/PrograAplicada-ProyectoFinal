from core.pyba_logic import PybaLogic


class UsuariosLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    def insertUsuario(self, usuario):
        database = self.databaseObj
        sql = (
            "INSERT INTO `comsedi`.`usuarios` (`id`,`user`,`email`,`password`,`salt`)"
            + f"VALUES (0, '{usuario['user']}', '{usuario['email']}', '{usuario['password']}', '{usuario['salt']}');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def getUsuarioId(self, id):
        database = self.databaseObj
        sql = f"SELECT * FROM comsedi.usuarios where id = {id};"
        result = database.executeQuery(sql)
        return result

    def updateUsuario(self, id, usuario):
        database = self.databaseObj
        sql = (
            "UPDATE `comsedi`.`usuarios` "
            + f"SET `user` = '{usuario['user']}', `email` = '{usuario['email']}', `password` = '{usuario['password']}', `salt` = '{usuario['salt']}' "
            + f"WHERE `id` = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def deleteUsuario(self, id):
        database = self.databaseObj
        sql = f"DELETE FROM `comsedi`.`usuarios` WHERE id = {id};"
        rows = database.executeNonQueryRows(sql)
        return rows
