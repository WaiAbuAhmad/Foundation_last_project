import json
from soduko_version3 import grid_creater

def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)

path = "./flaskr/static"
fileName = "sudoku"
# Example
data = grid_creater()


writeToJSONFile(path,fileName,data)
# './' represents the current directory so the directory save-file.py is in
# 'test' is my file name