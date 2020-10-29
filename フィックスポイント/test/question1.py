
def question1(file_path):
  prev_time = 0
  prev_rep = ''

  with open(file_path, mode='r', encoding='utf-8') as f:
    lines = f.readlines()
    for x in lines:
      line = x.rstrip('\n')
      LineSplit = line.split(',')

      if LineSplit[0] == '!':
        N = int(LineSplit[1])
        continue

      next_rep = LineSplit[2]
      next_time = int(LineSplit[0][-4] + LineSplit[0][-3])*60 + int(LineSplit[0][-2] + LineSplit[0][-1])
      
      if prev_rep == '-' and prev_rep != next_rep:
        print('故障期間')
        breakminute = (next_time - prev_time)//60
        breaksecond = (next_time - prev_time - breakminute*60)
        print(str(breakminute) + '分' + str(breaksecond) + '秒')
        prev_rep = next_rep
      
      elif next_rep == '-' and next_rep != prev_rep:
        prev_time = next_time
        prev_rep = next_rep

file_path_list = []
file_path = 'test/obs_log_file.txt'
with open(file_path, mode='r', encoding='utf-8') as f:
  lines = f.readlines()
  for x in lines:
    line = x.rstrip('\n')
    LineSplit = line.split(',')
    if LineSplit[0] != '!':
      file_name = LineSplit[1].split('/')
      file_path = 'test/' + file_name[0] + '.txt'
      file_bit = int(file_name[1]) + 2 # サブネット化で2ビット拡張させた。
      if not file_path_list:
        file_path_list.append(file_path)
      if not file_path in file_path_list:
        file_path_list.append(file_path)

for x in file_path_list:
  print('サーバーアドレス：' + x.strip('test/').rstrip('.txt'))
  question1(x)