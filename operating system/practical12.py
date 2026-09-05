# Sequential (Contiguous) File Allocation Method

def sequential_file_allocation():
    print("===== Sequential (Contiguous) File Allocation Method =====\n")

    # Input total number of disk blocks
    total_blocks = int(input("Enter total number of disk blocks: "))
    disk = [0] * total_blocks          # 0 means free, otherwise stores File ID

    files = {}                         # To store file information

    while True:
        print("\n--------- Menu ---------")
        print("1. Create File")
        print("2. Delete File")
        print("3. Show Disk Status")
        print("4. Show File Allocation Table")
        print("5. Exit")
        print("------------------------")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            # Create a new file
            file_name = input("Enter File Name: ")
            if file_name in files:
                print("Error: File already exists!")
                continue

            start_block = int(input("Enter Starting Block: "))
            length = int(input("Enter Length (Number of Blocks): "))

            # Validation
            if start_block < 0 or start_block >= total_blocks:
                print("Error: Invalid starting block!")
                continue
            if start_block + length > total_blocks:
                print("Error: Not enough blocks available from starting position!")
                continue

            # Check if the required contiguous blocks are free
            is_free = True
            for i in range(start_block, start_block + length):
                if disk[i] != 0:
                    is_free = False
                    break

            if is_free:
                # Allocate the blocks
                for i in range(start_block, start_block + length):
                    disk[i] = file_name
                files[file_name] = {"start": start_block, "length": length}
                print(f"File '{file_name}' allocated successfully from block {start_block} to {start_block + length - 1}")
            else:
                print("Error: Contiguous free blocks not available!")

        elif choice == 2:
            # Delete a file
            file_name = input("Enter File Name to Delete: ")
            if file_name not in files:
                print("Error: File not found!")
                continue

            start = files[file_name]["start"]
            length = files[file_name]["length"]

            # Free the blocks
            for i in range(start, start + length):
                disk[i] = 0

            del files[file_name]
            print(f"File '{file_name}' deleted successfully.")

        elif choice == 3:
            # Show Disk Status
            print("\nDisk Status (Block → Content):")
            print("-" * 40)
            for i in range(total_blocks):
                content = disk[i] if disk[i] != 0 else "Free"
                print(f"Block {i:3d} → {content}")
            print("-" * 40)

        elif choice == 4:
            # Show File Allocation Table
            if not files:
                print("No files allocated yet.")
            else:
                print("\nFile Allocation Table:")
                print("-" * 45)
                print(f"{'File Name':<15}{'Start Block':<15}{'Length'}")
                print("-" * 45)
                for name, info in files.items():
                    print(f"{name:<15}{info['start']:<15}{info['length']}")
                print("-" * 45)

        elif choice == 5:
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please try again.")


# Run the program
if __name__ == "__main__":
    sequential_file_allocation()