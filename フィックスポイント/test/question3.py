def question3(file_path):
  prev_time = 0
  prev_rep = 0
  N = 0
  m = 0
  t = 0
  rep_cnt = 0
  average_list = []
  ave_cnt = 0
  average = 0
  time_list = []

  with open(file_path, mode='r', encoding='utf-8') as f:
    lines = f.readlines()
    for x in lines:
      line = x.rstrip('\n')
      LineSplit = line.split(',')
      if LineSplit[0] == '!':
        N = int(LineSplit[1])
        t = int(LineSplit[2])
        m = int(LineSplit[3])
        continue

      next_rep = LineSplit[2]
      next_time = int(LineSplit[0][-4] + LineSplit[0][-3])*60 + int(LineSplit[0][-2] + LineSplit[0][-1])

      if prev_rep == '-' and next_rep != '-': 
        print('故障期間')
        breakminute = (next_time - prev_time)//60
        breaksecond = (next_time - prev_time - breakminute*60)
        print(str(breakminute) + '分' + str(breaksecond) + '秒')
        ave_cnt += 1
        if ave_cnt <= m:
          average_list.append(next_rep)
          for i in average_list:
            average += int(i)
          average /= len(average_list)
          if average >= t:
            print('サーバが過負荷状態です')
            serverminute = (int(time_list[len(average_list)-1]) - int(time_list[0]))//60
            serversecond = (int(time_list[len(average_list)-1]) - int(time_list[0]) - serverminute*60)
            print(str(serverminute) + '分' + str(serversecond) + '秒')

          average = 0
        else:
          average_list.pop(0)
          average_list.append(next_rep)
          for i in average_list:
            average += int(i)
          average /= len(average_list) 
          if average >= t:
            print('サーバが過負荷状態です')
            serverminute = (int(time_list[len(average_list)-1]) - int(time_list[0]))//60
            serversecond = (int(time_list[len(average_list)-1]) - int(time_list[0]) - serverminute*60)
            print(str(serverminute) + '分' + str(serversecond) + '秒')
          average = 0
        prev_rep = next_rep

      elif prev_rep != '-' and next_rep == '-':
        prev_time = next_time
        prev_rep = '-' # prev_rep = next_rep
        rep_cnt = 1

      elif prev_rep == '-' and next_rep == '-':
        rep_cnt += 1
        if rep_cnt >= N:
          print('サーバの故障')

      elif prev_rep != '-' and next_rep != '-':
        ave_cnt += 1
        if ave_cnt <= m:
          time_list.append(next_time)
          average_list.append(next_rep)
          for i in average_list:
            average += int(i)
          average /= len(average_list)
          if average >= t:
            print('サーバが過負荷状態です')
            serverminute = (int(time_list[len(average_list)-1]) - int(time_list[0]))//60
            serversecond = (int(time_list[len(average_list)-1]) - int(time_list[0]) - serverminute*60)
            print(str(serverminute) + '分' + str(serversecond) + '秒')
          average = 0

        else:
          time_list.pop(0)
          average_list.pop(0)
          time_list.append(next_time)
          average_list.append(next_rep)
          for i in average_list:
            average += int(i)
          average /= len(average_list) 
          if average >= t:
            print('サーバが過負荷状態です')
            serverminute = (int(time_list[len(average_list)-1]) - int(time_list[0]))//60
            serversecond = (int(time_list[len(average_list)-1]) - int(time_list[0]) - serverminute*60)
            print(str(serverminute) + '分' + str(serversecond) + '秒')
          average = 0
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
  print(x.strip('test/').rstrip('.txt'))
  question3(x)