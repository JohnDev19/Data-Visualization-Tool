class UserInterface:
    def display_main_menu(self):
        print("\nData Visualization Tool")
        print("1. Bar Chart")
        print("2. Line Chart")
        print("3. Scatter Plot")
        print("4. Pie Chart")
        print("5. Histogram")
        print("6. Exit")
        return input("Enter your choice (1-6): ")

    def display_exit_message(self):
        print("Thank you for using the Data Visualization Tool. Goodbye!")

    def display_error(self, message):
        print(f"Error: {message}")

    def get_file_input(self):
        file_type = input("Enter file type (csv/json): ").lower()
        if file_type not in ['csv', 'json']:
            print("Invalid file type. Please choose 'csv' or 'json'.")
            return None, None

        filename = input(f"Enter the {file_type.upper()} file name: ")
        return file_type, filename