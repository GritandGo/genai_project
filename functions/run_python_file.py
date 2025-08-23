import os
import subprocess
from google.genai import types


def run_python_file(working_directory, file_path, args=None):
    if args is None:
        args = []


    full_path = os.path.abspath(os.path.join(working_directory, file_path))
    working_dir = os.path.abspath(working_directory)


    if not full_path.startswith(working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(full_path):
        return f'Error: File "{file_path}" not found.'
    if not full_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    
    command = ["python", full_path] + args


    try:
        result = subprocess.run(
            command,
            timeout=30,
            capture_output=True,
            text=True,
            cwd=working_dir,
    )
    except Exception as e:
        return f"Error: executing Python file: {e}"


    output = []
    if result.stdout:
        output.append(f"STDOUT:\n{result.stdout}")
    if result.stderr:
        output.append(f"STDERR:\n{result.stderr}")
    if result.returncode != 0:
        output.append(f"Process exited with code {result.returncode}")
    return "\n".join(output) if output else "No output produced."
    
            
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file and returns the output or error messages.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory.",
            ),
        },
    ),
)
