class Process:
    def __init__(self, pid, arrival_time, burst_time, priority=0):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.waiting_time = 0
        self.turnaround_time = 0
        self.completion_time = 0
        self.remaining_time = burst_time  # Needed for Round Robin

def get_process_input():
    processes = []

    # Choose Scheduling Algorithm
    print("\n🔹 Choose a Scheduling Algorithm:")
    print("1️⃣ FCFS (First-Come, First-Serve)")
    print("2️⃣ SJF (Shortest Job First)")
    print("3️⃣ Round Robin")
    print("4️⃣ Priority Scheduling")

    algo_choice = input("Enter choice (1-4): ").strip()
    while algo_choice not in {'1', '2', '3', '4'}:
        print("❌ Invalid choice! Please enter 1, 2, 3, or 4.")
        algo_choice = input("Enter choice (1-4): ").strip()

    # Get Number of Processes
    n = int(input("\n🔹 Enter number of processes: "))
    while n <= 0:
        print("❌ Number of processes must be greater than 0.")
        n = int(input("\n🔹 Enter number of processes: "))

    # Get Process Details
    for i in range(n):
        pid = i + 1
        arrival_time = int(input(f"⏳ Enter arrival time for P{pid}: "))
        burst_time = int(input(f"⚡ Enter burst time for P{pid}: "))

        priority = 0
        if algo_choice == '4':  # Priority Scheduling
            priority = int(input(f"🏅 Enter priority for P{pid} (lower value = higher priority): "))

        processes.append(Process(pid, arrival_time, burst_time, priority))

    # If Round Robin, ask for Quantum Time
    quantum = None
    if algo_choice == '3':  # Round Robin
        quantum = int(input("\n⏳ Enter time quantum for Round Robin: "))

    return processes, algo_choice, quantum
