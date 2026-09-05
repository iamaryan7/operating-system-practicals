# Shortest Job First (SJF) - Non-Preemptive CPU Scheduling
# Calculates Average Waiting Time and Average Turnaround Time

def sjf_scheduling():
    print("===== Shortest Job First (SJF) - Non-Preemptive Scheduling =====\n")

    n = int(input("Enter the number of processes: "))

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
            "completed": False
        })

    current_time = 0
    completed = 0
    total_waiting = 0
    total_turnaround = 0
    result = []

    print("\n" + "-" * 80)
    print(f"{'Process':<10}{'Arrival':<12}{'Burst':<10}{'Start':<10}{'Completion':<12}{'Waiting':<10}{'Turnaround':<12}")
    print("-" * 80)

    while completed < n:
        # Find all processes that have arrived and not yet completed
        available = [p for p in processes if p["arrival"] <= current_time and not p["completed"]]

        if not available:
            # If no process is available, jump to the next earliest arrival time
            next_arrival = min(p["arrival"] for p in processes if not p["completed"])
            current_time = next_arrival
            continue

        # Select the process with the shortest burst time
        # (If tie, choose the one that arrived earlier)
        selected = min(available, key=lambda x: (x["burst"], x["arrival"]))

        # Calculate times
        start_time = current_time
        completion_time = start_time + selected["burst"]
        turnaround_time = completion_time - selected["arrival"]
        waiting_time = turnaround_time - selected["burst"]

        # Update totals
        total_waiting += waiting_time
        total_turnaround += turnaround_time

        # Store result for printing
        result.append({
            "pid": selected["pid"],
            "arrival": selected["arrival"],
            "burst": selected["burst"],
            "start": start_time,
            "completion": completion_time,
            "waiting": waiting_time,
            "turnaround": turnaround_time
        })

        # Mark as completed and update current time
        selected["completed"] = True
        current_time = completion_time
        completed += 1

    # Print in the order they were executed
    for r in result:
        print(f"{r['pid']:<10}{r['arrival']:<12}{r['burst']:<10}{r['start']:<10}{r['completion']:<12}{r['waiting']:<10}{r['turnaround']:<12}")

    # Calculate averages
    avg_waiting = total_waiting / n
    avg_turnaround = total_turnaround / n

    print("-" * 80)
    print(f"\nAverage Waiting Time     : {avg_waiting:.2f}")
    print(f"Average Turnaround Time  : {avg_turnaround:.2f}")
    print("-" * 80)


# Run the program
if __name__ == "__main__":
    sjf_scheduling()