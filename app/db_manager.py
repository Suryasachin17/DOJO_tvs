import mysql.connector
from app.config import Config
from app import logger

class DBManager:
    """Manages database connections and queries."""
    def __init__(self):
        self.db = mysql.connector.connect(
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            database=Config.DB_NAME,
            port=Config.DB_PORT
        )
        if self.db:
            logger.info("DB Connected Succesfully")
    
    # def execute_query(self, query, params=None):
    #     """Executes a query with optional parameters."""
    #     cursor = self.db.cursor(dictionary=True, buffered=False)
    #     print(query, params,"check to what goinh ------------------------ database")
    #     cursor.execute(query, params)
    #     # self.db.commit()
    #     # print(cursor.fetchall(),"*************************************")
    #     results = cursor.fetchall()
    #     print(results,"^^^^^^^^^^^^^^^^^^^^^^^^ execute_query^^^^^^^^^^^^^^^^^^^^^^^^^")
    #     # self.db.autocommit(True)
    #     cursor.close()
    #     logger.info(" execute__query : Query executed successfully")
    #     return results
            
    def execute_query(self, query, params=None):
            """Executes a query with optional parameters."""

            self.db.commit()  # Ensure changes are committed before fetching data
            cursor = self.db.cursor(dictionary=True, buffered=False)
            print(query, params, "check to what going ------------------------ database")
            cursor.execute(query, params)
            results = cursor.fetchall()
            print(results, "^^^^^^^^^^^^^^^^^^^^^^^^ execute_query^^^^^^^^^^^^^^^^^^^^^^^^^")
            cursor.close()
            logger.info("execute_query: Query executed successfully")
            return results

            
    
    def execute_non_query(self, query, params=None):
        """Executes a query that does not return results (e.g., INSERT/UPDATE)."""
        cursor = self.db.cursor()
        cursor.execute(query, params)
        
        print("execute_non _query                INSERT")
        self.db.commit()
        cursor.close()
        logger.info(" execute_non_query : Query executed successfully")
        
    def close_connection(self):
        """Closes the database connection."""
        self.db.close()
