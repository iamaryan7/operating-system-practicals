# Banker's Algorithm Implementation in Python
# Checks whether the system is in a Safe State and finds the Safe Sequence

def calculate_need(max_matrix, allocation, n, m):
    """Calculate Need matrix = Max - Allocation"""
    need = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            need[i][j] = max_matrix[i][j] - allocation[i][j]
    return need


def is_safe(processes, available, max_matrix, allocation, n, m):
    """
    Safety Algorithm of Banker's Algorithm
    Returns True if system is in safe state, along with the safe sequence
    """
    need = calculate_need(max_matrix, allocation, n, m)

    # Initialize
    work = available.copy()
    finish = [False] * n
    safe_sequence = []

    count = 0
    while count < n:
        found = False
        for i in range(n):
            if not finish[i]:
                # Check if Need[i] <= Work
                if all(need[i][j] <= work[j] for j in range(m)):
                    # Simulate allocation
                    for j in range(m):
                        work[j] += allocation[i][j]
                    finish[i] = True
                    safe_sequence.append(processes[i])
                    found = True
                    count += 1
                    break  # Restart from beginning after finding one

        if not found:
            break

    if count == n:
        return True, safe_sequence
    else:
        return False, []


def print_matrix(matrix, title, processes, resources):
    print(f"\n{title}:")
    print("     ", end="")
    for r in resources:
        print(f"{r:>5}", end="")
    print()
    for i, row in enumerate(matrix):
        print(f"{processes[i]:>4} ", end="")
        for val in row:
            print(f"{val:>5}", end="")
        print()


def bankers_algorithm():
    print("===== Banker's Algorithm =====\n")

    n = int(input("Enter number of processes: "))
    m = int(input("Enter number of resource types: "))

    processes = [f"P{i}" for i in range(n)]
    resources = [f"R{i}" for i in range(m)]

    # Input Allocation Matrix
    print("\nEnter Allocation Matrix:")
    allocation = []
    for i in range(n):
        row = list(map(int, input(f"Process {processes[i]}: ").split()))
        allocation.append(row)

    # Input Max Matrix
    print("\nEnter Max Matrix:")
    max_matrix = []
    for i in range(n):
        row = list(map(int, input(f"Process {processes[i]}: ").split()))
        max_matrix.append(row)

    # Input Available Resources
    print("\nEnter Available Resources:")
    available = list(map(int, input().split()))

    # Calculate and display Need Matrix
    need = calculate_need(max_matrix, allocation, n, m)

    print_matrix(allocation, "Allocation Matrix", processes, resources)
    print_matrix(max_matrix, "Max Matrix", processes, resources)
    print_matrix(need, "Need Matrix", processes, resources)

    print(f"\nAvailable Resources: {available}")

    # Check for Safe State
    safe, safe_sequence = is_safe(processes, available, max_matrix, allocation, n, m)

    print("\n" + "="*50)
    if safe:
        print("System is in SAFE state.")
        print("Safe Sequence:", " → ".join(safe_sequence))
    else:
        print("System is in UNSAFE state. Deadlock may occur.")
    print("="*50)


# Run the program
if __name__ == "__main__":
    bankers_algorithm()