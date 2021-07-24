from datetime import datetime, date

def log_message(exc):
  now = datetime.now()
  date = now.strftime('%d-%m-%y')
  time = now.strftime('%H:%M:%S')
  
  file = open(f'./logs/logs_{date}.txt', mode='a', encoding='utf-8')
  file.write(f'{exc} -- at -- {time}\n')
  file.close()
