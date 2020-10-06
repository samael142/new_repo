time = int(input('Введи время в секундах'))
seconds = time % 60
hours = time // 3600
minutes = (time // 60) - (hours * 60)
print('%02d:%02d:%02d' % (hours, minutes, seconds))
