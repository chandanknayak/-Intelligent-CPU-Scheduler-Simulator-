def fcfs_scheduling(processes):
    """ First-Come, First-Serve (FCFS) Scheduling """
    processes.sort(key=lambda x: x.arrival_time)
    current_time = 0
    for process in processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time
        process.waiting_time = current_time - process.arrival_time
        process.completion_time = current_time + process.burst_time
        process.turnaround_time = process.waiting_time + process.burst_time
        current_time += process.burst_time
    return processes

def sjf_scheduling(processes):
    """ Shortest Job First (SJF) Scheduling - Non-Preemptive """
    processes.sort(key=lambda x: (x.arrival_time, x.burst_time))
    completed = []
    current_time = 0
    while processes:
        available = [p for p in processes if p.arrival_time <= current_time]
        if not available:
            current_time += 1
            continue
        shortest = min(available, key=lambda x: x.burst_time)
        processes.remove(shortest)
        shortest.waiting_time = current_time - shortest.arrival_time
        shortest.completion_time = current_time + shortest.burst_time
        shortest.turnaround_time = shortest.waiting_time + shortest.burst_time
        current_time += shortest.burst_time
        completed.append(shortest)
    return completed

def priority_scheduling(processes):
    """ Priority Scheduling (Lower value = Higher Priority) - Non-Preemptive """
    processes.sort(key=lambda x: (x.arrival_time, x.priority))
    completed = []
    current_time = 0
    while processes:
        available = [p for p in processes if p.arrival_time <= current_time]
        if not available:
            current_time += 1
            continue
        highest_priority = min(available, key=lambda x: x.priority)
        processes.remove(highest_priority)
        highest_priority.waiting_time = current_time - highest_priority.arrival_time
        highest_priority.completion_time = current_time + highest_priority.burst_time
        highest_priority.turnaround_time = highest_priority.waiting_time + highest_priority.burst_time
        current_time += highest_priority.burst_time
        completed.append(highest_priority)
    return completed

def round_robin_scheduling(processes, quantum):
    """ Round Robin Scheduling """
    queue = processes[:]
    time = 0
    while queue:
        for process in queue[:]:
            if process.remaining_time > quantum:
                time += quantum
                process.remaining_time -= quantum
            else:
                time += process.remaining_time
                process.remaining_time = 0
                process.completion_time = time
                process.turnaround_time = process.completion_time - process.arrival_time
                process.waiting_time = process.turnaround_time - process.burst_time
                queue.remove(process)
    return processes
