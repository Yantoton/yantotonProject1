from datetime import datetime
now:datetime = datetime.now()
print(f'{now:%x}')
print(f'{now:%c}')
print(f'{now:%H:%M:%S}')
