def question2(file_path):
  prev_time = 0
  prev_rep = 0
  N = 0
  count = 0

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

      if prev_rep == '-' and next_rep != '-': 
        print('故障期間')
        breakminute = (next_time - prev_time)//60
        breaksecond = (next_time - prev_time - breakminute*60)
        print(str(breakminute) + '分' + str(breaksecond) + '秒')
        prev_time = next_time
        prev_rep = next_rep
      
      elif prev_rep != '-' and next_rep == '-':
        prev_time = next_time
        prev_rep = '-' # prev_rep = next_rep
        count = 1
      
      elif prev_rep == '-' and next_rep == '-': #prev_timeを更新しないことで最初の'-'のtimeを保持できる。
        count += 1
        if count >= N:
          print('サーバの故障')
          break
      
      elif prev_rep != '-' and next_rep != '-':
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
  question2(x)