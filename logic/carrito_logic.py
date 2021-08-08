from core.pyba_logic import PybaLogic


class CarritoLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    def insertCarrito(self, user, producto, precio, cantidad):
        database = self.databaseObj
        total = precio*cantidad
        sql = (
            "INSERT INTO `comsedi`.`carrito` (`id`,`usuario`,`producto`,`precio`,`cantidad`,`total`)"
            + f"VALUES (0, '{user}', '{producto}','{precio}','{cantidad}', '{total}');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def getAllForUser(self, user):
        database = self.databaseObj
        sql = (
            f"SELECT * FROM comsedi.carrito WHERE usuario like '{user}';"
        )
        data = database.executeQuery(sql)
        return data

    def getTotalByUser(self, user):
        database = self.databaseObj
        sql = (
            f"SELECT sum(total) FROM comsedi.carrito WHERE usuario like '{user}';"
        )
        total = database.executeQuery(sql)
        return total[0]

    def deleteById(self, id):
        database = self.databaseObj
        sql = f"DELETE FROM `comsedi`.`carrito` WHERE id = {id};"
        database.executeNonQueryRows(sql)