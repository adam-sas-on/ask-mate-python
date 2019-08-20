"""All database questions should be implemented using this module through connection module"""

import connection
import time

utc_time = int(time.time())


def get_list_all_records(which_base):
    """
    This function return all records (question or answer) from database


    :param which_base: 'question' or 'answer' - required
    :return: list of dictionaries all which records from marked database
    """
    list_of_records = connection.get_list_records_from_data(which_base)
    return list_of_records


def add_new_question_to_base(title, question, image='None'):
    """
    This function added new question to "question.csv" base


    :param title: Title question - string
    :param question: Content question - string
    :param image: optional url to image - string - when image url isn't added default write to base string 'None'
    """

    exist_base = connection.get_list_records_from_data('question')

    try:
        max_exist_id = 0
        for record in exist_base:
            if int(record['id']) > max_exist_id:
                max_exist_id = int(record['id'])
    except ValueError('Problem which base!!!') as err:
        return err
    else:
        new_record = dict()
        new_record['id'] = max_exist_id + 1
        new_record['submission_time'] = utc_time
        new_record['view_number'] = 0
        new_record['vote_number'] = 0
        new_record['title'] = title
        new_record['message'] = question
        new_record['image'] = image

        connection.add_new_record_question('question', exist_base, new_record)
