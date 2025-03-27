def calculate_performance_metrics(processes):
    if not processes:
        print("Error: No processes to calculate metrics.")
        return None, None

    total_waiting_time = sum(p.waiting_time for p in processes)
    total_turnaround_time = sum(p.turnaround_time for p in processes)
    avg_waiting_time = total_waiting_time / len(processes)
    avg_turnaround_time = total_turnaround_time / len(processes)

    print(f"✅ Average Waiting Time: {avg_waiting_time:.2f}")
    print(f"✅ Average Turnaround Time: {avg_turnaround_time:.2f}")

    return avg_waiting_time, avg_turnaround_time

if __name__ == "__main__":
    from scheduler import fcfs_scheduling
    from process_input import get_process_input
    from report_generator import generate_report

    # Get process input
    processes = get_process_input()
    if not processes:
        print("⚠️ No processes provided. Exiting...")
        exit(1)

    # Run FCFS Scheduling
    scheduled_processes = fcfs_scheduling(processes)

    # Calculate metrics
    avg_wait, avg_turn = calculate_performance_metrics(scheduled_processes)
    if avg_wait is None or avg_turn is None:
        print("⚠️ Unable to generate report due to missing metrics.")
    else:
        # Generate report
        generate_report(scheduled_processes, avg_wait, avg_turn)
