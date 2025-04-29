from src.ordering_app import OrderingApp

def main():
    """
    Main entry point of the OrderingApp.

    This function creates an instance of the OrderingApp and starts its
    main application routine, which handles user interactions and order processing.
    """
    app = OrderingApp()
    app.application_routine()

if __name__ == "__main__":
    main()
