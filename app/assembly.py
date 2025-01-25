from app.db_manager import DBManager
from app import logger
import json

# class assemble_table:
#     def __init__(self):
#         self.db_manager = DBManager()
        
#     def save_data(self,json_data):
#             response = []

#             cc_no = json_data.get('cc_no')
#             assemble_test = json_data.get("assemble_test", [])

            
#             if assemble_test:  # Check if the list is not empty
#             # Access the first dictionary in the list
#                 assemble_test_data = assemble_test[0]

#                 # Extract top-level fields
#                 date = assemble_test_data.get("date")
#                 assembling  = assemble_test_data.get("assembling")
#                 status = assemble_test_data.get("status_")
#                 sign_by_trainee = assemble_test_data.get("sign",{}).get("sign_by_trainee")
#                 sign_by_line_captain  = assemble_test_data.get("sign", {}).get("sign_by_line_captain")
#                 # remarks = assemble_test_data.get("remarks")
#                 target_score = assemble_test_data.get("target_score")
#                 actual_score = assemble_test_data.get("actual_score")

#             # Process all attempts in memory_test
#                 for attempt_data  in assemble_test_data.get("attempts",[]):
#                     print(attempt_data ,"================================")
#                     attempts =  attempt_data .get("attempt_number")
#                     design_cycle_time = attempt_data.get("design_cycle_time")
#                     mistakes  =  attempt_data .get("mistakes")
#                     cycle_time = attempt_data.get("cycle_time")
#                     process_id  = attempt_data.get("process_id")
#                     process_completed  = attempt_data.get("process_completed")
#                     remarks = attempt_data.get("remarks")
#                     # Check if record exists for cc_no and process_name combined with attempt_no
#                     print(cc_no,attempts)
#                     check_query = """
#                     SELECT * FROM assembly 
#                     WHERE cc_no = %s AND  attemmpt = %s
#                     """
#                     existing_record = self.db_manager.execute_query(check_query, (cc_no,  attempts))
#                     print(existing_record,"existing_record************************")
                    
#                     if not existing_record:
#                         # Insert new record
#                             insert_query = """
#                             INSERT INTO assembly (
#                             cc_no, process_id, process_completed, assembling, design_cycle_time,
#                             attemmpt, mistakes, cycle_time, target_score, actual_score,
#                             status_, sign_by_trainee, sign_by_line_captain, remarks, date_
#                             ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#                             """

#                             try:
#                                 self.db_manager.execute_non_query(
#                                     insert_query,
#                                     (
#                                         cc_no, process_id, process_completed, assembling, design_cycle_time,
#                                         attempts, mistakes, cycle_time, target_score, actual_score,
#                                         status, sign_by_trainee, sign_by_line_captain, remarks, date
#                                     )
#                                 )
#                                 logger.info(f"Inserted new record in assembly table for process_id: {process_id}, attempt: {attempts}")
#                                 response.append({'action': "Inserted", "status": "success", "message": "Assembly details saved successfully."})
#                             except Exception as e:
#                                 logger.error("Failed to insert assembly data", e)
#                                 response.append({'action': "Error", "status": "fail", "message": f"In assembly table: {str(e)}"})
#                     else:
#  # Update existing record
#                         update_query = """
#                         UPDATE assembly
#                         SET process_id = %s, process_completed = %s, assembling = %s, design_cycle_time = %s,
#                             mistakes = %s, cycle_time = %s, target_score = %s, actual_score = %s,
#                             status_ = %s, sign_by_trainee = %s, sign_by_line_captain = %s, remarks = %s, date_ = %s
#                         WHERE cc_no = %s AND attemmpt = %s
#                         """

