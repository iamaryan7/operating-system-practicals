# Priority Scheduling (Non-Preemptive)
# Lower priority number = Higher priority
# Calculates Average Waiting Time and Average Turnaround Time

def priority_scheduling():
    print("===== Priority Scheduling (Non-Preemptive) =====")
    print("Note: Lower priority number means Higher priority\n")

    n = int(input("Enter the number of processes: "))

    processes = []

    # Input process details
    for i in range(n):
        print(f"\nProcess P{i+1}:")
        arrival = int(input("  Arrival Time: "))
        burst = int(input("  Burst Time: "))
        priority = int(input("  Priority: "))
        processes.append({
            "pid": f"P{i+1}",
            "arrival": arrival,
            "burst": burst,
            "priority": priority,
            "completed": False
        })

    current_time = 0
    completed = 0
    total_waiting = 0
    total_turnaround = 0
    result = []

    print("\n" + "-" * 90)
    print(f"{'Process':<10}{'Arrival':<10}{'Burst':<10}{'Priority':<10}{'Start':<10}{'Completion':<12}{'Waiting':<10}{'Turnaround':<12}")
    print("-" * 90)

    while completed < n:
        # Find all processes that have arrived and not yet completed
        available = [p for p in processes if p["arrival"] <= current_time and not p["completed"]]

        if not available:
            # If no process is available, jump to the next earliest arrival time
            next_arrival = min(p["arrival"] for p in processes if not p["completed"])
            current_time = next_arrival
            continue

        # Select the process with the highest priority (lowest priority number)
        # In case of tie, choose the one that arrived earlier
        selected = min(available, key=lambda x: (x["priority"], x["arrival"]))

        # Calculate times
        start_time = current_time
        completion_time = start_time + selected["burst"]
        turnaround_time = completion_time - selected["arrival"]
        waiting_time = turnaround_time - selected["burst"]

        # Update totals
        total_waiting += waiting_time
        total_turnaround += turnaround_time

        # Store result
        result.append({
            "pid": selected["pid"],
            "arrival": selected["arrival"],
            "burst": selected["burst"],
            "priority": selected["priority"],
            "start": start_time,
            "completion": completion_time,
            "waiting": waiting_time,
            "turnaround": turnaround_time
        })

        # Mark as completed and update current time
        selected["completed"] = True
        current_time = completion_time
        completed += 1

    # Print results in the order of execution
    for r in result:
        print(f"{r['pid']:<10}{r['arrival']:<10}{r['burst']:<10}{r['priority']:<10}"
              f"{r['start']:<10}{r['completion']:<12}{r['waiting']:<10}{r['turnaround']:<12}")

    # Calculate averages
    avg_waiting = total_waiting / n
    avg_turnaround = total_turnaround / n

    print("-" * 90)
    print(f"\nAverage Waiting Time     : {avg_waiting:.2f}")
    print(f"Average Turnaround Time  : {avg_turnaround:.2f}")
    print("-" * 90)


# Run the program
if __name__ == "__main__":
    priority_scheduling()