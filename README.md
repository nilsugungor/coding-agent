# Coding Agent

A CLI coding agent powered by Google Gemini that can read, write, and execute Python files in the working directory.

## Requirements

- Python 3.11+
- Gemini API key

## Setup

```bash
uv sync
echo "GEMINI_API_KEY=your_key_here" > .env
```

## Usage

```bash
python main.py "your prompt here"
python main.py "your prompt here" --verbose
```

## Tools

The agent has access to four tools:

- `get_files_info` — list files in the working directory
- `get_file_content` — read a file's contents
- `write_file` — write or overwrite a file
- `run_python_file` — execute a Python file and return output

## Limitations

- Only operates on Python files within the working directory
- Max 20 agentic iterations per run
