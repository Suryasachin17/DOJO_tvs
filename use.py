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
            
query3 = """ALTER TABLE vision_db.attempts
MODIFY COLUMN pf_status VARCHAR(255) """          
# for i in [ query2]:      
# db_manager.execute_non_query(query3, params =None)        


#########################################################################


####################################### MEMORY TABLE #######################

query4 = """ CREATE TABLE vision_db.memory_details (
    memory_id INT AUTO_INCREMENT PRIMARY KEY,
    cc_no VARCHAR(255),
    process_name VARCHAR(255),
    process_obsevations VARCHAR(255),
    attempts VARCHAR(255),
    mistakes VARCHAR(255),
    heart_test VARCHAR(255),
    data_time TIMESTAMP ,
    status_ VARCHAR(255),
    sign_trainee LONGTEXT,
    sign_team_leader VARCHAR(255)
);

    """
query5 = """ALTER TABLE vision_db.memory_details
ADD COLUMN remarks VARCHAR(255);
 """   
 
query8 = """ALTER TABLE vision_db.memory_details
MODIFY COLUMN status_ VARCHAR(255) """ 




####################################### assembly TABLE #######################

# query21 = """ CREATE TABLE vision_db.assembly (
#     Task_id INT AUTO_INCREMENT PRIMARY KEY,
#     cc_no VARCHAR(255),
#     process_id VARCHAR(255),
#     process_completed VARCHAR(255),
#     assembling VARCHAR(255),
#     design_cycle_time VARCHAR(255),
#     attemmpt VARCHAR(255),
#     mistakes VARCHAR(255),
#     cycle_time VARCHAR(255),
#     target_score VARCHAR(255),
#     actual_score VARCHAR(255),
#     status_ VARCHAR(255),
#     sign_by_trainee LONGTEXT,
#     sign_by_line_captain VARCHAR(255),
#     remarks  VARCHAR(255),
#     date_ VARCHAR(255)
# );"""
query21 = """ CREATE TABLE vision_db.cycle (
    Task_id INT AUTO_INCREMENT PRIMARY KEY,
    cc_no VARCHAR(255),
    dct VARCHAR(255),
    actual_score VARCHAR(255),
    remarks VARCHAR(255),
    demo_line_captain VARCHAR(100),            -- Name of the demo line captain
    demo_trainee VARCHAR(100),                 -- Name of the demo trainee
    skill_matrix VARCHAR(100),                 -- Skill level or category
    cycle_achievementt VARCHAR(100),           -- Specific cycle achievement description
    sign_by_trainee TEXT,                      -- Signature by the trainee
    sign_by_line_captain TEXT,                 -- Signature by the line captain
    sign_by_module_controller TEXT,            -- Signature by the module controller
    attempt INT ,                      -- Attempt number
    cycle_time FLOAT,                          -- Time taken to complete the cycle (seconds)
    mistakes INT,                              -- Number of mistakes in the attempt
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    UNIQUE KEY unique_attempt (cc_no, attempt) -- Ensure unique cc_no and attempt combination
);"""


query100 = """ CREATE TABLE tasks_cycle (
    task_id INT  AUTO_INCREMENT PRIMARY KEY,
    cc_no VARCHAR(255),
    station_name VARCHAR(255),
    dct VARCHAR(255),
    status_ VARCHAR(255),
    remarks TEXT,
    date_ VARCHAR(255),
    attempt VARCHAR(255),
    actual_score VARCHAR(255),
    demo_line_captain VARCHAR(255),
    demo_trainee VARCHAR(255),
    cycle_achievement VARCHAR(255),
    skill_matrix VARCHAR(255),
    process_name VARCHAR(255),
    signature_by_trainee LONGTEXT,
    signature_by_line_caption VARCHAR(255),
    signature_by_module_controller VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY unique_attempt (cc_no, attempt)
);"""




query200 = """ CREATE TABLE attempts_cycle (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cc_no INT ,
    task_id INT,
    attempt_number VARCHAR(255),
    attempts_id VARCHAR(255),
    ji_demo_line_captain VARCHAR(255),
    mistakes JSON,
    cycle_time JSON,
    FOREIGN KEY (task_id) REFERENCES tasks_cycle(task_id) ON DELETE CASCADE
);
"""


query22 = """ ALTER TABLE vision_db.registration 
MODIFY COLUMN date_of_joining VARCHAR(100) ; """  

query23 = """ ALTER TABLE vision_db.examine_details 
ADD COLUMN date VARCHAR(100) ; """  

query26 = """ ALTER TABLE vision_db.attempts_cycle 
ADD COLUMN cc_no VARCHAR(100) ; """  

query25 = """ ALTER TABLE vision_db.attempts 
MODIFY COLUMN Signature_by_Trainee LONGTEXT """ 

query28 = """ ALTER TABLE vision_db.attempts_cycle 
ADD UNIQUE KEY unique_attempt (cc_no,attempt_number) """ 


query29 = """ ALTER TABLE vision_db.memory_details 
ADD COLUMN place VARCHAR(100) ; """  


query30 = """ ALTER TABLE vision_db.attempts 
ADD COLUMN place VARCHAR(100) ; """  

query31 = """ALTER TABLE vision_db.tasks_cycle
ADD COLUMN place VARCHAR(100) ;"""

query32 = """ ALTER TABLE vision_db.registration 
MODIFY COLUMN date_of_joining VARCHAR(100) ; """  

query33 = """ ALTER TABLE vision_db.Examine_details 
ADD COLUMN over_all_result VARCHAR(100) ;"""

db_manager.execute_non_query(query33, params =None)

# db_manager.execute_non_query(query24, params =None)   





# query = INSERT INTO tasks (task_name) VALUES
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

# {'assemble_test': [{'date': '2025-01-01', 'assembling': 'TypeA', 'design_cycle_time': '60s', 'status_': 'Completed', 'target_score': '95', 'actual_score': '90', 'sign': {'sign_by_trainee': 'John Doe', 'sign_by_line_captain': 'Surya Smith'}}], 'attempt': [{'attempt_number': '1', 'design_cycle_time': '55s', 'process_id': 'p0001', 'process_completed': '1', 'mistakes': '0', 'remarks': None}, {'attempt_number': '2', 'design_cycle_time': '60s', 'process_id': 'p0002', 'process_completed': '0', 'mistakes': '1', 'remarks': None}], 'cc_no': '12345'}