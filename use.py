from app.db_manager import DBManager
# app.db_manager

db_manager = DBManager()

# query = """ CREATE TABLE bio_data ( 
    
#     si_no INT  PRIMARY KEY AUTO_INCREMENT,
#     cc_no INT UNIQUE, 
#     category VARCHAR(255) NOT NULL,
#     total_mark INT NOT NULL,
#     target_  INT NOT NULL,
#     status_ BOOLEAN NOT NULL,
#     photo VARCHAR(255) NOT NULL
# )"""


# query = """ CREATE TABLE Examine_details ( 
#     si_no INT PRIMARY KEY AUTO_INCREMENT,
#     topics VARCHAR(255) NOT NULL,
#     cc_no INT,
#     actual_score INT NOT NULL,
#     status_ VARCHAR(255) NOT NULL,
#     sign_by_trainee VARCHAR(255),
#     sign_by_training_officer VARCHAR(255),
#     Remarks VARCHAR(255),
#     FOREIGN KEY (cc_no) REFERENCES bio_data(cc_no)
#  )"""



# query =""" ALTER TABLE Examine_details MODIFY COLUMN status_ INT NULL """


# query = """CREATE TABLE Registration (
#     si_no INT PRIMARY KEY AUTO_INCREMENT,
#     name_ VARCHAR(255) NOT NULL,
#     cc_no INT UNIQUE NOT NULL,
#     designation VARCHAR(255) NOT NULL,
#     date_of_joining DATE NOT NULL,
#     grade VARCHAR(10) NOT NULL,
#     year_passed_out INT NOT NULL,
#     college_name VARCHAR(255) NOT NULL,
#     branch VARCHAR(50) NOT NULL,
#     qualification VARCHAR(50) NOT NULL,
#     photo TEXT NOT NULL
# )
# """



# query = """ SHOW CREATE TABLE Examine_details

# """

# query = """ALTER TABLE registration
# MODIFY COLUMN status_ VARCHAR(255)"""

# db_manager.execute_non_query(query, params =None)

# traing_data = { "train" :[{
#         "Topic": "About Lucas TVS (Customers/Products/Policies)",
#         "ccno": 13012,
#         "Actual_Score": None, 
#         "Status": None, 
#         "sign_by_trainee": None, 
#         "sign_by_training_officer": None, 
#         "Remarks": None 
        
#         },
#                           {
#         "Topic": "About Lucas TVS (Customers/Products/Policies)", 
#         "ccno": 13012,
#         "Actual_Score": None, 
#         "Status": None, 
#         "sign_by_trainee": None, 
#         "sign_by_training_officer": None, 
#         "Remarks": None 
        
#         }
#     ]
# }

# for category, entries in traing_data.items():
#             print( category, entries)
#             # for entry in entries:
            #     params = (entry["cc_no"] ,category,entry['Total_mark'], entry['Target'], entry['Status'])
            #     self.db_manager.execute_non_query(query, params)
            
            
############to create table for attempt     ####################      

            
query1 = """ CREATE TABLE  tasks (
    task_id INT AUTO_INCREMENT PRIMARY KEY,
    task_name VARCHAR(255) NOT NULL
)"""


query2 = """ CREATE TABLE   attempts (
    attempts_id INT AUTO_INCREMENT PRIMARY KEY,
    task_id INT ,
    attempt_number INT CHECK (attempt_number BETWEEN 1 AND 5),
    pf_status ENUM('Pass','Fail'),
    mistakes INT DEFAULT 0,
    cc_no INT,
    FOREIGN KEY (task_id) REFERENCES tasks(task_id)  ) """   
            
            
# for i in [ query2]:      
#     db_manager.execute_non_query(i, params =None)        

