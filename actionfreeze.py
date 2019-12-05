from datetime import datetime, timedelta


def whilefreezed(h=0, m=0, s=0, f=None):
    now = str(datetime.now() + timedelta(hours=h, minutes=m, seconds=s))[10:-4]
    while str(datetime.now())[10:-4] != now:
        f()
    
