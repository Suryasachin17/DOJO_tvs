from app.db_manager import DBManager

class BioService:
    """Handles logic related to bio data."""
    def __init__(self):
        self.db_manager = DBManager()
        
    def save_data(self, table_name, json_data):
        if table_name == "Examine_details":
            json_data_cc = json_data[0]
            print("Saving", json_data_cc)
            
            cc_no = json_data_cc.get("cc_no")
            response = []  # To collect the result of each entry
            for entry in json_data_cc.get("Safety_training", []):
                print(entry, "creating entry *******************")
                topics = entry["topic"]
                print(cc_no, topics, "312564")
                check_query = "SELECT COUNT(*) FROM Examine_details WHERE cc_no = %s AND topics = %s"
                count = self.db_manager.execute_query(check_query, (cc_no, topics))
                print(count, "tyyh")
                count = count[0]["COUNT(*)"]

                if count > 0:
                    update_columns = []
                    params = []
                    for column, value in entry.items():
                        if column not in ["ccno", "topic","targetScore","totalScore","si_no"]:
                            update_columns.append(f"{column} = %s")
                            params.append(value)
                    if update_columns:
                        update_query = f"""
                            UPDATE Examine_details 
                            SET {', '.join(update_columns)}
                            WHERE cc_no = %s AND topics = %s
                        """
                        params.extend([cc_no, topics])
                        print(update_columns, "/////", params, "1299885******************")
                        self.db_manager.execute_non_query(update_query, tuple(params))
                        # print(result, "/////")
                        response.append({"topic": topics, "action": "updated", "status": "success"})
                else:
                    # Insert a new row
                    print("insert into Examine_details")
                    insert_columns = []
                    placeholders = []
                    params = []

                    for column, value in entry.items():
                        insert_columns.append(column)
                        placeholders.append("%s")
                        params.append(value)

                    insert_query = """
                        INSERT INTO Examine_details (topics, cc_no, actual_score, status_, 
                                                    sign_by_trainee, sign_by_training_officer, Remarks) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """
                    params = (
                        topics,
                        cc_no,
                        entry["actual_score"],
                        entry["status_"],
                        entry["sign_by_trainee"],
                        entry["sign_by_training_officer"],
                        entry["Remarks"],
                    )
                    print(insert_query, params,"insert ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    self.db_manager.execute_non_query(insert_query, params)
                    response.append({"topic": topics, "action": "inserted", "status": "success"})

            # Return the cumulative response for all entries
            return {"status": "completed", "results": response}

        elif table_name == "Registration":
            response = []
            for entry in json_data.get("train", []):  # Iterate through the JSON array
                # Check if the `cc_no` already exists in the Registration table
                    cc_no = entry["cc_no"]
                    check_query = "SELECT COUNT(*) FROM Registration WHERE cc_no = %s"
                    count = self.db_manager.execute_query(check_query, (cc_no,))
                    count = count[0]["COUNT(*)"]
                    if count > 0:
                        # Update the existing row
                        update_query = """
                            UPDATE Registration 
                            SET name_ = %s, designation = %s, date_of_joining = %s, grade = %s,
                                year_passed_out = %s, college_name = %s, branch = %s, 
                                qualification = %s, photo = %s
                            WHERE cc_no = %s
                        """
                        params = (
                            entry["name"],
                            entry["Designation"],
                            entry["date_of_joining"],
                            entry["grade"],
                            entry["year_passed_out"],
                            entry["college_name"],
                            entry["Branch"],
                            entry["qualification"],
                            entry["photo"],
                            cc_no,
                        )
                        self.db_manager.execute_non_query(update_query, params)
                        
                        response.append({
                                            "cc_no": cc_no,
                                            "status": "updated",
                                            "message": "Registration details updated successfully."
                                        })
                    
                    else:
                        # Insert a new row
                        insert_query = """
                            INSERT INTO Registration (name_, cc_no, designation, date_of_joining, 
                                                    grade, year_passed_out, college_name, branch, 
                                                    qualification, photo) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        """
                        params = (
                            entry["name"],
                            cc_no,
                            entry["Designation"],
                            entry["date_of_joining"],
                            entry["grade"],
                            entry["year_passed_out"],
                            entry["college_name"],
                            entry["Branch"],
                            entry["qualification"],
                            entry["photo"],
                        )
                        self.db_manager.execute_non_query(insert_query, params)

                        response.append({
                                            "cc_no": cc_no,
                                            "status": "inserted",
                                            "message": "Registration details saved successfully."
                                        })
            return {
                    "status": "success",
                    "message": "Processed all registration details.",
                    "data": response
                } 
                    
            
                    