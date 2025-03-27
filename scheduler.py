def fcfs_scheduling(processes):
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
