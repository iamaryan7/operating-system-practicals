# FIFO Page Replacement Algorithm

from collections import deque

def fifo_page_replacement():
    print("===== FIFO Page Replacement Algorithm =====\n")

    # Input number of frames
    frames = int(input("Enter the number of frames: "))

    # Input reference string
    ref_string = list(map(int, input("Enter the reference string (space separated): ").split()))

    # Initialize
    memory = deque(maxlen=frames)   # Using deque to easily implement FIFO
    page_faults = 0
    page_hits = 0

    print("\n" + "-" * 70)
    print(f"{'Step':<6}{'Page':<8}{'Memory Frames':<30}{'Status':<12}{'Faults'}")
    print("-" * 70)

    for i, page in enumerate(ref_string, 1):
        if page in memory:
            # Page Hit
            status = "Hit"
            page_hits += 1
        else:
            # Page Fault
            status = "Fault"
            page_faults += 1
            if len(memory) == frames:
                memory.popleft()   # Remove the oldest page (FIFO)
            memory.append(page)

        # Display current state of memory
        mem_display = list(memory) + ["-"] * (frames - len(memory))
        print(f"{i:<6}{page:<8}{str(mem_display):<30}{status:<12}{page_faults}")

    # Final Results
    total_references = len(ref_string)
    hit_ratio = (page_hits / total_references) * 100
    fault_ratio = (page_faults / total_references) * 100

    print("-" * 70)
    print(f"\nTotal Page References : {total_references}")
    print(f"Total Page Faults     : {page_faults}")
    print(f"Total Page Hits       : {page_hits}")
    print(f"Hit Ratio             : {hit_ratio:.2f}%")
    print(f"Fault Ratio           : {fault_ratio:.2f}%")
    print("-" * 70)


# Run the program
if __name__ == "__main__":
    fifo_page_replacement()