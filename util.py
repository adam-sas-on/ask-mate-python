from datetime import datetime


def time_convert(timestamp):
    return datetime.fromtimestamp(int(timestamp)).strftime("%Y-%m-%d  %H:%M")


def sort_data_by_time(records):
    """
        This function sort by time input data
    :param records: iterable object
    :return: sorted iterable object
    """
    sort_data = sorted(records, key=lambda time: int(time['submission_time']), reverse=True)
    return sort_data
