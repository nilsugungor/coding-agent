import os
import sys
from google.genai import types

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import MAX_CHARS

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads the content of a specific file. Returns the text content (possibly truncated if too large).",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The relative path of the file to read, including the filename and extension.",
            ),
        },
        required=["file_path"]
    ),
)

def get_file_content(working_directory, file_path):

    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file_abs = os.path.normpath(os.path.join(working_dir_abs, file_path))

        if os.path.commonpath([working_dir_abs, target_file_abs]) != working_dir_abs:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_file_abs):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(target_file_abs, 'r', encoding='utf-8') as f:
            content = f.read(MAX_CHARS)
            if f.read(1):
                content +=f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

            return content
        
    except Exception as e:
        return f"Error: {str(e)}"