import matplotlib.pyplot as plt

def plot_gantt_chart(processes):
    fig, ax = plt.subplots()
    start_time = 0
    timeline = []  # Stores (start_time, duration, process_id)

    for process in processes:
        if start_time < process.arrival_time:
            # Insert an idle period
            idle_time = process.arrival_time - start_time
            timeline.append((start_time, idle_time, "Idle"))
            start_time = process.arrival_time
        
        # Add process execution
        timeline.append((start_time, process.burst_time, f"P{process.pid}"))
        start_time += process.burst_time

    # Draw Gantt Chart
    for (start, duration, label) in timeline:
        ax.broken_barh([(start, duration)], (10, 9), facecolors='blue' if "P" in label else 'gray')
        ax.text(start + duration / 2, 15, label, ha='center', va='center', color='white')

    ax.set_xlabel("Time")
    ax.set_yticks([])
    ax.set_title("Gantt Chart")
    plt.show()
