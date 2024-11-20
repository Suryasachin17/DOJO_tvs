from app.bio_service import BioService

def main():
    bio_service = BioService()
    
    # Example bio data from API
    bio_data = {
        "A": [{"Total_mark": 40, "Target": 50, "Status": True}],
        "B": [{"Total_mark": 40, "Target": 50, "Status": True}],
        "C": [{"Total_mark": 10, "Target": 40, "Status": False}]
    }
    
    # Save bio data to DB
    bio_service.save_bio(bio_data)
    print("Bio data saved to the database.")
    
    # Fetch bio data from DB
    fetched_bio = bio_service.fetch_bio()
    print("Fetched bio data:", fetched_bio)

if __name__ == "__main__":
    main()
