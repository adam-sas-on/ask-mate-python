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


    :type title: object
    :param title: Title question - string
    :param question: Content question - string
    :param image: optional url to image - string - when image url isn't added default write to base string 'None'
    :return number new question id
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
        print(new_record['id'])
        return new_record['id']


def add_new_answer_to_base(question_id, answer, image='None'):
    """
    This function added new question to "question.csv" base


    :param question_id: question id - decimal string or int
    :param answer: Content question - string
    :param image: optional url to image - string - when image url isn't added default write to base string 'None'
    :return
    """
    try:
        exist_base = connection.get_list_records_from_data('answer')
        exist_answer_to_question = [answer for answer in exist_base if answer['question_id'] == question_id]
    except ValueError('Problem which base!!!') as err:
        return err
    else:
        max_exist_id = 1
        for record in exist_answer_to_question:
            if int(record['id']) > max_exist_id:
                max_exist_id = int(record['id'])

        new_record = dict()
        new_record['id'] = max_exist_id + 1
        new_record['submission_time'] = utc_time
        new_record['vote_number'] = 0
        new_record['question_id'] = question_id
        new_record['message'] = answer
        new_record['image'] = image

        connection.add_new_record_question('answer', exist_base, new_record)


def get_all_answers_by_id(question_id):
    """
    If you need all answers for concrete question
    This function return all records with answer by id question
    :param question_id: id question - int or decimal str
    :return: dictionaries of combined answer
    """
    try:
        exist_answer = get_list_all_records('answer')

    except ValueError('Problem whit database answer')as err:
        return err

    else:
        combined_answer = [record for record in exist_answer if int(record['question_id']) == int(question_id)]
        return combined_answer


def get_single_question_by_id(question_id):
    """
    If you need concrete question by id
    This function return dictionary with items question
    :param question_id: id question - int or decimal str
    :return: dictionary with items question
    """
    try:
        exist_question = get_list_all_records('question')

    except ValueError('Problem whit database question')as err:
        return err

    else:
        question = [record for record in exist_question if int(record['id']) == int(question_id)]
        return dict(question[0])


def increment_value(which_base, question_id, answer_id=False, which_value='vote_number', up_or_down='up'):
    """
    This function increment or decrement possible value in database

    :param which_base: 'answer' or 'question' - string
    :param question_id: question id to change - int or decimal string
    :param answer_id: answer id to change - int or decimal string
    :param which_value: which value to change 'vote_number' or 'view_number' - string
    :param up_or_down: 'up' or 'down' - increment or decrement - string
    :return: change value in checked base
    """
    records = get_list_all_records(which_base)

    def change():
        if up_or_down == 'up':
            record[which_value] = int(record[which_value]) + 1
        elif up_or_down == 'down':
            record[which_value] = int(record[which_value]) - 1

    if which_base == 'question':
        for record in records:
            if int(record['id']) == int(question_id):
                change()
    elif which_base == 'answer':
        for record in records:
            if int(record['question_id']) == int(question_id) and int(record['id']) == int(answer_id):
                change()

    connection.add_new_record_question(which_base, records)
