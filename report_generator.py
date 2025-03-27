def generate_report(processes, avg_waiting_time, avg_turnaround_time):
    """Generates a report file with process execution details."""
    with open("cpu_scheduling_report.txt", "w") as file:
        file.write("PID\tArrival\tBurst\tWaiting\tTurnaround\n")
        for p in processes:
            file.write(f"{p.pid}\t{p.arrival_time}\t{p.burst_time}\t{p.waiting_time}\t{p.turnaround_time}\n")

        file.write("\n")
        file.write(f"Average Waiting Time: {avg_waiting_time:.2f}\n")
        file.write(f"Average Turnaround Time: {avg_turnaround_time:.2f}\n")

    print("Report generated: cpu_scheduling_report.txt")

if __name__ == "__main__":
    from process_input import get_process_input
    from metrics_calculator import calculate_performance_metrics
    from scheduler import fcfs_scheduling, sjf_scheduling, priority_scheduling, round_robin_scheduling

    # Get process input
    processes, scheduling_type, quantum = get_process_input()

    # Apply scheduling algorithm
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

    # Generate report after calculations
    avg_wait, avg_turn = calculate_performance_metrics(scheduled)
    generate_report(scheduled, avg_wait, avg_turn)
