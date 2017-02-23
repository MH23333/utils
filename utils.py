
def readfile(filename, separator='\t'):
    res = []
    with open(filename, 'rb') as f:
        for line in f:
            arr = f.split(separator)
            res.append(arr)
    return res
