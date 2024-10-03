### Small Description:

A Python command-line utility for batch renaming files with a specified format, applying a custom prefix, and renaming them in sequence.


# batch-file-renaming-cli

A Python command-line utility for batch renaming files with a specified format. The script allows you to rename files by applying a custom prefix and renaming them sequentially.

## Features

- **Choose File Type**: Specify the file format (e.g., `.txt`, `.log`, etc.) you want to work with.
- **Batch Rename with Prefix**: Rename all files of the selected format with a specified prefix and number them sequentially.
- **Flexible File Type**: Option to change the file format during the renaming process.

## How It Works

1. **Specify File Format**: Start by entering the file format (e.g., `.txt` or `.log`) to choose the files you want to rename.
2. **Enter Prefix**: The script prompts you to enter a prefix, which will be applied to all the files and will rename them sequentially.
3. **Change File Format Option**: You can switch the file format during the process to rename different types of files without restarting.
4. **Completion**: After renaming, the task is completed, and the renamed files are displayed.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Sjschhabra/batch-file-renaming-cli.git
   ```

2. Navigate to the project directory:
   ```bash
   cd batch-file-renaming-cli
   ```

3. Ensure Python 3.x is installed on your system.

## Usage

1. Run the script:
   ```bash
   python hell.py
   ```

2. Follow the prompts:
   - **Step 1**: Enter the file format (e.g., `.txt`).
   - **Step 2**: Enter the prefix to apply to all files.
   - **Step 3**: Optionally, change the file format and continue renaming files.

### Example

```bash
$ python hell.py

1. Enter file format you want to work with (enter ._filetype_): .txt
Files Present in the directory are: ['file1.txt', 'file2.txt']

2. Enter prefix you want for all the ".txt" files: report
Files renamed to: ['report-1.txt', 'report-2.txt']

----Task Completed----
```
