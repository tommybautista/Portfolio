from datetime import date
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Event:
    db_name = 'jototools'

    def __init__(self,db_data):
        self.id = db_data['id']
        self.event = db_data['event']        
        self.link = db_data['link']
        self.price = db_data['price']        
        self.total = db_data['total']
        self.user_id = db_data['user_id']        
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']


    @classmethod
    def save(cls,data):
        query = "INSERT INTO budgets (event, link, price, total, user_id) VALUES (%(event)s, %(link)s, %(price)s, %(total)s, %(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)  

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM budgets;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        all_budgets = []
        for row in results:
            all_budgets.append( cls(row) )
        return all_budgets
    

    @classmethod
    def update(cls, data):
        query = 'UPDATE budgets SET event = %(event)s, link = %(link)s, price = %(price)s, total = %(total)s, user_id = %(user_id)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db_name).query_db(query, data)


    @classmethod
    def destroy(cls,data):
        query  = "DELETE FROM budgets WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    # @classmethod
    # def get_one(cls, data):
    #     query = 'SELECT * FROM budgets WHERE id = %(id)s;'
    #     results =  connectToMySQL(cls.db_name).query_db(query, data)
    #     if len(results) < 1:
    #         return False
    #     return cls(results[0])

    @classmethod
    def get_budgets_by_user(cls, data):
        query = 'SELECT * FROM budgets WHERE user_id = %(id)s ORDER BY date ASC;'
        results =  connectToMySQL(cls.db_name).query_db(query, data)
        all_budgets = []
        for row in results:
            all_budgets.append(cls(row))
            if len(all_budgets) < 1:
                return False
        return all_budgets

    @classmethod
    def get_one(cls, data):
        query = 'SELECT * FROM budgets WHERE id = %(id)s;'
        results =  connectToMySQL(cls.db_name).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
    

