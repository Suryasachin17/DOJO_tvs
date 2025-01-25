from collections import defaultdict
import time,json


def json_converter(db_output):

    transformed_data = defaultdict(lambda: {"attempts": [], "status_": "", "sign": {}})

    # print(transformed_data["1"])
    # print(db_output,"/////////////json_converter////////////")
    # print(db_output.keys(),"/////////json_converter/////////////")
    for item in db_output:
        # print(item)
        task_id = str(item["task_id"])
        transformed_data[task_id]["attempts"].append({
            "attempt_number": item["attempt_number"],
            "pf_status" : item["pf_status"] if item["pf_status"] else None ,
            "mistakes" : item["mistakes"] if item["mistakes"] else None ,
            "cycle_time": item["cycle_time"] if item["cycle_time"] else None,
        })
        transformed_data[task_id]["status_"] =  item["status_"] 
        transformed_data[task_id]["place"] =  item["place"] 
        transformed_data[task_id]["date"] =  item["date"] 
        transformed_data[task_id]["sign"] =  {
            "Signature_by_Trainee": item.get("Signature_by_Trainee") or None,
            "Signature_by_Process_Coach": item.get("Signature_by_Process_Coach") or None,
            "Signature_by_Training_Officer": item.get("Signature_by_Training_Officer") or None,
        }

    # print(transformed_data)


    final_output = []
    for task_id,detail in transformed_data.items():
        # print(detail,"3543341354531")
        final_output.append({
            "task_id": task_id,
            **detail
        })
    
    return final_output





def json_converter2(db_output):
    transformed_data = {"cc_no": None, "memory_test": {"attempts": [],"sign": {}}}
    # print(db_output,"db_outputdb_outputdb_outputdb_outputdb_outputdb_outputdb_output ")
    for item in db_output:
        # Set the common fields for memory_test
        # print(item,"))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))")
        transformed_data["cc_no"] = str(item["cc_no"])
        transformed_data["memory_test"]["date"] = item["data_time"]
        transformed_data["memory_test"]["process_name"] = item["process_name"]
        transformed_data["memory_test"]["process_observation"] = item["process_obsevations"]
        transformed_data["memory_test"]["place"] = item["place"] or None

        transformed_data["memory_test"]["status_"] = item["status_"]
        # transformed_data["memory_test"]["sign_by_trainee"] = item["sign_trainee"]
        # transformed_data["memory_test"]["sign_by_line_captain"] = item["sign_team_leader"]
        transformed_data["memory_test"]["remarks"] = item["remarks"]
        transformed_data["memory_test"]["sign"] =  {
            "sign_by_trainee": item["sign_trainee"] or None,
            "sign_by_line_captain": item["sign_team_leader"] or None}
        # Append attempts details
        transformed_data["memory_test"]["attempts"].append({
            "attempt_number": item["attempts"],
            "mistakes": item["mistakes"] if item["mistakes"] else None,
            "heart_test": item["heart_test"] if item["heart_test"] else None,
        })

    # Print the final transformed data
    print(transformed_data,"789898989898989898989898989898989898989898989898989898989898989--------------------------")

    
    final = []

    # Assuming 'memory_test' holds the main data we need
    memory_test_data = transformed_data['memory_test']

    # Create a dictionary for the final output
    final.append({
        "task_id": 1,  # Example task_id based on current timestamp
        "attempts": memory_test_data['attempts'],
        "status_": memory_test_data['status_'],
        "sign": memory_test_data['sign'],
        "remarks": memory_test_data['remarks'],
        "process_name": memory_test_data['process_name'],
        "process_observation": memory_test_data['process_observation'],
        "date": memory_test_data['date'],
        "place": memory_test_data['place']
    })
    
    
    return final



# def json_converter3(db_output):
#     output = {"assemble_test":{},"attempt" :[]}
#     for assemblyy in db_output:
#         output["cc_no"] = assemblyy["cc_no"]
#         output["assemble_test"] = [{"date" :assemblyy["date_"], 
#                                     "assembling" :assemblyy["assembling"],
#                                     "design_cycle_time" :assemblyy["design_cycle_time"],
#                                     "status_" :assemblyy["status_"],"target_score" :assemblyy["target_score"],
#                                     "actual_score" :assemblyy["actual_score"],
#                                     "sign" : {"sign_by_trainee" :assemblyy["sign_by_trainee"], 
#                                                 "sign_by_line_captain" :assemblyy["sign_by_line_captain"]}}]
#         output["attempt"].append({"attempt_number": assemblyy["attemmpt"],
#             "design_cycle_time":  assemblyy["design_cycle_time"],
#             "process_id":  assemblyy["process_id"],
#             "process_completed": assemblyy["process_completed"],
#             "mistakes":  assemblyy["mistakes"],
#             "remarks":  assemblyy["remarks"]})

