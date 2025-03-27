# -Intelligent-CPU-Scheduler-Simulator-
CPU Scheduler Simulator
A simple GUI-based CPU scheduling simulator that helps users visualize and understand how different CPU scheduling algorithms work. This project is designed for students and beginners to learn about CPU scheduling without using command-line tools.

📌 What This Project Does
Allows users to enter process details (Process ID, Arrival Time, Burst Time).

Supports different CPU scheduling algorithms:

✅ First-Come-First-Serve (FCFS)

✅ Shortest Job First (SJF)

Displays Gantt Chart to show process execution order.

Calculates and shows:

⏳ Waiting Time

⏳ Turnaround Time

Generates a report file with scheduling results.

🛠️ How to Use (No Command Line Needed!)
Step 1: Open the Program
Double-click the gui.py file to start the program.

A window will open with the title "CPU Scheduler Simulator".

Step 2: Enter Process Details
Click "Add Processes" and enter:

Process ID (P1, P2, P3, etc.)

Arrival Time (When the process arrives)

Burst Time (How long the process runs)

Click OK to save the process.

Step 3: Run a Scheduling Algorithm
Select the algorithm:

Click "Run FCFS" for First-Come-First-Serve.

Click "Run SJF" for Shortest Job First.

The results will appear on the screen.

Step 4: View the Gantt Chart
A new window will open showing a Gantt Chart.

This chart displays the order in which processes run.

Step 5: View or Save the Report
The program automatically saves the results in a file:
📄 cpu_scheduling_report.txt

You can open this file in Notepad to see the details.

🖥️ Features
✔ Simple GUI (No command line needed!)
✔ Supports FCFS & SJF Scheduling
✔ Real-time Gantt Chart visualization
✔ Easy-to-read scheduling reports

📂 Files in This Project
File Name	Purpose
gui.py	User interface (start this file)
scheduler.py	Handles scheduling logic
gantt_chart.py	Draws Gantt chart
metrics_calculator.py	Calculates waiting & turnaround times
report_generator.py	Creates a scheduling report
process_input.py	Takes user input for processes
📜 No Need for Installation!
Just download the project, open the folder, and double-click gui.py to start. 🚀
