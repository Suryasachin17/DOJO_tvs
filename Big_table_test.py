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
            print(entry)
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
                        attempts["status_"])
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

big_table_test = big_table_test()
big_table_test.save_data({
    'Cycle_games': [
        {
            'task_id': '1',
            'attempts': [
                { 'attempt_number': 1, 'pf_status': 'Pass', 'mistakes': '2', 'cycle_time': '2' },
                { 'attempt_number': 2, 'pf_status': 'Fail', 'mistakes': '2', 'cycle_time': '2' },
                { 'attempt_number': 3, 'pf_status': 'Pass', 'mistakes': '2', 'cycle_time': '2' },
                { 'attempt_number': 4, 'pf_status': 'Fail', 'mistakes': '1', 'cycle_time': '2' },
                { 'attempt_number': 5, 'pf_status': 'Pass', 'mistakes': '2', 'cycle_time': '2' }
            ],
            'status_': None,
            'sign': { 'Signature_by_Trainee': 'Donald', 'Signature_by_Process_Coach': 'Gokul', 'Signature_by_Training_Officer': 'Surya' }
        },
        {
            'task_id': '2',
            'attempts': [
                { 'attempt_number': 1, 'pf_status': None, 'mistakes': None, 'cycle_time': None },
                { 'attempt_number': 2, 'pf_status': None, 'mistakes': None, 'cycle_time': None },
                { 'attempt_number': 3, 'pf_status': None, 'mistakes': None, 'cycle_time': None },
                { 'attempt_number': 4, 'pf_status': None, 'mistakes': None, 'cycle_time': None },
                { 'attempt_number': 5, 'pf_status': None, 'mistakes': None, 'cycle_time': None }],
            'status_': None,
            'sign': { 'Signature_by_Trainee': None, 'Signature_by_Process_Coach': None, 'Signature_by_Training_Officer': None }
        },
        { 'task_id': '3', 'attempts': [{ 'attempt_number': 1, 'pf_status': None, 'mistakes': None, 'cycle_time': None }, { 'attempt_number': 2, 'pf_status': None, 'mistakes': None, 'cycle_time': None }, { 'attempt_number': 3, 'pf_status': None, 'mistakes': None, 'cycle_time': None }, { 'attempt_number': 4, 'pf_status': None, 'mistakes': None, 'cycle_time': None }, { 'attempt_number': 5, 'pf_status': None, 'mistakes': None, 'cycle_time': None }], 'status_': None, 'sign': { 'Signature_by_Trainee': None, 'Signature_by_Process_Coach': None, 'Signature_by_Training_Officer': None } }, { 'task_id': '4', 'attempts': [{ 'attempt_number': 1, 'pf_status': None, 'mistakes': None, 'cycle_time': None }, { 'attempt_number': 2, 'pf_status': None, 'mistakes': None, 'cycle_time': None }, { 'attempt_number': 3, 'pf_status': None, 'mistakes': None, 'cycle_time': None }, { 'attempt_number': 4, 'pf_status': None, 'mistakes': None, 'cycle_time': None }, { 'attempt_number': 5, 'pf_status': None, 'mistakes': None, 'cycle_time': None }], 'status_': None, 'sign': { 'Signature_by_Trainee': None, 'Signature_by_Process_Coach': None, 'Signature_by_Training_Officer': None } }, { 'task_id': '5', 'attempts': [{ 'attempt_number': 1, 'pf_status': None, 'mistakes': None, 'cycle_time': None }, { 'attempt_number': 2, 'pf_status': None, 'mistakes': None, 'cycle_time': None }, { 'attempt_number': 3, 'pf_status': None, 'mistakes': None, 'cycle_time': None }, { 'attempt_number': 4, 'pf_status': None, 'mistakes': None, 'cycle_time': None }, { 'attempt_number': 5, 'pf_status': None, 'mistakes': None, 'cycle_time': None }], 'status_': None, 'sign': { 'Signature_by_Trainee': None, 'Signature_by_Process_Coach': None, 'Signature_by_Training_Officer': None } }, {
            'task_id': '6', 'attempts': [{ 'attempt_number': 1, 'pf_status': None, 'mistakes': None, 'cycle_time': None }, {
                'attempt_number':
                    2, 'pf_status': None, 'mistakes': None, 'cycle_time': None
            }, { 'attempt_number': 3, 'pf_status': None, 'mistakes': None, 'cycle_time': None }, { 'attempt_number': 4, 'pf_status': None, 'mistakes': None, 'cycle_time': None }, { 'attempt_number': 5, 'pf_status': None, 'mistakes': None, 'cycle_time': None }], 'status_': None, 'sign': { 'Signature_by_Trainee': None, 'Signature_by_Process_Coach': None, 'Signature_by_Training_Officer': None }
        }, { 'task_id': '7', 'attempts': [{ 'attempt_number': 1, 'pf_status': None, 'mistakes': None, 'cycle_time': None }, { 'attempt_number': 2, 'pf_status': None, 'mistakes': None, 'cycle_time': None }, { 'attempt_number': 3, 'pf_status': None, 'mistakes': None, 'cycle_time': None }, { 'attempt_number': 4, 'pf_status': None, 'mistakes': None, 'cycle_time': None }, { 'attempt_number': 5, 'pf_status': None, 'mistakes': None, 'cycle_time': None }], 'status_': None, 'sign': { 'Signature_by_Trainee': None, 'Signature_by_Process_Coach': None, 'Signature_by_Training_Officer': None } }, { 'task_id': '8', 'attempts': [{ 'attempt_number': 1, 'pf_status': None, 'mistakes': None, 'cycle_time': None }, { 'attempt_number': 2, 'pf_status': None, 'mistakes': None, 'cycle_time': None }, { 'attempt_number': 3, 'pf_status': None, 'mistakes': None, 'cycle_time': None }, { 'attempt_number': 4, 'pf_status': None, 'mistakes': None, 'cycle_time': None }, { 'attempt_number': 5, 'pf_status': None, 'mistakes': None, 'cycle_time': None }], 'status_': None, 'sign': { 'Signature_by_Trainee': None, 'Signature_by_Process_Coach': None, 'Signature_by_Training_Officer': None } }, { 'task_id': '9', 'attempts': [{ 'attempt_number': 1, 'pf_status': None, 'mistakes': None, 'cycle_time': None }, { 'attempt_number': 2, 'pf_status': None, 'mistakes': None, 'cycle_time': None }, { 'attempt_number': 3, 'pf_status': None, 'mistakes': None, 'cycle_time': None }, { 'attempt_number': 4, 'pf_status': None, 'mistakes': None, 'cycle_time': None }, { 'attempt_number': 5, 'pf_status': None, 'mistakes': None, 'cycle_time': None }], 'status_': None, 'sign': { 'Signature_by_Trainee': None, 'Signature_by_Process_Coach': None, 'Signature_by_Training_Officer': None } }, { 'task_id': '10', 'attempts': [{ 'attempt_number': 1, 'pf_status': None, 'mistakes': None, 'cycle_time': None }, { 'attempt_number': 2, 'pf_status': None, 'mistakes': None, 'cycle_time': None }, { 'attempt_number': 3, 'pf_status': None, 'mistakes': None, 'cycle_time': None }, { 'attempt_number': 4, 'pf_status': None, 'mistakes': None, 'cycle_time': None }, { 'attempt_number': 5, 'pf_status': None, 'mistakes': None, 'cycle_time': None }], 'status_': None, 'sign': { 'Signature_by_Trainee': None, 'Signature_by_Process_Coach': None, 'Signature_by_Training_Officer': None } }], 'cc_no': 13012
} )