#     # print(output,"to chck")

#     goal =[{"task_id": 1,
#         "assemble_test": output["assemble_test"],
#         "attempts": output["attempt"],
#         "cc_no": output["cc_no"]}]

#     return goal


#  [{'cc_no': '13012', 'station_name': 'cycle_table', 'dct': '22-05-2002', 'status_': None, 'remarks': 'dedication', 'date_': '10-01-2015', 'actual_score': '100', 'demo_line_captain': 'dude', 'demo_trainee': 'macha', 
#    'cycle_achievement': 'rod', 'skill_matrix': 'yesboss', 'process_name': 'gym', 'signature_by_trainee': 'surya', 'signature_by_line_caption': 'arnold', 
#    'signature_by_module_controller': 'brucelee', 'attempt_number': '1', 'attempts_id': 'null', 'ji_demo_line_captain': None, 'mistakes': '["1", "2", "3", "4", "5"]', 'cycle_time': '["6", "7", "8", "9", "10"]'}, 
 
#   {'cc_no': '13012', 'station_name': 'cycle_table', 'dct': '22-05-2002', 'status_': None, 'remarks': 'dedication', 'date_': '10-01-2015', 'actual_score': '100', 'demo_line_captain': 'dude', 'demo_trainee': 'macha',
#    'cycle_achievement': 'rod', 'skill_matrix': 'yesboss', 'process_name': 'gym', 'signature_by_trainee': 'surya', 'signature_by_line_caption': 'arnold', 
#    'signature_by_module_controller': 'brucelee', 'attempt_number': '2', 'attempts_id': 'null', 'ji_demo_line_captain': None, 'mistakes': '["87", "82", "83", "84", "85"]', 'cycle_time': '["21", "22", "23", "24", "80"]'}] 13012


def json_converter3(db_output):
    output = {
        "cc_no": None,
        "task_id" : 1,
        "place": None,
        "dct": None,
        "date": None,
        "actual_score": None,
        "status_": None,
        "process_name": None,
        "remarks": None,
        "demo_line_captain": None,
        "demo_trainee": None,
        "skill_matrix": None,
        "cycle_achievement": None,
        "sign": {},
        "attempts": []
    }
    # station_name
    for assemblyy in db_output:
        # Populate top-level fields (assumes values are consistent across rows)
        print(assemblyy,"common cycle check")
        output["cc_no"] = str(assemblyy.get("cc_no"))
        output["dct"] = assemblyy.get("dct")
        output["date"] = assemblyy.get("date_")
        output["actual_score"] = assemblyy.get("actual_score")
        output["status_"] = assemblyy.get("status_")
        output["place"] = assemblyy.get("place")
        output["process_name"] = assemblyy.get("process_name")
        output["remarks"] = assemblyy.get("remarks")
        output["demo_line_captain"] = assemblyy.get("demo_line_captain")
        output["demo_trainee"] = assemblyy.get("demo_trainee")
        output["skill_matrix"] = assemblyy.get("skill_matrix")
        output["cycle_achievement"] = assemblyy.get("cycle_achievement")
        output["sign"] = {
            "sign_by_trainee": assemblyy.get("signature_by_trainee"),
            "sign_by_line_captain": assemblyy.get("signature_by_line_caption"),
            "sign_by_module_controller": assemblyy.get("signature_by_module_controller")
        }
        cycle_time = assemblyy.get("cycle_time")
        mistakes = assemblyy.get("mistakes")
        cycle_time = json.loads(cycle_time)
        mistakes = json.loads(mistakes)
        print(cycle_time,mistakes,"common file")
        # Append attempt details
        output["attempts"].append({
           
            "attempt_number": assemblyy.get("attempt_number"),
            "ji_demo_line_captain" : assemblyy.get("ji_demo_line_captain"),
            "cycle_time": cycle_time,
            "mistakes": mistakes
        })
    print(output,"check common")
    return [output]
