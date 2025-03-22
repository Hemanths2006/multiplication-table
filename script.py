def generate_table():
    """Generates a multiplication table and saves it to a file."""
    try:
        # Get user input for the number
        number = int(input("Enter a number to generate its multiplication table: "))
        
        # Generate the multiplication table
        table_list = [f"{number} x {i} = {number * i}" for i in range(1, 11)]
        
        # Display the table
        print(f"\n🔢 Multiplication Table of {number}:\n")
        print("\n".join(table_list))
        
        # Save the table to a file
        file_name = f"{number}_multiplication_table.txt"
        with open(file_name, "w") as file:
            file.write("\n".join(table_list))
        
        print(f"\n✅ Multiplication table saved as '{file_name}'.\n")
    
    except ValueError:
        print("❌ Invalid input! Please enter a valid integer.")

def access_table():
    """Reads and displays a saved multiplication table."""
    try:
        # Get user input for the number
        number = int(input("Enter a number to fetch its multiplication table: "))
        file_name = f"{number}_multiplication_table.txt"
        
        # Read and display the table
        with open(file_name, "r") as file:
            table_content = file.read()
            print(f"\n📖 Multiplication Table of {number}:\n")
            print(table_content)
    
    except FileNotFoundError:
        print(f"❌ Table for {number} not found. Please generate it first.")
    except ValueError:
        print("❌ Invalid input! Please enter a valid integer.")

def main_menu():
    """Displays the main menu and handles user choices."""
    while True:
        try:
            # Display menu options
            print("\n🌟 Main Menu 🌟")
            print("1️⃣ Generate Multiplication Table")
            print("2️⃣ Show Multiplication Table")
            print("3️⃣ Exit")
            
            # Get user choice
            choice = int(input("➡️ Enter your choice (1, 2, or 3): "))
            
            # Handle user choice
            if choice == 1:
                generate_table()
            elif choice == 2:
                access_table()
            elif choice == 3:
                print("👋 Exiting... Have a great day!")
                break
            else:
                print("❌ Invalid option. Please choose 1, 2, or 3.")
        
        except ValueError:
            print("❌ Invalid input! Please enter a number.")

# Run the program
if __name__ == "__main__":
    main_menu()
