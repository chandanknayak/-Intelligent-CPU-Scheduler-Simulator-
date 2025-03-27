def calculate_performance_metrics(processes):
    """Calculates average waiting time and turnaround time for scheduled processes."""
    total_waiting_time = sum(p.waiting_time for p in processes)
    total_turnaround_time = sum(p.turnaround_time for p in processes)
    
    avg_waiting_time = total_waiting_time / len(processes)
    avg_turnaround_time = total_turnaround_time / len(processes)

    print(f"Average Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")

    return avg_waiting_time, avg_turnaround_time

if __name__ == "__main__":
    from scheduler import fcfs_scheduling, sjf_scheduling, priority_scheduling, round_robin_scheduling
    from process_input import get_process_input
    from report_generator import generate_report

    # Get user input for processes
    processes, scheduling_type, quantum = get_process_input()

    # Apply the selected scheduling algorithm
    if scheduling_type == "fcfs":
        scheduled = fcfs_scheduling(processes)
    elif scheduling_type == "sjf":
        scheduled = sjf_scheduling(processes)
    elif scheduling_type == "priority":
        scheduled = priority_scheduling(processes)
    elif scheduling_type == "rr":
        scheduled = round_robin_scheduling(processes, quantum)
    else:
        print("Invalid scheduling type selected.")
        exit()

    # Calculate metrics and generate report
    avg_wait, avg_turn = calculate_performance_metrics(scheduled)
    generate_report(scheduled, avg_wait, avg_turn)
