from app.db_manager import DBManager
from app import logger
from  app.common import json_converter,json_converter2,json_converter3
import json
import qrcode,os
import io
import base64

class QR_gen:
    
    def __init__(self):
        self.db_manager = DBManager()
    
    def fetch_data_all_table(self,json_data):
            # json_data =  {"cc_no" : 13012}
            # print(json_data,"json")
            print(json_data[0].get("cc_no"),"123132123213231")

            cc_no= json_data[0].get("cc_no")
            print(cc_no,"cc_no              12   ")
            # query =  "SELECT * FROM registration left join  examine_details on registration.cc_no = examine_details.cc_no where registration.cc_no = %s"
            query1 = "SELECT * FROM   registration where cc_no = %s"
            query2 = "SELECT status_ FROM   examine_details where cc_no = %s AND topics = 'SOP - Standard Operating Procedure (System Followed by Operators)'"
            query3 = "SELECT status_ FROM   attempts where cc_no = %s "
            query4 = "SELECT status_ FROM   memory_details where cc_no = %s"
            # query5 = "SELECT * FROM   cycle where cc_no = %s"
            query5 = """ SELECT status_  FROM tasks_cycle  attempts_cycle where cc_no = %s """
                    
            print("this block is executed")
            detail_table1 = self.db_manager.execute_query(query1,(cc_no,))
            detail_table2 = self.db_manager.execute_query(query2,(cc_no,))
            
            detail_table3 = self.db_manager.execute_query(query3,(cc_no,))
            print("this block is executed till 3")
            detail_table4 = self.db_manager.execute_query(query4,(cc_no,))
            detail_table5 = self.db_manager.execute_query(query5,(cc_no,))
            # print("this block is executed till 5",detail_table5,cc_no)
            
            # print(detail_table1,"detail_table1")
            # print(detail_table2,"detail_table2")
            print(detail_table3,"detail_table3............................................................")
            # print(detail_table4,"detail_table4")
            # print(detail_table5,"detail_table5")
            # if detail_table2 is not None:
            #     detail_table2 =detail_table2
            # else:
            #     detail_table2 = [{'status_': 'No datas for Day 1 to 3'}]
            
            # if detail_table3 is not None:
            #     detail_table3 = detail_table3
            # else:
            #     detail_table3 = [{'status_': 'No datas for Day4'}]
            
            # if detail_table4 is not None:
            #         detail_table4 = detail_table4
            # else:
            #     detail_table4 = [{'status_': 'No datas for Day 5'}]
            
            # if detail_table5 is not None:
            #         detail_table5 = detail_table5
            # else:
            #     detail_table5 = [{'status_': 'No datas for Day 5.5'}]
            
            return detail_table1,detail_table2,detail_table3,detail_table4,detail_table5
    def generate_qr_code(self,data):
        reg,day123,day4,day41,day5 = self.fetch_data_all_table(data)
        # print(day123[0]["status_"],"789456231")
        # print(day4[0]["status_"],"789456231")
        # print(day41[0]["status_"],"789456231")
        # print(day5[0]["status_"],"789456231")
        # print(reg[0]["name_"],"789456231")
        
        
        cc_no = reg[0]["cc_no"]
        name = reg[0]["name_"]
        designation = reg[0]["designation"]
        date_of_joining = reg[0]["date_of_joining"]
        grade =reg[0]["grade"]
        qualification = reg[0]["qualification"]
        photo = reg[0]["photo"]
        # all([item['status_'] == 'Pass' for item in day4])
        
        
        
        level1 = day123[0]["status_"] if day123 and day123[0].get("status_") else False
        level11 = all([item['status_'] == 'Pass' for item in day4]) if day4 and day4[0].get("status_") else False
        level2 = day41[0]["status_"]  if day41 and day41[0].get("status_")else False
        level22 = day5[0]["status_"]  if day5 and day5[0].get("status_") else False
        
        print(level1, level11, level2, level22,"status of stage check")
        stage1 = (level1 == "Pass" and  level11 == True) and  level1 == "Pass"
        stage2 = stage1 and (level2 == level22) and level2 == "Pass"
        
        # if (level1 == level11) and (level2 == level22):
        #     print("you r level 2 employee")
        #     stage2 =  True
        #     stage1 =  True
        # elif (level1 == level11):
        #     print("you r level 1 employee")
        #     stage1 =  True
        #     stage2 =  False
        # else:
        #     print("he is not not fit to any type")
        #     stage1 =  False
        #     stage2 =  False
            
        # Convert data dictionary to JSON string
                # name_ cc_no designation date_of_joining grade qualification photo
        if stage1:
            all_datas = {
                    "Current_Level" : "Level-1",
                    
                    "cc_no": cc_no
                }  
        if stage2:
                all_datas = {
                    "Current_Level" : "Level-2",
                    "cc_no": cc_no
                }       
        
        print(stage1, stage2,"check stage")
        if stage1 or stage2:
                all_datas = all_datas
                all_datas2 = { 
                            "name" : name,
                            "cc_no" : cc_no,
                            "designation" : designation,
                            "date_of_joining" : date_of_joining,
                            "grade" : grade,
                            "photo" : photo,

                            }
                qr_data = json.dumps(all_datas)
                
                # Create QR code instance
                qr = qrcode.QRCode(
                    version=1,  # Controls the size of the QR Code
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
                
                qr.add_data(qr_data)
                qr.make(fit=True)
                
                # Generate and save QR code image
                # Generate QR code image
                qr_img = qr.make_image(fill='black', back_color='white')

                # Convert image to binary for saving to database
                img_byte_arr = io.BytesIO()
                qr_img.save(img_byte_arr, format='PNG')
                
                
                save_directory = "qr_code"
                if not os.path.exists(save_directory):
                    os.makedirs(save_directory)
                    
                qr_filename = f"{cc_no}_qr_code.png"
                
                
                path =os.path.join(save_directory, qr_filename)
                
                
                qr_img.save(path)
                
                qr_binary = img_byte_arr.getvalue()
                qr_base64 = base64.b64encode(qr_binary).decode('utf-8')
                response = { "status": "success", "message": "QR code successfully generated.","QR_code": qr_base64 if qr_base64 else [] ,"personal_info" : all_datas2 if all_datas2 else [] }
        else:
            qr_base64 = None
            all_datas2 = None
            response = { "status": "fail", "message": "Finish training to unlock your QR code.","QR_code": qr_base64 if qr_base64 else [] ,"personal_info" : all_datas2 if all_datas2 else [] }
        # Save to the database
        # self.save_qr_to_db(cc_no, qr_binary)
       
        # print(response)
        return response
    def save_qr_to_db(self, cc_no, qr_binary):


            # Insert or update query
            query = """
                INSERT INTO qr_codes (data,cc_no, qr_image)
                VALUES (%s, %s)
                ON DUPLICATE KEY UPDATE qr_image = VALUES(qr_image)
            """
            self.db_manager.execute_non_query(query, (cc_no, qr_binary))
            
            logger.info(f"updated the qr scanner for: {cc_no}")
            # print(f"Updated existing record for process_name: {process_name}, attempt_no: {attempts}")
            