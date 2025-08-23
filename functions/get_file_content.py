import os
from config import MAX_CHARS
from google.genai import types


def get_file_content(working_directory, file_path):
        full_path = os.path.abspath(os.path.join(working_directory, file_path))
        working_dir = os.path.abspath(working_directory)


        if not full_path.startswith(working_dir):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        

        if not os.path.isfile(full_path):
            return f'Error: File not found or is not a regular file: "{full_path}"'
        

        try:
            with open(full_path, "r") as f:
                file_content_string = f.read(MAX_CHARS)
                if len(file_content_string) >= MAX_CHARS:
                    return file_content_string + (f'[...File "{file_path}" truncated at {MAX_CHARS} characters]') 
                else:
                    return file_content_string
                
    
        except Exception as e:
            return f"Error: An unexpected error occurred: {e}"
        

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads and returns the content of a specified file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to read, relative to the working directory.",
            ),
        },
    ),
)

