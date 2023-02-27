def read_file(fpath):
    with open(fpath, mode='r', encoding='utf8') as f:
        return f.read()
#data = utils.read_file(fpath='rawdata.txt')