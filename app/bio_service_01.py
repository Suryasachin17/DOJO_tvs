from app.db_manager import DBManager

class BioService:
    """Handles logic related to bio data."""
    def __init__(self):
        self.db_manager = DBManager()
    
    def save_bio(self, bio_data):
        """Saves bio data to the database."""
        query = "INSERT INTO Registration (name_, cc_no, designation, date_of_joining, grade, year_passed_out,college_name, branch, qualification, photo ) VALUES (%s,%s, %s, %s, %s,%s , %s, %s, %s,%s)"
        
        for category, entries in bio_data.items():
            print(query, category, entries)
            for entry in entries:
                params = (entry["name"],
            entry["cc_no"],
            entry["Designation"],
            entry["date_of_joining"],
            entry["grade"],
            entry["year_passed_out"],
            entry["college_name"],
            entry["Branch"],
            entry["qualification"],
            entry["photo"])
                self.db_manager.execute_non_query(query, params)
                
        # query = "INSERT INTO Examine_details (topics,cc_no, actual_score, status_, sign_by_trainee,sign_by_training_officer,Remarks ) VALUES (%s,%s, %s, %s, %s , %s, %s)"

        # for category, entries in bio_data.items():
        #     print(query, category, entries,"*********************")
        #     for entry in entries:
        #         if 
        #         params = (entry["Topic"] , entry['ccno'],entry['Actual_Score'], entry['Status'], entry['sign_by_trainee'],entry['sign_by_training_officer'], entry['Remarks'])
        #         self.db_manager.execute_non_query(query, params)
        
        return self.db_manager
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
