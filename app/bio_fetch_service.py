from app.db_manager import DBManager
from app import logger

class bio_fetch_service:
    
    def __init__(self):
        self.db_manager = DBManager()
    
    def fetch_data(self,table_name,json_data):
        # json_data =  {"cc_no" : 13012}
        # print(json_data,"json")
        cc_no= json_data[0].get("cc_no")
        print(cc_no,"cc_no                 ")
        query = "SELECT * FROM  {} WHERE cc_no = %s".format(table_name)
        
        detail_table = self.db_manager.execute_query(query,(cc_no,))
        
        return detail_table
    
    def fetch_data(self,table_name,json_data):
        # json_data =  {"cc_no" : 13012}
        # print(json_data,"json")
        
        try:
            cc_no= json_data[0].get("cc_no")
            print(cc_no,"cc_no                 ")
            query = "SELECT * FROM  {} WHERE cc_no = %s".format(table_name)
            
            detail_table = self.db_manager.execute_query(query,(cc_no,))
            if detail_table:
                    result = ({
                                "cc_no": cc_no,
                                "status": "Sucessfully fetched",
                                "message": "Registration details fetched.",
                                "data" :    detail_table
                            })
                                    
            else:
                
                    result = ({
                                "cc_no": cc_no,
                                "status": "Failed fetched",
                                "message": "There is no such cc_no,enter the new details."
                            })
            return result
    
        except Exception as e:
            logger.info(f"Error in fetching registerdata {e}")
            return {
            "status": "Error",
            "message": "An error occurred while fetching details.",
            "error": str(e)
        }
            
    def fetch_data_both_table_duplicate(self,json_data):
        # json_data =  {"cc_no" : 13012}
        # print(json_data,"json")
        
        try:
            cc_no= json_data[0].get("cc_no")
            print(cc_no,"cc_no                 ")
            # query =  "SELECT * FROM registration left join  examine_details on registration.cc_no = examine_details.cc_no where registration.cc_no = %s"
            query1 = "SELECT * FROM   registration where cc_no = %s"
            query2 = "SELECT * FROM   examine_details where cc_no = %s"
            detail_table2 = self.db_manager.execute_query(query2,(cc_no,))
            detail_table1 = self.db_manager.execute_query(query1,(cc_no,))
            
            # print(detail_table1,detail_table2,"[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
            if detail_table1 and not detail_table2:
                print("true false")
                result = ({
                                "cc_no": cc_no,
                                "status": "Sucessfully fetched one table table",
                                "message": "Registration details fetched and examine the person below table.",
                                "bio" :    detail_table1,
                                "Safety_training"  : detail_table2
                            })
                # print(detail_table2,"detail_table")
            elif detail_table1 and detail_table2:
                    print("true true")
                    result = ({
                                "cc_no": cc_no,
                                "status": "Sucessfully fetched two table",
                                "message": "Registration and examine details fetched.",
                                "bio" :    detail_table1,
                                "Safety_training"  : detail_table2
                            })
            
                                    
            else:
                    print("This block is being executed.")
                    logger.info("Error in fetching register data and examine  for {}".format(cc_no))
                    result = ({
                                "cc_no": cc_no,
                                "status": "Failed fetched  two table",
                                "message": "There is no such cc_no,enter the new details."
                            })
            return result
    
        except Exception as e:
            print("This block is being executed.")
            logger.info(f"Error in fetching registerdata and examine  {e}")
            return {
            "status": "Error",
            "message": "An error occurred while fetching details.",
            "error": str(e)
        }

            
    def fetch_data_both_table(self,json_data):
        # json_data =  {"cc_no" : 13012}
        # print(json_data,"json")
        
        try:
            cc_no= json_data[0].get("cc_no")
            print(cc_no,"cc_no                 ")
            # query =  "SELECT * FROM registration left join  examine_details on registration.cc_no = examine_details.cc_no where registration.cc_no = %s"
            query1 = "SELECT * FROM   registration where cc_no = %s"
            query2 = "SELECT * FROM   examine_details where cc_no = %s"
            query3 = "SELECT * FROM   attempts where cc_no = %s"
            detail_table2 = self.db_manager.execute_query(query2,(cc_no,))
            detail_table1 = self.db_manager.execute_query(query1,(cc_no,))
            detail_table3 = self.db_manager.execute_query(query3,(cc_no,))
            
            
            # print(detail_table1,detail_table2,"[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
            if detail_table1 and not detail_table2:
                print("true false")
                result = ({
                                "cc_no": cc_no,
                                "status": "Sucessfully fetched one table table",
                                "message": "Registration details fetched and examine the person below table.",
                                "bio" :    detail_table1,
                                "Safety_training"  : detail_table2
                            })
                # print(detail_table2,"detail_table")
            # elif detail_table1 and detail_table2:
            #         print("true true")
            #         result = ({
            #                     "cc_no": cc_no,
            #                     "status": "Sucessfully fetched two table",
            #                     "message": "Registration and examine details fetched.",
            #                     "bio" :    detail_table1,
            #                     "Safety_training"  : detail_table2
            #                 })
            elif detail_table1 and detail_table2 and detail_table3:
                    print("true true true")
                    result = ({
                                "cc_no": cc_no,
                                "status": "Sucessfully fetched three table",
                                "message": "Registration , examine  and attempts details fetched.",
                                "bio" :    detail_table1,
                                "Safety_training"  : detail_table2,
                                "Cycle_games"  : detail_table3
                            })
                                    
            else:
                    print("This block is being executed.")
                    logger.info("Error in fetching register data and examine  for {}".format(cc_no))
                    result = ({
                                "cc_no": cc_no,
                                "status": "Failed fetched  any table",
                                "message": "There is no such cc_no,enter the new details."
                            })
            return result
    
        except Exception as e:
            print("This block is being executed.")
            logger.info(f"Error in fetching all table  {e}")
            return {
            "status": "Error",
            "message": "An error occurred while fetching details.",
            "error": str(e)
        }

          
    def fetch_registration_details(self,):
        # json_data =  {"cc_no" : 13012}
        # print(json_data,"json")
        
        try:

            # query =  "SELECT * FROM registration left join  examine_details on registration.cc_no = examine_details.cc_no where registration.cc_no = %s"
            query = "SELECT * FROM   registration"

            detail_table = self.db_manager.execute_query(query)
            if detail_table:
                    result = ({
                                
                                "status": "Sucessfully fetched   overall table",
                                "message": "overall Registration details fetched.",
                                "Full_table" :    detail_table
                                
                            })
                                    
            else:
                    # print("This block is being executed.")
                    logger.info("Error in fetching register all data ")
                    result = ({
                               
                                "status": "Failed fetched   table  data",
                                "message": "Cant able to fetch all data."
                            })
            return result
    
        except Exception as e:
            print("This block is being executed.")
            logger.info(f"Error in fetching registerdata and examine  {e}")
            return {
            "status": "Error",
            "message": "An error occurred while fetching details.",
            "error": str(e)
        }

# bio_fetch_service.fetch_data("Registration",json_data = None)