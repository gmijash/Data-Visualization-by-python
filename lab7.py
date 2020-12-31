#Mijash Ghimire Code
#Student Western Oregon University
#2/26/2020

def print_data_point():
  data_points = []
  while True:
    data_point = input('Enter a data point (-1 to stop input):\n')
    if data_point == '-1':
      break
    elif ',' not in data_point:
      print('Error: No comma in string.')
      print()
    else:
      if len(data_point.split(',')) > 2:
        print ('Error: Too many commas in input.')
        print()
      else:
        if not(data_point.split()[-1].isnumeric()):
          print('Error: Comma not followed by an integer.')
          print()
        else:
          blist=data_point.split(',')
          print('Data string:',blist[0])
          print('Data integer:'+blist[1])
          print()
          blist[1] = int(blist[1])
          data_points.append(blist)
  return data_points


if __name__ == '__main__':
    data = input()
    print('Enter a title for the data:')
    print('You entered:',data)
    print()
    column_1 = input()
    print('Enter the column 1 header:')
    print('You entered:',column_1)
    print()
    column_2 = input()
    print('Enter the column 2 header:')
    print('You entered:',column_2)
    print()
    data_points = print_data_point()
    print()
    print('%33s' % data)
    print('%-20s|%23s' % (column_1, column_2))
    print('--------------------------------------------')
    for blist in data_points:
        print('%-20s|%23s' % (blist[0], str(blist[1])))
    
    for blist in data_points:
        print('\n%20s' % (blist[0]), end=' ')
        for j in range(blist[1]):
            print('*', end = '')
        
    print()