# query = """ INSERT INTO tasks (task_name) VALUES
# ('Spot the Safety Hazard'),
# ('Quality Check Exercise'),
# ('Poison Cake Test'),
# ('Memory Game'),
# ('Process Sequence'),
# ('5S Exercise'),
# ('Finger Dexterity'),
# ('Eye and Hand Coordination'),
# ('Hand Steadiness'),
# ('Assemble & Disassemble') """
        

# db_manager.execute_non_query(query, params =None)                   

 
 
 
 
 
 
 
 
 
# Example bio data from API
# bio_data = {
#     "A": [{"name": "Surya","cc_no": 13012,"Designation": "Boss", "data_of_joining": "2023-05-12", "grade": "A+", "year_passed_out": 2019, "college_name": "vels", "Branch": "EEE", "qualification": "BE", "photo": "base file"}],
#     "B": [{"name": "gok","cc_no": 12997,"Designation": "Boss", "data_of_joining":  "2023-05-12", "grade": "A+", "year_passed_out": 2019, "college_name": "vels", "Branch": "EEE", "qualification": "BE", "photo": "base file"}],
#     "C": [{"name": "don","cc_no": 12345,"Designation": "Boss", "data_of_joining":  "2023-05-12", "grade": "A+", "year_passed_out": 2019, "college_name": "vels", "Branch": "EEE", "qualification": "BE", "photo": "base file"}]
# }
    
# # data = {
#      "train" :[{
#         "Topic": "About Lucas TVS (Customers/Products/Policies)", 
#         "ccno": 13012,
#         "Actual_Score": None, 
#         "Status": None, 
#         "sign_by_trainee": None, 
#         "sign_by_training_officer": None, 
#         "Remarks": None
#         },
#     {
#         "Topic": "Work Discipline (including Uniform, Working Safety Shoes, Attendance/Discipline, Shift Times, Punctuality)", 
#         "ccno": 13012,
#         "Actual_Score": None, 
#         "Status": None, 
#         "sign_by_trainee": None, 
#         "sign_by_training_officer": None, 
#         "Remarks": None
#     },
#     {
#         "Topic": "Industrial Safety Training", 
#         "ccno": 13012,
#         "Actual_Score": None, 
#         "Status": None, 
#         "sign_by_trainee": None, 
#         "sign_by_training_officer": None, 
#         "Remarks": None
#     },
#     {
#         "Topic": "Awareness of Quality", 
#         "ccno": 13012,
#         "Actual_Score": None, 
#         "Status": None, 
#         "sign_by_trainee": None, 
#         "sign_by_training_officer": None, 
#         "Remarks": None
#     },
#     {
#         "Topic": "SOP - Standard Operating Procedure (System Followed by Operations)", 
#         "ccno": 13012,
#         "Actual_Score": None, 
#         "Status": None, 
#         "sign_by_trainee": None, 
#         "sign_by_training_officer": None, 
#         "Remarks": None
#     },
#     {
#         "Topic": "5 S & 3M Practices", 
#         "ccno": 13012,
#         "Actual_Score": None, 
#         "Status": None, 
#         "sign_by_trainee": None, 
#         "sign_by_training_officer": None, 
#         "Remarks": None
#     },
#     {
#         "Topic": "OHSAS & EMS", 
#         "ccno": 13012,
#         "Actual_Score": None, 
#         "Status": None, 
#         "sign_by_trainee": None, 
#         "sign_by_training_officer": None, 
#         "Remarks": None
#     },
#     {
#         "Topic": "Product Knowledge (Basic Level)", 
#         "ccno": 13012,
#         "Actual_Score": None, 
#         "Status": None, 
#         "sign_by_trainee": None, 
#         "sign_by_training_officer": None, 
#         "Remarks": None
#     },
#     {
#         "Topic": "Fire Safety & Electrical Safety", 
#         "Actual_Score": None, 
#         "Status": None, 
#         "sign_by_trainee": None, 
#         "sign_by_training_officer": None, 
#         "Remarks": None, 
#         "ccno": 13012
#     },
# ]
#     }

