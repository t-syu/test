import os

class WithTest:
  def __init__(self, file_name):
    self.__file_name = file_name

  def __enter__(self):
    self.__file = open(self.__file_name, mode='a', encoding='utf-8')
    return self
  
  def write(self, msg):
    self.__file.write(msg)

  def __exit__(self, exc_type, exc_val, traceback): #exc_type,exc_val, traceback はエラーが発生した時に, エラーを検出してくれるはず
    self.__file.close()

file_path = 'test/obs_log_file.txt'
with open(file_path, mode='r', encoding='utf-8') as f:
  lines = f.readlines()
  param = ''
  for x in lines:
    line = x.rstrip('\n')
    LineSplit = line.split(',')
    if LineSplit[0] == '!':
      param = x
      continue
    file_name = LineSplit[1].split('/')
    file_path = 'test/' + file_name[0] + '.txt'
    MyCheck = os.path.isfile(file_path)
    if not MyCheck:
      with WithTest(file_path) as t:
        t.write(param)
    
    with WithTest(file_path) as t:
      t.write(x)