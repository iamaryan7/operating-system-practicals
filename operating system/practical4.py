# FCFS CPU Scheduling Algorithm
# Calculates Average Waiting Time and Average Turnaround Time

def fcfs_scheduling():
    print("===== First Come First Serve (FCFS) Scheduling =====\n")

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
            "burst": burst
        })

    # Sort processes by Arrival Time (FCFS rule)
    processes.sort(key=lambda x: x["arrival"])

    current_time = 0
    total_waiting = 0
    total_turnaround = 0

    print("\n" + "-" * 75)
    print(f"{'Process':<10}{'Arrival':<12}{'Burst':<10}{'Start':<10}{'Completion':<12}{'Waiting':<10}{'Turnaround':<12}")
    print("-" * 75)

    for p in processes:
        # Start time is the maximum of current time and arrival time
        start_time = max(current_time, p["arrival"])
        completion_time = start_time + p["burst"]
        turnaround_time = completion_time - p["arrival"]
        waiting_time = turnaround_time - p["burst"]

        # Update totals
        total_waiting += waiting_time
        total_turnaround += turnaround_time

        # Print process details
        print(f"{p['pid']:<10}{p['arrival']:<12}{p['burst']:<10}{start_time:<10}{completion_time:<12}{waiting_time:<10}{turnaround_time:<12}")

        # Update current time
        current_time = completion_time

    # Calculate averages
    avg_waiting = total_waiting / n
    avg_turnaround = total_turnaround / n

    print("-" * 75)
    print(f"\nAverage Waiting Time     : {avg_waiting:.2f}")
    print(f"Average Turnaround Time  : {avg_turnaround:.2f}")
    print("-" * 75)


# Run the program
if __name__ == "__main__":
    fcfs_scheduling()