import sys # Used for exiting gracefully if needed

print("--- File Operations ---")
print("1. Write text to a file (write.txt)")
print("2. Read text from a file (read.txt)")
print("-----------------------")

choice = None # Initialize choice variable

# --- Get User Input ---
while choice not in [1, 2]:
    try:
        choice_str = input("Choose an option (1 or 2): ")
        choice = int(choice_str)
        if choice not in [1, 2]:
            print("Invalid choice. Please enter 1 or 2.")
    except ValueError:
        print("Invalid input. Please enter a number (1 or 2).")
    # Loop continues if input was invalid or not 1 or 2

# --- Perform Action Based on Choice ---

# Option 1: Write to file
if choice == 1:
    filename_to_write = "write.txt"
    try:
        # Get text from the user
        text_to_write = input(f"Enter the text you want to write to '{filename_to_write}':\n")

        # Use 'with' statement for safe file handling (automatically closes)
        # 'w' mode: Opens for writing. Creates the file if it doesn't exist,
        #           TRUNCATES (empties) the file if it does exist.
        # Use 'a' mode instead if you want to append to the end of the file.
        with open(filename_to_write, "w", encoding='utf-8') as file: # encoding='utf-8' is good practice
            file.write(text_to_write) # Write the user's text
            file.write("\n") # Optionally add a newline at the end
        print(f"\nSuccessfully wrote to '{filename_to_write}'.")

    except IOError as e:
        # Catch errors related to file operations (e.g., permissions)
        print(f"\nError: Could not write to file '{filename_to_write}'. Reason: {e}")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"\nAn unexpected error occurred: {e}")

# Option 2: Read from file
elif choice == 2:
    filename_to_read = "read.txt"
    try:
        # Use 'with' statement for safe file handling (automatically closes)
        # 'r' mode: Opens for reading (this is the default if mode is omitted)
        with open(filename_to_read, "r", encoding='utf-8') as file: # encoding='utf-8' is good practice
            print(f"\n--- Content of '{filename_to_read}' ---")
            content = file.read() # Read the entire content of the file
            if not content:
                 print("(File is empty or contains only whitespace)")
            else:
                 print(content)
            print("--- End of Content ---")

    except FileNotFoundError:
        # Specific error if the file doesn't exist
        print(f"\nError: The file '{filename_to_read}' was not found.")
        print("Tip: You might need to create it first or use option 1 to write to a file.")
    except IOError as e:
        # Catch other errors related to file operations (e.g., permissions)
        print(f"\nError: Could not read file '{filename_to_read}'. Reason: {e}")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"\nAn unexpected error occurred: {e}")

# This else should not be reachable due to the while loop validation,
# but included for logical completeness.
# else:
#    print("Invalid option selected.")

print("\nProgram finished.")