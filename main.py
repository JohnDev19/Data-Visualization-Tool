from ui import UserInterface
from visualizer import Visualizer
from data_handler import DataHandler

def main():
    ui = UserInterface()
    visualizer = Visualizer()
    data_handler = DataHandler()

    while True:
        choice = ui.display_main_menu()

        if choice == '6':
            ui.display_exit_message()
            break

        if choice in ['1', '2', '3', '4', '5']:
            data = data_handler.get_data(choice)
            if data:
                visualizer.create_visualization(choice, data)
            else:
                ui.display_error("Invalid data input. Please try again.")
        else:
            ui.display_error("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()