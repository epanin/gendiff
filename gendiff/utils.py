import argparse
    
def parse_args():    
    parser = argparse.ArgumentParser()
    parser.add_argument("firstfile", help="the file to compare with")
    parser.add_argument("secondfile", help="the file to be compared")
    return parser.parse_args()