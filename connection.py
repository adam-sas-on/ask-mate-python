import csv

DELIMITER = ','
FIELDNAMES_FOR_QUESTION = ['id', 'submission_time', 'view_number', 'vote_number', 'message', 'image']
FIELDNAMES_FOR_ANSWER = ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'image']
BASE_NAME_QUESTIONS = 'question.csv'
BASE_NAME_ANSWER = 'answer.csv'


def get_list_records_from_data(which_base):

    if which_base == 'question':
        base_name = BASE_NAME_QUESTIONS
    elif which_base == 'answer':
        base_name = BASE_NAME_ANSWER
    else:
        raise ValueError('Wrong database name "which_base"')

    with open(base_name, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=DELIMITER)
        list_of_records = []
        for record in csv_reader:
            list_of_records.append(record)
        return list_of_records


def add_new_record_question(which_base, exist_records_list, new_record=False):

    if which_base == 'question':
        base_name = BASE_NAME_QUESTIONS
        field = FIELDNAMES_FOR_QUESTION
    elif which_base == 'answer':
        base_name = BASE_NAME_ANSWER
        field = FIELDNAMES_FOR_ANSWER
    else:
        raise ValueError('Wrong database name "which_base"')

    with open(base_name, 'w') as update_file:
        csv_writer = csv.DictWriter(update_file, fieldnames=field , delimiter=DELIMITER)
        csv_writer.writeheader()
        if exist_records_list:
            for record in exist_records_list:
                csv_writer.writerow(record)
        if new_record:
            csv_writer.writerow(new_record)
