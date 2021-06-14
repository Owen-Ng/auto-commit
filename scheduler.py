import schedule
from process import execute
import time
from continuous import continuous

schedule.every().day.at("17:24").do(execute)

# schedule.every(10).seconds.do(execute)

continuous()
while True:
    schedule.run_pending()
    time.sleep(1)
