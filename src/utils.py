import os

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