#                         try:
#                             self.db_manager.execute_non_query(
#                                 update_query,
#                                 (
#                                     process_id, process_completed, assembling, design_cycle_time,
#                                     mistakes, cycle_time, target_score, actual_score, status,
#                                     sign_by_trainee, sign_by_line_captain, remarks, date, cc_no, attempts
#                                 )
#                             )
#                             logger.info(f"Updated existing record in assembly table for process_id: {process_id}, attempt: {attempts}")
#                             response.append({'action': "Updated", "status": "success", "message": "Assembly details updated successfully."})
#                         except Exception as e:
#                             logger.error("Failed to update assembly data", e)
#                             response.append({'action': "Error", "status": "fail", "message": f"In update assembly table: {str(e)}"})
#             print("Save operation completed successfully.")
#             if response:
#                 print()
#                 return {
#                 "Messege" : response[0]["message"],
#                 "Status" : response[0]["status"]
#             }
#             else:
#                 return {
#                     "Messege" : "No data processed",
#                     "Status" : "Fail"
#                 }


# class CycleAchievements:
#     def __init__(self):
#         self.db_manager = DBManager()

#     def save_data(self, json_data):
#         response = []

#         cc_no = json_data.get('cc_no')
#         if cc_no is not None:
#             cycle_achievement = json_data.get("Cycle_time_achievement", [])
#             print(cycle_achievement)
#             if cycle_achievement:  # Check if the list is not empty
#                 # Access the first dictionary in the list
#                 assemble_test_data = cycle_achievement[0]
#                 print(assemble_test_data)
#                 # Extract top-level fields
#                 dct = assemble_test_data.get("dct")
#                 print(dct,"dcttttttttttt")
#                 date = assemble_test_data.get("date")
#                 actual_score = assemble_test_data.get("actual_score")
#                 status = assemble_test_data.get("status_")
#                 remarks = assemble_test_data.get("remarks")
#                 process_name = assemble_test_data.get("process_name")
#                 demo_line_captain = assemble_test_data.get("demo_line_captain")
#                 demo_trainee = assemble_test_data.get("demo_trainee")
#                 skill_matrix = assemble_test_data.get("skill_matrix")
#                 cycle_achievementt = assemble_test_data.get("cycle_achievement")
#                 sign_by_trainee = assemble_test_data.get("sign", {}).get("Signature_by_Trainee")
#                 sign_by_line_captain = assemble_test_data.get("sign", {}).get("Signature_by_line_caption")
#                 sign_by_module_controller = assemble_test_data.get("sign", {}).get("Signature_by_module_controller")

#                 for attempt_data in assemble_test_data.get("attempts", []):
#                     print(attempt_data,"789546123")
#                     attempt_number = attempt_data.get("attempt_number")
#                     mistakes = attempt_data.get("mistakes")
#                     cycle_time = attempt_data.get("cycle_time")

#                     check_query = """
#                     SELECT * FROM cycle 
#                     WHERE cc_no = %s AND attempt = %s
#                     """
#                     existing_record = self.db_manager.execute_query(check_query, (cc_no, attempt_number))
#                     print(existing_record)
#                     if not existing_record:
#                         # Insert new record
#                         insert_query = """
#                         INSERT INTO cycle (
#                             cc_no, dct, actual_score, status_, remarks, 
#                             demo_line_captain, demo_trainee, cycle_achievementt, skill_matrix,
#                             sign_by_trainee, sign_by_line_captain, sign_by_module_controller,
#                             attempt, cycle_time, mistakes,process_name,date
#                         ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#                         """
#                         try:
#                             self.db_manager.execute_non_query(
#                                 insert_query,
#                                 (
#                                     cc_no, dct, actual_score, status, remarks, 
#                                     demo_line_captain, demo_trainee,cycle_achievementt, skill_matrix, 
#                                     sign_by_trainee, sign_by_line_captain,sign_by_module_controller, 
#                                     attempt_number, cycle_time, mistakes,process_name,date
#                                 )
#                             )
#                             response.append({'action': "Inserted", "status": "success", "message": "Record successfully inserted."})
                        
#                         except Exception as e:
#                             logger.info("Failed to insert data into cycle table.", exc_info=e)
#                             response.append({'action': "Error", "status": "fail", "message": f"Insertion error: {str(e)}"})
                        

