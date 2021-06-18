import schedule
from process import execute
import time
from continuous import continuous
from keep import keep

# schedule.every().day.at("17:24").do(execute)
schedule.every().hour.do(keep)
schedule.every(2).hours.do(execute)

# schedule.every(10).seconds.do(execute)

continuous()
while True:
    schedule.run_pending()
    time.sleep(1)
