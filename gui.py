import matplotlib.pyplot as plt

def plot_gantt_chart(processes):
    """Plots the Gantt Chart for process execution timeline."""
    fig, ax = plt.subplots()
    start_time = 0

    for process in processes:
        ax.broken_barh([(start_time, process.burst_time)], (10, 9), facecolors='blue')
        ax.text(start_time + process.burst_time / 2, 15, f"P{process.pid}", ha='center', va='center')
        start_time += process.burst_time

    ax.set_xlabel("Time")
    ax.set_yticks([])
    ax.set_title("Gantt Chart")
    plt.show()

if __name__ == "__main__":
    from process_input import get_process_input
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

    # Plot Gantt chart after scheduling
    plot_gantt_chart(scheduled)
