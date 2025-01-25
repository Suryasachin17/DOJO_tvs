from app.db_manager import DBManager
#best one
class BioService:
    """Handles logic related to bio data."""
    def __init__(self):
        self.db_manager = DBManager()
        
    def save_data(self, table_name, json_data):
        response = []
        if table_name == "Examine_details":
           
            json_data_cc = json_data[0]
            # print("Saving", json_data_cc)
            place = json_data_cc.get("place")
            date =json_data_cc.get("date") 
            cc_no = json_data_cc.get("cc_no")
            over_all_status = json_data_cc.get("over_all_status")
            # over_all_result = json_data_cc.get("over_all_result")
            # print("Overall result",over_all_result)
            
            if cc_no is not None:
                     # To collect the result of each entry
                    for entry in json_data_cc.get("Safety_training", []):
                        # print(entry, "creating entry *******************")
                        topics = entry["topic"]
                        # date = entry["date"]
                        # print(cc_no, topics, "312564")
                        check_query = "SELECT COUNT(*) FROM Examine_details WHERE cc_no = %s AND topics = %s"
                        count = self.db_manager.execute_query(check_query, (cc_no, topics))
                        # print(count, "tyyh")
                        count = count[0]["COUNT(*)"]

                        if count > 0:
                            update_columns = []
                            params = []
                            for column, value in entry.items():
                                # print(entry,"checking day  123 table")
                                if column not in ["ccno", "topic","targetScore","totalScore","si_no","status_"]:
                                    update_columns.append(f"{column} = %s")
                                    params.append(value)
                            update_columns.extend(("status_ = %s","date = %s","place = %s"))
                            if update_columns:
                                # print(update_columns,"updateddddddddddddddddddddddddddd")
                                update_query = f"""
                                    UPDATE Examine_details 
                                    SET {', '.join(update_columns)}
                                    WHERE cc_no = %s AND topics = %s
                                """
                                params.extend([over_all_status, date,place,cc_no, topics])
                                print(update_columns, "/////", params, "1299885******************")
                                self.db_manager.execute_non_query(update_query, tuple(params))
                                # print(result, "/////")
                                response.append({"topic": topics, "action": "updated", "status": "success","Message" : "Safety Training details updated successfully"})
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
                                                            sign_by_trainee, sign_by_training_officer, Remarks,date, place) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                            """
                            params = (
                                topics,
                                cc_no,
                                entry["actual_score"],
                                over_all_status,
                                entry["sign_by_trainee"],
                                entry["sign_by_training_officer"],
                                entry["Remarks"],
                                date,
                                place
                                
                            )
                            # print(insert_query, params,entry["date"],"insert ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                            self.db_manager.execute_non_query(insert_query, params)
                            response.append({"topic": topics, "action": "inserted", "status": "success","Message" : "Safety Training details updated successfully"})

                    # Return the cumulative response for all entries.
                    print(response,"status check")
                    return {
                        "Message" : response[0]["Message"],
                        "Status" : response[0]["status"]
                }
            else:
                response.append({ "status" : "fail","Message" : "No records found "})

                if response:
                        return {
                            "Message" : response[0]["Message"],
                            "Status" : response[0]["status"]
                        }
                else:
                        return {
                            "Message" : "No data processed",
                            "Status" : "Fail"
                        } 
             
                
                
                
        elif table_name == "Registration":
            response = []
            for entry in json_data.get("train", []):  # Iterate through the JSON array
                # Check if the `cc_no` already exists in the Registration table
                    cc_no = entry["cc_no"]
                    check_query = "SELECT COUNT(*) FROM Registration WHERE cc_no = %s"
                    count = self.db_manager.execute_query(check_query, (cc_no,))
                    count = count[0]["COUNT(*)"]
                    # photo = entry["photo"]
                    # if photo is not None:
                    #     if photo.startwith('data:image'):
                            
                    if count > 0:
                        # # Update the existing row
                        # print("Update reg")
                        # update_query = """
                        #     UPDATE Registration 
                        #     SET name_ = %s, designation = %s, date_of_joining = %s, grade = %s,
                        #         year_passed_out = %s, college_name = %s, branch = %s, 
                        #         qualification = %s, photo = %s
                        #     WHERE cc_no = %s
                        # """
                        # params = (
                        #     entry["name"],
                        #     entry["Designation"],
                        #     entry["date_of_joining"],
                        #     entry["grade"],
                        #     entry["year_passed_out"],
                        #     entry["college_name"],
                        #     entry["Branch"],
                        #     entry["qualification"],
                        #     entry["photo"],
                        #     cc_no,
                        # )
                        # self.db_manager.execute_non_query(update_query, params)
                        
                        response.append({
                                        "cc_no": cc_no,
                                        "status": "Failed",
                                        "message": f"User already  registered  {cc_no}.",
                                        "Action" : "Already register in  registration table"
                                    })
                    else:
                        # Insert a new row
                        insert_query = """
                            INSERT INTO Registration (name_, cc_no, designation, date_of_joining, 
                                                    grade, year_passed_out, college_name, branch, 
                                                    qualification, photo,existing_cc_no,is_existing) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
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
                            entry["previous_cc_no"],
                            entry["previously_worked"]
                        )
                        self.db_manager.execute_non_query(insert_query, params)

                        response.append({
                                            "cc_no": cc_no,
                                            "status": "Success",
                                            "message":   f"Registration for cc_no {cc_no} saved successfully.",
                                            "Action" : "Insert Updated"
                                        })
            print(response)
            return {
                    "status": response[0]["status"],
                    "message": response[0]["message"],
                    "Action": response[0]["Action"]
                } 
                    
            
                    