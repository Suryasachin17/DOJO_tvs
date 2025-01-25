from app.db_manager import DBManager
from app import logger
import pprint

class big_table_test:
    def __init__(self):
        self.db_manager = DBManager()
        # pass

    def save_data(self, json_data):
        response = []
        json_data_cc = json_data
        cc_no = json_data_cc.get('cc_no')
        if cc_no is not None:
                date = json_data_cc.get('date')
                place = json_data_cc.get("place")
                # date = entry.get("date","")
                for entry in json_data_cc.get("Cycle_games"):
                    existing_attempt = 0
                    print(entry,"to check")
                    task_id = entry["task_id"]
                    Task_id_status = entry["status_"]
                    # place = entry["place"]
                    signature = entry.get("sign",{})
                    Signature_by_Trainee = signature.get("Signature_by_Trainee",None)
                    print(Signature_by_Trainee)
                    Signature_by_Process_Coach = signature.get("Signature_by_Process_Coach",None)
                    Signature_by_Training_Officer = signature.get("Signature_by_Training_Officer",None)
                    print(Signature_by_Trainee,"*/*/*/*/*/*/*/*/*//")
                    
                    check_query = "SELECT * FROM attempts WHERE cc_no = %s AND task_id = %s"
                    existing_record  = self.db_manager.execute_query(check_query, (cc_no, task_id))
                    print(existing_record,"existing type")
                    
                    
                    
                    # count = count[0]["COUNT(*)"]
                    
                    for attempts in entry.get("attempts"):
                        
                        print("insert big table")
                        attempt_number = attempts["attempt_number"]
                        pf_status =  attempts["pf_status"]
                        if  attempts["mistakes"].strip() == "":
                             mistakes  = None
                        else:
                             mistakes  =  int(attempts["mistakes"])
                             
                        if  attempts["cycle_time"].strip() == "":
                             mistakes  =  None
                        else:
                             cycle_time  =   int(attempts["cycle_time"])
                            
                        # mistakes  =  attempts["mistakes"]
                        # cycle_time = attempts["cycle_time"]
                        # print(cycle_time.strip(),"cycle time)))))))))))))))))))))))))))))))")
                        print(existing_record,"existing_record  ------------")
                        if not  existing_record :
                        
                            
                            insert_query = """INSERT INTO attempts (task_id, attempt_number, pf_status, mistakes, cc_no, status_, Signature_by_Trainee, Signature_by_Process_Coach, Signature_by_Training_Officer, cycle_time, date,place) 
                                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s , %s, %s)"""
                            
                            params = (
                                task_id,
                                attempt_number,
                                pf_status,
                                mistakes,
                                cc_no,
                                Task_id_status,
                                Signature_by_Trainee, 
                                Signature_by_Process_Coach,
                                Signature_by_Training_Officer,
                                cycle_time,
                                date,
                                place
                            )
                            try:
                                self.db_manager.execute_non_query(insert_query, params)
                                response.append({'action': "Inserted", "status": "success", "message": "Cycle games details saved successfully."})
                            except Exception as e:
                                logger.info("Failed to insert big table cycle games", e)
                                response.append({'action': "Error", "status": "fail" ,"message": str(e)})
                        else:
                            # Update existing record
                            print("update big table")
                            update_field =[]
                            update_value = []
                            # print(existing_record,"existing_record -------------exxx")
                            # pp = pprint.PrettyPrinter(width=50, compact=True)
                            # pp.pprint(existing_record)  
                            # # print(cycle_time.strip(),cycle_time,"*/*///*/*//*/*//")
                            # for index,details in enumerate(existing_record):
                            if pf_status != existing_record[attempt_number- 1]["pf_status"]:
                                    update_field.append("pf_status = %s")
                                    update_value.append(pf_status)
                            if mistakes != existing_record[attempt_number - 1]["mistakes"]:
                                    update_field.append("mistakes = %s")
                                    update_value.append(mistakes)
                            if Task_id_status  != existing_record[attempt_number -1]["status_"]:
                                    update_field.append("status_ = %s")
                                    update_value.append(Task_id_status)
                            if place != existing_record[attempt_number - 1]["place"]:
                                    update_field.append("place = %s")
                                    update_value.append(place)
                            if date  != existing_record[attempt_number - 1]["date"]:
                                    update_field.append("date = %s")
                                    update_value.append(date)
                            if Signature_by_Trainee != existing_record[attempt_number - 1]["Signature_by_Trainee"]:
                                    update_field.append("Signature_by_Trainee = %s")
                                    update_value.append(Signature_by_Trainee)
                            if Signature_by_Process_Coach != existing_record[attempt_number - 1]["Signature_by_Process_Coach"]:
                                    update_field.append("Signature_by_Process_Coach = %s")
                                    update_value.append(Signature_by_Process_Coach)
                            if Signature_by_Training_Officer != existing_record[attempt_number - 1]["Signature_by_Training_Officer"]:
                                    update_field.append("Signature_by_Training_Officer = %s")
                                    update_value.append(Signature_by_Training_Officer)
                                        
                            # pp = pprint.PrettyPrinter(width=41, compact=True)
                            # pp.pprint(cycle_time)  
                            # print(int(cycle_time) , int(existing_record[0]["cycle_time"]),"check_cycle_time")
                            # print(cycle_time,existing_record[attempt_number - 1]["cycle_time"],"------>mis",mistakes, existing_record[attempt_number - 1]["mistakes"],"checking in big tablev------------")      
                            if cycle_time != existing_record[0]["cycle_time"]:
                                    update_field.append("cycle_time = %s")
                                    update_value.append(cycle_time)
                            # print(update_field,update_value,attempt_number,"789564123")
                            if update_field:
                                # update_query = ','.join(update_field)
                                update_query = f"""
                                    UPDATE attempts 
                                    SET  {','.join(update_field)}
                                    WHERE cc_no = %s AND task_id = %s AND attempt_number = %s
                                """
                                update_value.extend([cc_no, task_id, attempt_number])
                                try:
                                    # print(update_query,update_field,update_value,attempt_number,"sql check ***********")
                                    self.db_manager.execute_non_query(update_query, tuple(update_value))
                                    response.append({'action': "Updated", "status": "success" ,"message": "Cycle games details saved successfully."})
                                except Exception as e:
                                    logger.info("Failed to update big table cycle games", e)
                                    response.append({'action': "Error", "status": "fail" ,"message": str(e)})
                                    
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
            response.append({ "status" : "fail","message" : "No records found ."})

            if response:
                    return {
                        "Message" : response[0]["message"],
                        "Status" : response[0]["status"]
                    }
            else:
                    return {
                        "Message" : "No data processed",
                        "Status" : "Fail"
                    } 
             
             
                    
                    
                    
                    
                    