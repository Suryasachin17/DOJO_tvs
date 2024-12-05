from app.db_manager import DBManager



class big_table_test:
    def __init__(self):
        self.db_manager = DBManager()
        # pass

    def save_data(self, json_data):
        response = []
        json_data_cc = json_data
        cc_no = json_data_cc.get('cc_no')
        
        for entry in json_data_cc.get("Cycle_games"):
            print(entry,"to check")
            task_id = entry["task_id"]
            Task_id_status = entry["status_"]
            signature = entry["sign"] 
            Signature_by_Trainee = signature["Signature_by_Trainee"]
            Signature_by_Process_Coach = signature["Signature_by_Process_Coach"]
            Signature_by_Training_Officer = signature["Signature_by_Training_Officer"]

            
            check_query = "SELECT COUNT(*) FROM attempts WHERE cc_no = %s AND task_id = %s"
            count = self.db_manager.execute_query(check_query, (cc_no, task_id))
            count = count[0]["COUNT(*)"]
            
            for attempts in entry.get("attempts"):
                print("insert big table")
                if count == 0:
                
                    print(task_id, attempts["attempt_number"],
                        attempts["pf_status"],
                        attempts["mistakes"],
                        cc_no,
                        )
                    insert_query = """INSERT INTO attempts (task_id, attempt_number, pf_status, mistakes, cc_no, status_,Signature_by_Trainee, Signature_by_Process_Coach,Signature_by_Training_Officer,cycle_time) 
                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                    
                    params = (
                        task_id,
                        attempts["attempt_number"],
                        attempts["pf_status"],
                        attempts["mistakes"],
                        cc_no,
                        Task_id_status,
                        Signature_by_Trainee, 
                        Signature_by_Process_Coach,
                        Signature_by_Training_Officer,
                        attempts["cycle_time"]
                    )
                    self.db_manager.execute_non_query(insert_query, params)
                    response.append({'action': "Inserted", "status": "success"})
                else:
                    # Update existing record
                    print("update big table")
                    update_query = """
                        UPDATE attempts 
                        SET  pf_status = %s, mistakes = %s, status_ = %s, Signature_by_Trainee = %s, Signature_by_Process_Coach = %s, Signature_by_Training_Officer = %s ,cycle_time = %s
                        WHERE cc_no = %s AND task_id = %s AND attempt_number = %s
                    """
                    update_params = (
                        attempts["pf_status"],
                        attempts["mistakes"],
                        Task_id_status,
                        Signature_by_Trainee,
                        Signature_by_Process_Coach,
                        Signature_by_Training_Officer,
                        attempts["cycle_time"],
                        cc_no,
                        task_id,
                        attempts["attempt_number"]
                    )
                    self.db_manager.execute_non_query(update_query, update_params)
                    response.append({'action': "Updated", "status": "success"})

        return response