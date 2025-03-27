import tkinter as tk
from scheduler import fcfs_scheduling
from process_input import get_process_input

class CPUSchedulerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("CPU Scheduler Simulator")
        self.process_list = []

        self.label = tk.Label(root, text="CPU Scheduler", font=("Arial", 14))
        self.label.pack()

        self.add_process_button = tk.Button(root, text="Add Processes", command=self.add_processes)
        self.add_process_button.pack()

        self.run_fcfs_button = tk.Button(root, text="Run FCFS", command=self.run_fcfs)
        self.run_fcfs_button.pack()

        self.result_text = tk.Text(root, height=10, width=50)
        self.result_text.pack()

    def add_processes(self):
        self.process_list = get_process_input()

    def run_fcfs(self):
        scheduled = fcfs_scheduling(self.process_list)
        self.display_results(scheduled)

    def display_results(self, processes):
        self.result_text.delete('1.0', tk.END)
        self.result_text.insert(tk.END, "PID\tArrival\tBurst\tWaiting\tTurnaround\n")
        for p in processes:
            self.result_text.insert(tk.END, f"{p.pid}\t{p.arrival_time}\t{p.burst_time}\t{p.waiting_time}\t{p.turnaround_time}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = CPUSchedulerGUI(root)
    root.mainloop()