#                     else:
#                         # Update existing record
#                         update_query = """
#                         UPDATE cycle
#                         SET dct = %s, status_ = %s, mistakes = %s, cycle_time = %s, 
#                             actual_score = %s, sign_by_trainee = %s, sign_by_line_captain = %s, cycle_achievementt = %s,
#                             sign_by_module_controller = %s, demo_line_captain = %s, demo_trainee = %s, remarks = %s,  process_name = %s,date = %s
#                         WHERE cc_no = %s AND attempt = %s
#                         """
#                         try:
#                             self.db_manager.execute_non_query(
#                                 update_query,
#                                 (
#                                     dct, status, mistakes, cycle_time, actual_score,
#                                     sign_by_trainee, sign_by_line_captain, cycle_achievementt, sign_by_module_controller,
#                                     demo_line_captain, demo_trainee, remarks,process_name,date , cc_no, attempt_number
#                                 )
#                             )
#                             response.append({'action': "Updated", "status": "success", "message": "cycle details updated successfully."})
#                             # Exit the loop after a successful update
#                         except Exception as e:
#                             logger.info("Failed to update cycle data", exc_info=e)
#                             response.append({'action': "Error", "status": "fail", "message": f"In update cycle table: {str(e)}"})
         
#                 if response:
#                         return {
#                         "Message": response[0]["message"],
#                         "Status": response[0]["status"]
#                     }
#                 else:
#                     return {
#                         "Message": "No data processed",
#                         "Status": "Fail"
#                     }        
#         else:
#             logger.info("Serach the cc_no then update")
#             response.append({'action': "Error", "status": "fail", "message": "No records found ."})
#             if response:
#                         return {
#                         "Message": response[0]["message"],
#                         "Status": response[0]["status"]
#                     }
#             else:
#                     return {
#                         "Message": "No data processed",
#                         "Status": "Fail"
#                     }        
            
