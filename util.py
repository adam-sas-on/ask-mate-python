from datetime import datetime

def time_convert(timestamp):
    return datetime.fromtimestamp(int(timestamp)).strftime("%Y-%m-%d  %H:%M")    
#

