import schedule
from process import execute


def job():
    print("HELLO \n")


schedule.every(5).seconds.do(execute)

while True:
    schedule.run_pending()
