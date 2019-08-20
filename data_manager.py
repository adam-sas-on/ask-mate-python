"""All database questions should be implemented using this module through connection module"""
import connection
import time

submission_time = time.time()

def get_list_all_records(which_base):
    """
    This function return all records (question or answer) from database


    :param which_base: 'question' or 'answer'
    :return: list of dictionaries all which records from marked database
    """
    list_of_records = connection.get_list_records_from_data(which_base)
    return list_of_records