from os import listdir
from os.path import join


def getting_files(link):
    return [join(link, f) for f in listdir(link)]
