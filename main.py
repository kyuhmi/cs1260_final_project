from src.ordering_app import OrderingApp
import os

BASE_DEPARTMENT_DIR = "departments"  # base path for department json files

def get_json_files_in_dir(directory_path: str):
    """
    Retrieves a list of JSON files located within a specified directory.

    Args:
        directory_path (str): The path to the directory to search.

    Returns:
        list: A list of strings, where each string is the full path to a JSON file in the directory.
              Returns an empty list if the directory does not exist or if no JSON files are found.
    """
    json_files = []
    try:
        # Check if the directory exists
        if not os.path.isdir(directory_path):
            print(f"Directory not found: {directory_path}")
            return json_files

        # Get all files in the directory
        for filename in os.listdir(directory_path):
            if filename.lower().endswith('.json'): # is json
                # Create full path and add to list
                full_path = os.path.join(directory_path, filename)
                json_files.append(full_path)
    except Exception as e:
        print(f"Error accessing directory {directory_path}: {str(e)}")

    return json_files

def main():
    """
    Main function that initializes and runs the OrderingApp.

    It loads department data from JSON files located in the BASE_DEPARTMENT_DIR
    and then executes the application routine.
    """
    app = OrderingApp()
    app.load_departments(get_json_files_in_dir(BASE_DEPARTMENT_DIR))
    app.application_routine()

if __name__ == "__main__":
    main()
