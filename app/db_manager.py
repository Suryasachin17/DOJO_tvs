import mysql.connector
from app.config import Config


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
    
    def execute_query(self, query, params=None):
        """Executes a query with optional parameters."""
        cursor = self.db.cursor(dictionary=True)
        cursor.execute(query, params)
        results = cursor.fetchall()
        cursor.close()
        return results
    
    def execute_non_query(self, query, params=None):
        """Executes a query that does not return results (e.g., INSERT/UPDATE)."""
        cursor = self.db.cursor()
        cursor.execute(query, params)
        self.db.commit()
        cursor.close()

    def close_connection(self):
        """Closes the database connection."""
        self.db.close()
