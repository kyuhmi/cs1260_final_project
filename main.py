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
        help="Directory with department .json files")
    parser.add_argument(
        "-o", "--output",
        default=DEFAULT_OUTPUT_FILE,
        help="Output receipt of program execution")

    args = parser.parse_args()
    department_dir = args.directory
    output_file = args.output

    return department_dir, output_file


def main():
    """
    Main entry point of the OrderingApp.

    This function creates an instance of the OrderingApp and starts its
    main application routine, which handles user interactions and order processing.
    """
    department_dir, output_file = parse_cl_args()
    app = OrderingApp(department_dir, output_file)
    app.application_routine()

if __name__ == "__main__":
    main()
