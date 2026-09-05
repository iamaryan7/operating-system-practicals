# Round Robin (RR) CPU Scheduling Algorithm
# Calculates Average Waiting Time and Average Turnaround Time

from collections import deque

def round_robin():
    print("===== Round Robin (RR) CPU Scheduling =====\n")

    n = int(input("Enter the number of processes: "))
    time_quantum = int(input("Enter Time Quantum: "))

    processes = []

    # Input process details
    for i in range(n):
        print(f"\nProcess P{i+1}:")
        arrival = int(input("  Arrival Time: "))
        burst = int(input("  Burst Time: "))
        processes.append({
            "pid": f"P{i+1}",
            "arrival": arrival,
            "burst": burst,
            "remaining": burst,          # Remaining burst time
            "completion": 0,
            "waiting": 0,
            "turnaround": 0,
            "started": False
        })

    # Sort processes by arrival time
    processes.sort(key=lambda x: x["arrival"])

    ready_queue = deque()
    current_time = 0
    completed = 0
    i = 0  # Index to track which processes have arrived

    # Add first process(es) that arrive at time 0 (or earliest)
    while i < n and processes[i]["arrival"] <= current_time:
        ready_queue.append(processes[i])
        i += 1

    print("\n" + "-" * 85)
    print(f"{'Process':<10}{'Arrival':<12}{'Burst':<10}{'Completion':<14}{'Waiting':<12}{'Turnaround':<12}")
    print("-" * 85)

    while completed < n:
        if not ready_queue:
            # CPU is idle → jump to next process arrival
            current_time = processes[i]["arrival"]
            while i < n and processes[i]["arrival"] <= current_time:
                ready_queue.append(processes[i])
                i += 1
            continue

        # Get the next process from ready queue
        current = ready_queue.popleft()

        # Execute for min(time_quantum, remaining time)
        exec_time = min(time_quantum, current["remaining"])
        current["remaining"] -= exec_time
        current_time += exec_time

        # Add newly arrived processes during this execution
        while i < n and processes[i]["arrival"] <= current_time:
            ready_queue.append(processes[i])
            i += 1

        if current["remaining"] > 0:
            # Process is not finished → put it back in the queue
            ready_queue.append(current)
        else:
            # Process completed
            current["completion"] = current_time
            current["turnaround"] = current["completion"] - current["arrival"]
            current["waiting"] = current["turnaround"] - current["burst"]
            completed += 1

    # Calculate totals and print results
    total_waiting = 0
    total_turnaround = 0

    # Sort by Process ID for nice display
    processes.sort(key=lambda x: x["pid"])

    for p in processes:
        print(f"{p['pid']:<10}{p['arrival']:<12}{p['burst']:<10}"
              f"{p['completion']:<14}{p['waiting']:<12}{p['turnaround']:<12}")
        total_waiting += p["waiting"]
        total_turnaround += p["turnaround"]

    avg_waiting = total_waiting / n
    avg_turnaround = total_turnaround / n

    print("-" * 85)
    print(f"\nAverage Waiting Time     : {avg_waiting:.2f}")
    print(f"Average Turnaround Time  : {avg_turnaround:.2f}")
    print("-" * 85)


# Run the program
if __name__ == "__main__":
    round_robin()