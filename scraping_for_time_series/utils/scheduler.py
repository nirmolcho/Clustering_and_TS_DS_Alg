import time
import threading


class Scheduler:
    def __init__(self):
        self.tasks = []
        self.start_time = None
        self.end_time = None

    def schedule(self, task, interval):
        multiplier = {'h': 3600, 'm': 60}
        time_val = int(interval[:-1])
        time_unit = interval[-1]

        if time_unit in multiplier:
            time_val *= multiplier[time_unit]
        else:
            print(f"Invalid time unit in interval: {interval}")
            return

        self.tasks.append((task, time_val))

    def start(self):
        while True:
            for task, interval in self.tasks:
                threading.Thread(target=self.run_task, args=(task, interval)).start()
            time.sleep(1)

    @staticmethod
    def run_task(task, interval):
        last_run = 0
        while True:
            if time.time() - last_run >= interval:
                task()
                last_run = time.time()
            time.sleep(1)

    def start_timer(self):
        self.start_time = time.time()

    def stop_timer(self):
        self.end_time = time.time()

    def get_elapsed_time(self):
        return str(timedelta(seconds=int(self.end_time - self.start_time)))

