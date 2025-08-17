import os


def write_file(working_directory, file_path, content):
    full_path = os.path.abspath(os.path.join(working_directory, file_path))
    working_dir = os.path.abspath(working_directory)

    if not full_path.startswith(working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    

    try: 
        if not os.path.exists(full_path):
            parent_dir_path = os.path.dirname(full_path)
            os.makedirs(parent_dir_path, exist_ok=True)
    
    
        with open(full_path, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        

    except OSError as e:
        return f"Error: An operating system error occurred: {e}"
    except Exception as e:
        return f"Error: An unexpected error occurred: {e}"
