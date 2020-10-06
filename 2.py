time = int(input('Введи время в секундах'))
seconds = time % 60
hours = time // 3600
minutes = (time // 60) - (hours * 60)

if seconds < 10:
    seconds = '0' + str(seconds)
if minutes < 10:
    minutes = '0' + str(minutes)
if hours < 10:
    hours = '0' + str(hours)

print('{}:{}:{}'.format(hours, minutes, seconds))
