import matplotlib.pyplot as plt

def plot_gantt_chart(processes):
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
