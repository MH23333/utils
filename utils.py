import datetime


def readfile(filename, separator='\t'):
    res = []
    with open(filename, 'rb') as f:
        for line in f:
            arr = f.split(separator)
            res.append(arr)
    return res


def get_datetime(date_format='%Y/%m/%d %H:%M:%S'):
    return datetime.datetime.now().strftime(format=date_format)