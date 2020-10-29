prev_time = 0
prev_rep = 0
N = 0
m = 0
t = 0
count = 1
average_list = []
ave_cnt = 0
average = 0

file_path = 'test/obs_log_file.txt'
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
      breakminute = (next_time - prev_time)//60
      breaksecond = (next_time - prev_time - breakminute*60)
      print(str(breakminute) + '分' + str(breaksecond) + '秒')
      ave_cnt += 1
      if ave_cnt <= m:
        average_list.append(next_rep)
        for i in average_list:
          average += int(i)
        # print(average, 'if ave1 elif')
        average /= len(average_list)
        # print(average_list, 'if list elif')
        # print(len(average_list), 'if len elif')
        # print(average, 'if ave2')
        if average >= t:
          print('サーバが過負荷状態です')
        average = 0
      else:
        average_list.pop(0)
        average_list.append(next_rep)
        # print(average_list, 'else list elif')
        # print(len(average_list), 'else len elif')
        for i in average_list:
          average += int(i)
        average /= len(average_list) 
        # print(average, 'else ave elif')
        if average >= t:
          print('サーバが過負荷状態です')
        average = 0
      prev_rep = next_rep

    elif prev_rep != '-' and next_rep == '-':
      prev_time = int(LineSplit[0][-4] + LineSplit[0][-3])*60 + int(LineSplit[0][-2] + LineSplit[0][-1])
      prev_rep = '-' # prev_rep = next_rep
      count = 1

    elif prev_rep == '-' and next_rep == '-':
      count += 1
      if count >= N:
        print('サーバの故障')
        print(x)
        break

    elif prev_rep != '-' and next_rep != '-':
      prev_time = int(LineSplit[0][-4] + LineSplit[0][-3])*60 + int(LineSplit[0][-2] + LineSplit[0][-1])
      ave_cnt += 1
      if ave_cnt <= m:
        average_list.append(next_rep)
        for i in average_list:
          average += int(i)
        # print(average, 'if ave1')
        average /= len(average_list)
        # print(average_list, 'if list')
        # print(len(average_list), 'if len')
        # print(average, 'if ave2')
        if average >= t:
          print('サーバが過負荷状態です')
        average = 0
      else:
        average_list.pop(0)
        average_list.append(next_rep)
        # print(average_list, 'else list')
        # print(len(average_list), 'else len')
        for i in average_list:
          average += int(i)
        average /= len(average_list) 
        # print(average, 'else ave')
        if average >= t:
          print('サーバが過負荷状態です')
        average = 0
      prev_rep = next_rep



    # if ave_cnt == 0:
    #   average = int(next_rep)
    #   ave_cnt += 1
    # elif ave_cnt <= m:
    #   average = int((average*ave_cnt + int(next_rep))/(ave_cnt+1))
    #   ave_cnt += 1
    #   if average >= t:
    #     print('サーバが過負荷状態です')