class CycleAchievements:
    def __init__(self):
        self.db_manager = DBManager()

    def save_data(self,json_data):
        
        response = []
        settingup = json_data["Cycle_time_achievement"][0]
        cc_no = json_data.get('cc_no')
        print(cc_no)
        if cc_no is not None:
                attempt = 1
                station_name = settingup.get('process_name')
                dct = settingup.get('dct')
                status_ = settingup.get('status_')
                print(status_,dct,"assembly  .. comming inside. . . ..  .    ")
                remarks = settingup.get('remarks')
                date_ = settingup.get('date')
                place = settingup.get('place')
                print(station_name,place,date_,status_,dct,"assembly  .. comming inside. . . ..  .    ")
                actual_score = settingup.get('actual_score')
                demo_line_captain = settingup.get('demo_line_captain')
                demo_trainee = settingup.get('demo_trainee')
                cycle_achievement = settingup.get('cycle_achievement')
                skill_matrix = settingup.get('skill_matrix')
                process_name = settingup.get('process_name')
                signature_by_trainee = settingup.get('sign').get('Signature_by_Trainee')
                signature_by_line_caption = settingup.get('sign').get('Signature_by_line_caption')
                signature_by_module_controller = settingup.get('sign').get('Signature_by_module_controller')
                
                try:
                    # Insert or Update `tasks_cycle`
                    task_query = """
                        INSERT INTO tasks_cycle (
                        cc_no, station_name, place, dct, status_, remarks, date_, attempt,
                        actual_score, demo_line_captain, demo_trainee, cycle_achievement,
                        skill_matrix, process_name, signature_by_trainee, 
                        signature_by_line_caption, signature_by_module_controller
                        )
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        ON DUPLICATE KEY UPDATE
                                        
                        station_name = VALUES(station_name),
                        place = VALUES(place),
                        dct = VALUES(dct),
                        status_ = VALUES(status_),
                        remarks = VALUES(remarks),
                        date_ = VALUES(date_),
                        attempt = VALUES(attempt),
                        actual_score = VALUES(actual_score),
                        demo_line_captain = VALUES(demo_line_captain),
                        demo_trainee = VALUES(demo_trainee),
                        cycle_achievement = VALUES(cycle_achievement),
                        skill_matrix = VALUES(skill_matrix),
                        process_name = VALUES(process_name),
                        signature_by_trainee = VALUES(signature_by_trainee),
                        signature_by_line_caption = VALUES(signature_by_line_caption),
                        signature_by_module_controller = VALUES(signature_by_module_controller) ; """
                   
                    result =self.db_manager.execute_non_query(task_query, (
                        cc_no, station_name, place, dct, status_, remarks, date_, attempt,
                        actual_score, demo_line_captain, demo_trainee, cycle_achievement,
                        skill_matrix, process_name, signature_by_trainee, 
                        signature_by_line_caption, signature_by_module_controller
                        ))
                    parameters = (
                        cc_no, station_name, place, dct, status_, remarks, date_, attempt,
                        actual_score, demo_line_captain, demo_trainee, cycle_achievement,
                        skill_matrix, process_name, signature_by_trainee, 
                        signature_by_line_caption, signature_by_module_controller
                    )
                    print("Parameters passed to query:")
                    for param, value in zip(['cc_no', 'station_name', 'place', 'dct', 'status_', 'remarks', 
                                            'date_', 'attempt', 'actual_score', 'demo_line_captain', 'demo_trainee', 
                                            'cycle_achievement', 'skill_matrix', 'process_name', 
                                            'signature_by_trainee', 'signature_by_line_caption', 
                                            'signature_by_module_controller'], parameters):
                                            print(f"{param}: {value}")
                    print(cc_no, station_name, place, dct, status_, remarks, date_, attempt,
                        actual_score, demo_line_captain, demo_trainee, cycle_achievement,
                        skill_matrix, process_name, signature_by_trainee, 
                        signature_by_line_caption, signature_by_module_controller,"CHECK DB SAVING VARIABLES")
                    operation = "inserted" if result == 1  else  "updated"
                    # Get `task_id` for inserted/updated record
                    task_id_query = "SELECT task_id FROM tasks_cycle WHERE cc_no = %s AND attempt = %s"
                    task_id = self.db_manager.execute_query(task_id_query, (cc_no, attempt))[0]["task_id"]
                    print(task_id)
                    # Process attempts
                    for attempt_data in settingup["attempts"]:
                        print(attempt_data,"atempt")
                        attempt_number = attempt_data.get("attempt_number")
                        attempts_id = attempt_data.get("attempts_id"," ")
                        ji_demo_line_captain = attempt_data.get("JI_demo_line_captain")
                        mistakes = attempt_data.get("mistakes")
                        cycle_time = attempt_data.get("cycle_time")
                        # mistakes = ','.join(mistakes)
                        # cycle_time =  ','.join(cycle_time)
                        print(mistakes,cycle_time,"*****1****")
                        mistakes = json.dumps(mistakes)
                        cycle_time = json.dumps(cycle_time)
                        print(mistakes,cycle_time,"*********")
                        # Insert or Update `attempts_cycle`
                        attempts_query = """
                            INSERT INTO attempts_cycle (
                                task_id, attempt_number, attempts_id, ji_demo_line_captain, mistakes, cycle_time,cc_no
                            )
                            VALUES (%s, %s, %s, %s, %s, %s, %s)
                            ON DUPLICATE KEY UPDATE
                                ji_demo_line_captain = VALUES(ji_demo_line_captain),
                                mistakes = VALUES(mistakes),
                                cycle_time = VALUES(cycle_time),
                                cc_no = VALUES(cc_no);
                        """
                        self.db_manager.execute_non_query(attempts_query, (
                            task_id, attempt_number, attempts_id, ji_demo_line_captain, mistakes, cycle_time, cc_no
                        ))

                    operation = "inserted" if result == 1  else   "updated"

                    response.append({'status': "updated", "status": "success", "message": f"cycle games details {operation} successfully."})
                except Exception as e:
                    response.append({"status": "Error", "message": str(e)})

                return response
        else:
            return [{"status": "fail", "message": "No records found ."}]
