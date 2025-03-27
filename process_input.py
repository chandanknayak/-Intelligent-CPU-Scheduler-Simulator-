class Process:
    def __init__(self, pid, arrival_time, burst_time, priority=0):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.waiting_time = 0
        self.turnaround_time = 0
        self.completion_time = 0
        self.remaining_time = burst_time  # Required for Round Robin

def get_process_input():
    """Takes input from the user for process scheduling."""
    processes = []
    n = int(input("Enter number of processes: "))
    
    scheduling_type = input("Select scheduling (FCFS/SJF/Priority/RR): ").lower()
    quantum = 0  # Only needed for Round Robin
    
    if scheduling_type == "rr":
        quantum = int(input("Enter time quantum for Round Robin: "))

    for i in range(n):
        pid = i + 1
        arrival_time = int(input(f"Enter arrival time for P{pid}: "))
        burst_time = int(input(f"Enter burst time for P{pid}: "))
        
        priority = 0
        if scheduling_type == "priority":
            priority = int(input(f"Enter priority for P{pid} (lower value = higher priority): "))
        
        processes.append(Process(pid, arrival_time, burst_time, priority))

    return processes, scheduling_type, quantum  # Return quantum for Round Robin
