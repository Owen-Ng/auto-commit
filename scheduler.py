import schedule
from process import execute
import time

schedule.every().every().day.at("13:00").do(execute)

while True:
    schedule.run_pending()
    time.sleep(1)
