from datetime import datetime

current_time = datetime.now()

hour_integer = current_time.hour

if 12<=hour_integer<13:
    print('Weak up & get fresh & take breakfast')
elif 13<=hour_integer<15:
    print('study fc & keep practice')
elif 15<=hour_integer<17:
    print('take care ruhu & give birds and dog food & Lunch')
elif 17<=hour_integer<19:
    print('workout time & Snack')
elif 19<=hour_integer<20:
    print('Return Home & do anykind of house work')
elif 20<=hour_integer<23:
    print('Family&Friends time & Learnin new code & learn new thinks')
elif 23<=hour_integer<24:
    print('Go to outside for walk or bike ride')
elif 24<=hour_integer<1:
    print('Play Fortnite game & dinner & coco dinner')
elif 1<=hour_integer<4:
    print('Again study fc & keep practice & complete task')
elif 4<=hour_integer<5:
    print('Watch Farming video on youtube')
else:
    print('Your bed is calling it\'s sleep time')
