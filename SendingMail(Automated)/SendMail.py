import yagmail
import time
from datetime import datetime as dt

sender="rishabh1599@gmail.com"
receiver="rishabh1599@gmail.com"

subject="Test Mail"
contents= """
Here is the content
"""

yag=yagmail.SMTP(user=sender,password="yvzs tuzj sgiv bien")
#os.getenv()
while True:
    currect_time=dt.now()
    if currect_time.hour==21 and currect_time.minute==12:
        yag.send(to=receiver,subject=subject,contents=contents)
        print("Email sent!")
        time.sleep(60)