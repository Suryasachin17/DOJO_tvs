from app.db_manager import DBManager

class BioService:
    """Handles logic related to bio data."""
    def __init__(self):
        self.db_manager = DBManager()
    
    def save_bio(self, bio_data):
        """Saves bio data to the database."""
        query = "INSERT INTO bio_data (category, total_mark, target, status) VALUES (%s, %s, %s, %s)"
        
        for category, entries in bio_data.items():
            for entry in entries:
                params = (category, entry['Total_mark'], entry['Target'], entry['Status'])
                self.db_manager.execute_non_query(query, params)
    
    def fetch_bio(self):
        """Fetches bio data from the database."""
        query = "SELECT * FROM bio_data"
        results = self.db_manager.execute_query(query)
        
        # Reformat results into original structure
        bio = {}
        for row in results:
            category = row['category']
            entry = {
                "Total_mark": row['total_mark'],
                "Target": row['target'],
                "Status": row['status']
            }
            if category not in bio:
                bio[category] = []
            bio[category].append(entry)
        return bio
