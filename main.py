import argparse
from src.ordering_app import OrderingApp

DEFAULT_OUTPUT_FILE = "grocery_orders.txt"
DEFAULT_DEPARTMENT_DIR = "departments"

def parse_cl_args():
    """
    Parses command line arguments for the program.

    Returns:
        tuple: A tuple containing the department directory and output file path.
               The first element is the department directory (string).
               The second element is the output file path (string).
    """
    parser = argparse.ArgumentParser(
        description="Program to load departments and their inventories from JSON files, interactively accept a user order, and then write the receipt to a file."
    )

    parser.add_argument(
        "-d", "--directory",
        default=DEFAULT_DEPARTMENT_DIR,
        help="directory with department .json files (optional)")
    parser.add_argument(
        "-o", "--output",
        default=DEFAULT_OUTPUT_FILE,
        help="output file for storing receipts (optional)")

    args = parser.parse_args()
    return args.directory, args.output


def main():
    """
    Main entry point of the OrderingApp.

    This function creates an instance of the OrderingApp and starts its
    main application routine, which handles user interactions and order processing.
    """
    app = OrderingApp(*parse_cl_args()) # unpacking operator!
    app.application_routine()

if __name__ == "__main__":
    main()
