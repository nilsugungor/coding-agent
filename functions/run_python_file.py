import os
import subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file with optional command-line arguments.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The relative path of the Python file to execute.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="Optional list of command-line arguments to pass to the script.",
            ),
        },
        required=["file_path"],
    ),
)

def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file_abs = os.path.normpath(os.path.join(working_dir_abs, file_path))

        if os.path.commonpath([working_dir_abs, target_file_abs]) != working_dir_abs:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_file_abs):
            return f'Error: "{file_path}" does not exist'
        if not target_file_abs.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        try:
            command = ["python", target_file_abs]
            if args:
                command.extend(args)
            result = subprocess.run(
                    command,
                    cwd=working_dir_abs,
                    capture_output=True,
                    text=True,
                    timeout=30
                )
            output_parts = []

            if result.returncode != 0:
                output_parts.append(f"Process exited with code {result.returncode}")
            if not result.stdout and not result.stderr:
                output_parts.append("No output produced")
            else:
                if result.stdout:
                    output_parts.append(f"STDOUT:\n{result.stdout}")
                if result.stderr:
                    output_parts.append(f"STDERR:\n{result.stderr}")
    
            return "\n".join(output_parts)
        
        except subprocess.TimeoutExpired:
            return "Error: Process timed out after 30 seconds"


    except Exception as e:
        return f"Error: executing Python file: {e}"