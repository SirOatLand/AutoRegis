import datetime
import schedule
import time
import subprocess

def run_bash_script():
    subprocess.run(['bash', 'regis.sh', './curl.sh'])

# Schedule the execution of the bash script at a specific time
schedule.every().day.at("12:38:30").do(run_bash_script)

subprocess.run(['clear'])
while True:
    if schedule.next_run:
        time_until_next_run = str(datetime.timedelta(seconds=int(schedule.idle_seconds())))
        print(f"\rTime until registration: {time_until_next_run} seconds", end="")
    time.sleep(1)
    schedule.run_pending()
