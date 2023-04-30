
import queue
import pprint
import random
from collections import namedtuple


Event = namedtuple("Event", "time proc action")


class Simulator:
    def __init__(self, procs_map):
        self.events = queue.PriorityQueue()
        self.procs = dict(procs_map)

    def run(self, end_time):
        for _, proc in sorted(self.procs.items()):
            first = next(proc)
            print(first)
            self.events.put(first)

        time_ = 0
        while time_ <= end_time:
            if self.events.empty():
                break

            current_event = self.events.get()
            time_, proc_id, _ = current_event
            print(f"Taxi: {proc_id} | {current_event}")
            active_proc = self.procs[proc_id]
            next_time = time_ + random.randint(1, 10)
            
            try:
                next_event = active_proc.send(next_time)
                self.events.put(next_event)
            except StopIteration:
                del self.procs[proc_id]
        else:
            print(f"End of simulation time: {self.events.qsize()} events pending")
        print("Finished")

def taxi_process(ident, trips, start_time=0):
    time = yield Event(start_time, ident, "Leave garage")

    for _ in range(trips):
        time = yield Event(time, ident, "Pick up passenger")
        time = yield Event(time, ident, "Drop off passenger")

    yield Event(time, ident, "Going home")


if __name__ == "__main__":

    taxies = {i: taxi_process(i, (i + 1) * 2, i*10) for i in range(3)}

    sim = Simulator(taxies)
    sim.run(90)
