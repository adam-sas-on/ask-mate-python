import csv

DELIMITER = '\t'
FIELDNAMES = ['id', 'story_title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation']


def get_list_data():
    with open('data.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=DELIMITER)
        list_of_records = []
        for record in csv_reader:
            list_of_records.append(record)
        return list_of_records


def add_new_record(exist_records_list, new_record=False):
    with open('data.csv', 'w') as update_file:
        csv_writer = csv.DictWriter(update_file, fieldnames=FIELDNAMES, delimiter=DELIMITER)
        csv_writer.writeheader()
        if exist_records_list:
            for record in exist_records_list:
                csv_writer.writerow(record)
        if new_record:
            csv_writer.writerow(new_record)
