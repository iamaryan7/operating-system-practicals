# Least Recently Used (LRU) Page Replacement Algorithm

def lru_page_replacement():
    print("===== Least Recently Used (LRU) Page Replacement Algorithm =====\n")

    # Input number of frames
    frames = int(input("Enter the number of frames: "))

    # Input reference string
    ref_string = list(map(int, input("Enter the reference string (space separated): ").split()))

    memory = []          # Current pages in memory
    page_faults = 0
    page_hits = 0
    recent = []          # To keep track of usage order (most recent at the end)

    print("\n" + "-" * 75)
    print(f"{'Step':<6}{'Page':<8}{'Memory Frames':<30}{'Status':<12}{'Faults'}")
    print("-" * 75)

    for i, page in enumerate(ref_string, 1):
        if page in memory:
            # Page Hit → Update recent usage
            status = "Hit"
            page_hits += 1
            recent.remove(page)
            recent.append(page)
        else:
            # Page Fault
            status = "Fault"
            page_faults += 1

            if len(memory) < frames:
                # Still empty frames available
                memory.append(page)
                recent.append(page)
            else:
                # Memory is full → Replace Least Recently Used page
                lru_page = recent.pop(0)   # Least recently used
                index = memory.index(lru_page)
                memory[index] = page
                recent.append(page)

        # Display current state of memory
        mem_display = memory + ["-"] * (frames - len(memory))
        print(f"{i:<6}{page:<8}{str(mem_display):<30}{status:<12}{page_faults}")

    # Final Results
    total_references = len(ref_string)
    hit_ratio = (page_hits / total_references) * 100
    fault_ratio = (page_faults / total_references) * 100

    print("-" * 75)
    print(f"\nTotal Page References : {total_references}")
    print(f"Total Page Faults     : {page_faults}")
    print(f"Total Page Hits       : {page_hits}")
    print(f"Hit Ratio             : {hit_ratio:.2f}%")
    print(f"Fault Ratio           : {fault_ratio:.2f}%")
    print("-" * 75)


# Run the program
if __name__ == "__main__":
    lru_page_replacement()