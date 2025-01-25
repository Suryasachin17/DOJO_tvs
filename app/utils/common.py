from collections import defaultdict
import cv2
import numpy as np




def json_converter(db_output):

    transformed_data = defaultdict(lambda: {"attempts": [], "status_": "", "sign": {}})

    # print(transformed_data["1"])
    print(db_output.keys(),"////////////////////////////////")
    for item in db_output.get("Cycle_games"):
        # print(item)
        task_id = str(item["task_id"])
        transformed_data[task_id]["attempts"].append({
            "attempt_number": item["attempt_number"],
            "pf_status" : item["pf_status"] if item["pf_status"] else None ,
            "mistakes" : item["mistakes"] if item["mistakes"] else None ,
            "cycle_time": item["cycle_time"] if item["cycle_time"] else None,
        })
        transformed_data[task_id]["status_"] =  item["status_"] 
        transformed_data[task_id]["sign"] =  {
            "Signature_by_Trainee": item.get("Signature_by_Trainee") or None,
            "Signature_by_Process_Coach": item.get("Signature_by_Process_Coach") or None,
            "Signature_by_Training_Officer": item.get("Signature_by_Training_Officer") or None,
        }

    # print(transformed_data)


    final_output = {"cycle_games": []}
    for task_id,detail in transformed_data.items():
        print(detail,"3543341354531")
        final_output["cycle_games"].append({
            "task_id": task_id,
            **detail
        })
    
    return final_output



canvas = np.ones((400, 800,3) ,dtype  = np.uint8) * 255
prev_x,prev_y = -1, -1
drawing = False


def mouse_event(event,x,y,flags,param):
    global drawing,prev_x,prev_y,canvas
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        prev_x, prev_y = x, y
    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        if prev_x != -1 and prev_y != -1:
            cv2.line(canvas, (prev_x, prev_y), (x, y), (0, 0, 0), thickness=2)
        prev_x, prev_y = x, y
    
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        prev_x, prev_y = -1, -1
        
        

def draw_signature_window():
    global canvas
    cv2.namedWindow("signature_window")
    cv2.setMouseCallback("signature_window",mouse_event)
    while True:
        cv2.imshow("signature_window", canvas)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            print("pressed q")
            break
        elif key == ord('c'):
            print("pressed c")
            canvas[:] = 255
            break
        elif key == ord('s'):
            print("pressed s")
            cv2.imwrite("signature.png", canvas)
            break
    return canvas
    
