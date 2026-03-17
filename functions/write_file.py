import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import MAX_CHARS
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes or overwrites a file with the specified content.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The relative path where the file should be written.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The text content to write into the file.",
            ),
        },
        required=["file_path", "content"],
    ),
)

def write_file(working_directory, file_path, content):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file_abs = os.path.normpath(os.path.join(working_dir_abs, file_path))

        if os.path.commonpath([working_dir_abs, target_file_abs]) != working_dir_abs:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        if os.path.isdir(target_file_abs):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        target_dir = os.path.dirname(target_file_abs)
        os.makedirs(target_dir, exist_ok=True)

        with open(target_file_abs, "w", encoding="utf-8") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        return f"Error: {str(e)}"