import os

def generate_report(processes, avg_waiting_time, avg_turnaround_time, filename="cpu_scheduling_report.txt"):
    if not processes:
        print("⚠️ No processes provided. Report generation skipped.")
        return
    
    with open(filename, "w") as file:
        file.write("📊 CPU Scheduling Report\n")
        file.write("=" * 40 + "\n")
        file.write("PID\tArrival\tBurst\tWaiting\tTurnaround\n")
        file.write("-" * 40 + "\n")
        
        for p in processes:
            file.write(f"{p.pid}\t{p.arrival_time}\t{p.burst_time}\t{p.waiting_time}\t{p.turnaround_time}\n")

        file.write("\n")
        file.write("=" * 40 + "\n")
        file.write(f"✅ Average Waiting Time: {avg_waiting_time:.2f} ms\n")
        file.write(f"✅ Average Turnaround Time: {avg_turnaround_time:.2f} ms\n")

    print(f"📂 Report generated successfully: {os.path.abspath(filename)}")
