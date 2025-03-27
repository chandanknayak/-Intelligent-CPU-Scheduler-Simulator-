class Process:
    def __init__(self, pid, arrival_time, burst_time, priority=0):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.waiting_time = 0
        self.turnaround_time = 0
        self.completion_time = 0

def get_process_input():
    processes = []
    n = int(input("Enter number of processes: "))
    for i in range(n):
        pid = i + 1
        arrival_time = int(input(f"Enter arrival time for P{pid}: "))
        burst_time = int(input(f"Enter burst time for P{pid}: "))
        priority = int(input(f"Enter priority for P{pid} (lower value = higher priority): ")) if input("Use priority? (y/n): ").lower() == 'y' else 0
        processes.append(Process(pid, arrival_time, burst_time, priority))
    return processes
