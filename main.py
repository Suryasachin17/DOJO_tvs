from app.bio_service import BioService
from app.bio_fetch_service import bio_fetch_service
from app.qr_genrator import QR_gen
from app.Big_table_test import big_table_test
from app.assembly import CycleAchievements
from app.memory_test import memory
from app import logger
from flask import Flask, request,Response
from flask_cors import CORS
from app.utils.common import json_converter
from app.utils.common import draw_signature_window
import cv2
import base64




app = Flask(__name__)

CORS(app)



logger.info("Starting")
@app.route('/Examine_details',methods = ['GET', 'POST'])
def Examine_details():
    
    data = request.get_json()
    print(data,"****************************************************************************************")
  
    
    # Save bio data to DB

    bio_service.save_data("Examine_details",data)
    logger.info("%s:data saved to the database.",bio_service)
    return Response( "Completed")



@app.route('/Add_new_employee',methods = ['GET', 'POST'])
def Add_new_employee():
    
    data = request.get_json()
    # print(data,"****************************************************************************************")
  
    
    # Save bio data to DB

    res = bio_service.save_data("Registration",data)
    logger.info("%s:data saved to the database.",res)
    return res



@app.route('/fetch_all_employee_detail',methods = ['GET', 'POST'])
def fetch_all_employee_detail():
    

  
    
    # Save bio data to DB

    res = bio_fetch_service.fetch_registration_details()
    # logger.info("%s:data saved to the database.",res)
    return res


@app.route('/update_employee_details',methods = ['GET', 'POST'])
def update_employee_details():
    
    data = request.get_json()
    # print(data,"****************************************************************************************")
  
    
    # Save bio data to DB

    res = bio_service.save_data("Examine_details",data)
    # logger.info("%s:data saved to the database.",res)
    return res

@app.route('/get_all_employee_details',methods = ['GET', 'POST'])
def get_all_employee_details():
    
    data = request.get_json()
    # print(data,"****************************************************************************************")
  
    
    # Save bio data to DB

    res = bio_fetch_service.fetch_data("Examine_details",data)
    # logger.info("%s:data saved to the database.",res)
    return res


@app.route('/overall_employee_details',methods = ['GET', 'POST'])
def overall_employee_details():

    data = request.get_json()
    print(data,"****************************************************************************************")
  
    # data = bio_fetch_service.fetch_data_both_table(data)
    # print(data,"apiiiiiiiiiiiiiiiiiiiii")
    # logger.info("%s:data saved to the database.",res)
    return  bio_fetch_service.fetch_data_both_table(data)

# fetch_data_both_table
    # print("Bio data saved to the database.")
    
    # Fetch bio data from DB
    # fetched_bio = bio_service.fetch_bio()
    # logger.info("Fetched bio data:", fetched_bio)
    # print("Fetched bio data:", fetched_bio)
    
    
######################################Big table#####################################


@app.route('/Cycle_games_up_in',methods = ['GET', 'POST'])
def Cycle_games_up_in():
    
    data = request.get_json()
    # print(data,"****************************************************************************************")

    return  big_table_test.save_data(data)


###################################### memopry table#####################################


@app.route('/memory_table_up_in',methods = ['GET', 'POST'])
def memory_table_up_in():
    
    data = request.get_json()
    print(data,"***************************************************mem*************************************")
    return memory.save_data(data)
      


###################################### cycle_table #####################################


@app.route('/cycle_time_achievement',methods = ['GET', 'POST'])
def cycle_time_achievement():
    
    data = request.get_json()
    print(data,"***************************************************cycle*************************************")
    return CycleAchievements.save_data(data)
      




@app.route('/QR_generator',methods = ['GET', 'POST'])
def QR_generator():
    
    data = request.get_json()
    print(data,"***************************************************cycle*************************************")
    return QR_gen.generate_qr_code(data)







############################################## draw signature################################
from app.utils.common import draw_signature_window
import cv2
@app.route('/mouse_sign',methods = ['GET', 'POST'])
def mouse_sign():
    
    try:
        image  = draw_signature_window()
        cv2.imshow("signed_image",image)
        cv2.waitKey(1)
        print("hggjvbhbmnv")
        _,buffer = cv2.imencode('.png',image)
        sign = base64.b64encode(buffer).decode('utf-8')
        return  sign
    
    except Exception as e:
        return str(e)




if __name__ == "__main__":
    
    
    bio_service = BioService()
    big_table_test = big_table_test()
    bio_fetch_service = bio_fetch_service()
    memory = memory()
    CycleAchievements = CycleAchievements()
    QR_gen = QR_gen()
    logger.info("%s:Server initalised successfully")
    app.run(host="0.0.0.0", port=5000,  use_reloader=False)