{   
 
    "Cycle_games": [
        
        {
            "task_id": "1", #1 to 10
            "attempts": [
            { "attempt_number": 1, "pf_status": "pass", "mistakes": None,"Cycle_time" : None},
            { "attempt_number": 2, "pf_status": None, "mistakes": None,"Cycle_time" : None },
            { "attempt_number": 3, "pf_status": None, "mistakes": None,"Cycle_time" : None },
            { "attempt_number": 4, "pf_status": None, "mistakes": None,"Cycle_time" : None },
            { "attempt_number": 5, "pf_status": None, "mistakes": None,"Cycle_time" : None }
            ],
            "status_": None
        },
        {
        "task_id": "2",
        "attempts": [
        { "attempt_number": 1, "pf_status": "Fail", "mistakes": None, "Cycle_time": "Good_work" },
        { "attempt_number": 2, "pf_status": None, "mistakes": None, "Cycle_time": None },
        { "attempt_number": 3, "pf_status": None, "mistakes": None, "Cycle_time": None },
        { "attempt_number": 4, "pf_status": "Fail", "mistakes": 8, "Cycle_time": None },
        { "attempt_number": 5, "pf_status": None, "mistakes": None, "Cycle_time": "Good_work" }
        ],
        "status_": "Good_work"
         },
        {
        "Signature_by_Trainee": None,
        "Signature_by_Process_Coach": None,
        "Signature_by_Training_Officer": None,
  
        }
    ],
  
    "cc_no": 13012,
  
}





