from app.db_manager import DBManager
from app import logger


class memory:
    def __init__(self):
        self.db_manager = DBManager()
        
    def save_data(self,json_data):
            response = []

            cc_no = json_data.get('cc_no')
            if cc_no is not None:
                print(cc_no,"879456123")
                memory_test = json_data.get("memory_games", [])

                print(memory_test,"***************************//---*--*-//")
                if memory_test:  # Check if the list is not empty
                # Access the first dictionary in the list
                    memory_test_data = memory_test[0]

                    # Extract top-level fields
                    date = memory_test_data.get("date")
                    process_name = memory_test_data.get("process_name")
                    process_observation = memory_test_data.get("process_observation")
                    status = memory_test_data.get("status_")
                    sign_by_trainee = memory_test_data.get("sign", {}).get("sign_by_trainee")
                    sign_by_captain = memory_test_data.get("sign", {}).get("sign_by_line_captain")
                    remarks = memory_test_data.get("remarks")
                    place = memory_test_data.get("place")
                
                # Process all attempts in memory_test
                    for attemptssssss in memory_test_data.get("attempts",[]):
                        print(attemptssssss,"================================")
                        attempts =  attemptssssss.get("attempt_number")
                        mistake  =  attemptssssss.get("mistakes")
                        print(mistake,"check mistakes")
                        heart_test = attemptssssss.get("heart_test")
                        
                        # Check if record exists for cc_no and process_name combined with attempt_no
                        check_query = """
                        SELECT * FROM memory_details 
                        WHERE cc_no = %s AND  attempts = %s
                        """
                        existing_record = self.db_manager.execute_query(check_query, (cc_no,  attempts))
                        print(existing_record,"existing_record************************")
                        
                        if not existing_record:
                            # Insert new record
                            insert_query = """
                            INSERT INTO memory_details (
                                cc_no, process_name, process_obsevations, attempts, mistakes, heart_test, 
                                data_time, status_, sign_trainee, sign_team_leader, remarks, place
                            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                            """

                            try:
                                self.db_manager.execute_non_query(
                                    insert_query,
                                    (
                                        cc_no, 
                                        process_name,
                                        process_observation, 
                                        attempts, mistake, 
                                        heart_test, 
                                        date, status, sign_by_trainee, 
                                        sign_by_captain, remarks, place
                                    )
                                )
                                # print(f"Inserted new record for process_name: {process_name}, attempt_no: {attempts}")
                                logger.info(f"Inserted new record in memory table for process_name: {process_name}, attempt_no: {attempts}")
                                response.append({'action': "Inserted", "status": "success", "message": "memory games details saved successfully."})
                            except Exception as e:
                                logger.info("Failed to insert memory table  games", e)
                                response.append({'action': "Error", "status": "fail" ,"message":f"In memory table{str(e)}" })
                        else:
                            print("updated memory table")
                            # Update existing record
                            update_query = """
                            UPDATE memory_details
                            SET process_name = %s, mistakes = %s, heart_test = %s, data_time = %s, 
                                status_ = %s, sign_trainee = %s, sign_team_leader = %s, 
                                process_obsevations = %s,remarks = %s, place = %s
                            WHERE cc_no = %s AND attempts = %s
                            """
                        #                             try:
                        #     self.db_manager.execute_non_query(insert_query, params)
                        #     response.append({'action': "Inserted", "status": "success", "message": "Cycle games details saved successfully."})
                        # except Exception as e:
                        #     logger.info("Failed to insert big table cycle games", e)
                        #     response.append({'action': "Error", "status": "fail" ,"message": str(e)})
                            
                            try:
                                self.db_manager.execute_non_query(
                                    update_query,
                                    (
                                    process_name, mistake, heart_test, date, status, sign_by_trainee, 
                                        sign_by_captain, process_observation, remarks, place, cc_no, attempts
                                    )
                                )
                                logger.info(f"Updated existing record in memory table for process_name attempt_no: {attempts}")
                                # print(f"Updated existing record for process_name: {process_name}, attempt_no: {attempts}")
                                response.append({'action': "updated", "status": "success", "message": "memory games details inserted successfully."})
                                
                                
                            except Exception as e:
                                logger.info("Failed to update memory table  games", e)
                                response.append({'action': "Error", "status": "fail" ,"message":f"In update memory table{str(e)}" })
                    if response:
                   
                        return {
                        "Message" : response[0]["message"],
                        "Status" : response[0]["status"]
                    }
                    else:
                        return {
                            "Message" : "No data processed",
                            "Status" : "fail"
                        }
            
                            
            else:  
                response.append({'action': "cc_no type", "status": "fail", "message": "No records found ."})                 
            # print(response)                 
            print("Save operation completed successfully.")
            if response:
               
                return {
                "Message" : response[0]["message"],
                "Status" : response[0]["status"]
            }
            else:
                return {
                    "Message" : "No data processed",
                    "Status" : "fail"
                }
            
