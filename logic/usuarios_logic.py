from core.pyba_logic import PybaLogic


class UsuariosLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    def insertUsuario(self, user, email, role, password, salt):
        database = self.databaseObj
        sql = (
            "INSERT INTO `heroku_de080cfa793afc7`.`usuarios` (`id`,`user`,`email`,`role`,`password`,`salt`)"
            + f"VALUES (0, '{user}', '{email}','{role}','{password}', '{salt}');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def getUsuarioId(self, id):
        database = self.databaseObj
        sql = f"SELECT * FROM heroku_de080cfa793afc7.usuarios where id = {id};"
        result = database.executeQuery(sql)
        return result

    def updateUsuario(self, id, usuario):
        database = self.databaseObj
        sql = (
            "UPDATE `heroku_de080cfa793afc7`.`usuarios` "
            + f"SET `user` = '{usuario['user']}', `email` = '{usuario['email']}',`role` = '{usuario['role']}', `password` = '{usuario['password']}', `salt` = '{usuario['salt']}' "
            + f"WHERE `id` = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def deleteUsuario(self, id):
        database = self.databaseObj
        sql = f"DELETE FROM `heroku_de080cfa793afc7`.`usuarios` WHERE id = {id};"
        rows = database.executeNonQueryRows(sql)
        return rows

    def checkUser(self, user):
        database = self.databaseObj
        sql = f"SELECT user FROM `heroku_de080cfa793afc7`.`usuarios` WHERE user like '{user}';"
        result = database.executeQuery(sql)
        return result

    def getUserByName(self, userName):
        database = self.createDatabaseObj()
        sql = (
            "SELECT user, password, salt, role "
            + f"FROM heroku_de080cfa793afc7.usuarios where user like '{userName}';"
        )
        result = database.executeQuery(sql)
        if len(result) > 0:
            return result[0]
        else:
            return []

    def getEmailByName(self, userName):
        database = self.createDatabaseObj()
        sql = (
            "SELECT email "
            + f"FROM heroku_de080cfa793afc7.usuarios where user like '{userName}';"
        )
        result = database.executeQuery(sql)
        if len(result) > 0:
            return result[0]["email"]
        else:
            return []

    def getAllUsers(self):
        database = self.createDatabaseObj()
        sql = (
            "SELECT * "
            + f"FROM heroku_de080cfa793afc7.usuarios;"
        )
        result = database.executeQuery(sql)
        if len(result) > 0:
            return result
        else:
            return []


