def generate_report(processes, avg_waiting_time, avg_turnaround_time):
    with open("cpu_scheduling_report.txt", "w") as file:
        file.write("PID\tArrival\tBurst\tWaiting\tTurnaround\n")
        for p in processes:
            file.write(f"{p.pid}\t{p.arrival_time}\t{p.burst_time}\t{p.waiting_time}\t{p.turnaround_time}\n")

        file.write("\n")
        file.write(f"Average Waiting Time: {avg_waiting_time:.2f}\n")
        file.write(f"Average Turnaround Time: {avg_turnaround_time:.2f}\n")

    print("Report generated: cpu_scheduling_report.txt")