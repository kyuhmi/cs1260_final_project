from src.ordering_app import OrderingApp
import os

BASE_DEPARTMENT_DIR = "departments"

def get_json_files_in_dir(directory_path: str):
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
    app = OrderingApp()
    app.load_departments(get_json_files_in_dir(BASE_DEPARTMENT_DIR))
    app.application_routine()

if __name__ == "__main__":
    main()