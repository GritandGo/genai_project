import os


def get_files_info(working_directory, directory="."):
    full_path = os.path.abspath(os.path.join(working_directory, directory))
    working_dir = os.path.abspath(working_directory)
    if not full_path.startswith(working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(full_path):
        return f'Error: "{full_path}" is not a directory'
    
    
    try:
        list_of_item_names = os.listdir(full_path)
        new_list = []
        for name in list_of_item_names:
            if name != "__pycache__":
                full_name = os.path.join(full_path, name)
                size = os.path.getsize(full_name)
                is_dir = os.path.isdir(full_name)
                formatted_string = f"- {name}: file_size={size} bytes, is_dir={is_dir}"
                new_list.append(formatted_string)
            

        return "\n".join(new_list)
    

    except OSError as e:
        return f"Error: An operating system error occurred: {e}"
    except Exception as e:
        return f"Error: An unexpected error occurred: {e}"


    
    

