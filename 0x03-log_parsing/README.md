# README.md for 0x03. Log Parsing Project

## Project Overview

The **0x03. Log Parsing** project involves creating a Python script that reads log data from standard input (stdin), processes it, and computes various metrics based on the parsed log entries. This project focuses on real-time data stream processing, utilization of regular expressions for data validation, and the effective use of dictionaries for aggregation.

## Requirements

### Technical Requirements

- **Allowed Editors**: `vi`, `vim`, `emacs`
- **Operating System**: All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3).
- **File Format**: All files must end with a new line.
- **Shebang**: The first line of all files should be exactly:
  ```bash
  #!/usr/bin/python3
  ```
- **Executable**: All files must be executable.
- **PEP 8 Compliance**: Your code should follow PEP 8 style guidelines (version 1.7.x).
- **Length Testing**: The length of your files will be tested using `wc` (word count utility).

### Concepts to Understand

The following concepts are essential for completing this project:

1. **File I/O in Python**: Learn how to read from `sys.stdin` line by line.
2. **Signal Handling in Python**: Handle keyboard interruptions (CTRL + C) gracefully using signal handling.
3. **Data Processing**: 
   - Parsing strings to extract specific data points from log entries.
   - Aggregating data to compute summaries.
4. **Regular Expressions**: Validate the format of each log entry.
5. **Dictionaries in Python**: Use dictionaries to count the occurrences of specific status codes and accumulate file sizes.
6. **Exception Handling**: Properly handle exceptions that may arise during file reading and data processing.

### Additional Resources

- Python Official Documentation
- Regex101: A tool for testing and debugging regular expressions
- PEP 8 Style Guide: Python's guidelines for writing readable code

## Task Specification

### 0. Log Parsing (Mandatory)

Write a script named `log_parser.py` that performs the following:

1. Reads from `stdin` line by line.
2. Computes and prints metrics based on the log entries in the format:
   ```
   <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
   ```
   - If a line does not conform to the format, it should be skipped.
   
3. After every 10 lines or upon keyboard interruption (CTRL + C), the script should display the following statistics:
   - **Total file size**:
     ```
     File size: <total size>
     ```
     where `<total size>` is the sum of all previous `<file size>` entries.
   
   - **Number of lines by status code**:
     - Only consider status codes: 200, 301, 400, 401, 403, 404, 405, and 500.
     - If a status code does not appear or is not an integer, do not print anything for that status code.
     - Status codes should be printed in ascending order:
       ```
       <status code>: <number>
       ```

## Usage

To use the script, execute the following command in the terminal:

```bash
./log_parser.py < log_file.log
```

Replace `log_file.log` with the path to your log file or pipe data into the script. 

## Example Output

After processing every 10 lines or receiving a keyboard interrupt, the output may look like this (actual results will vary based on input):

```
File size: 12345
200: 3
401: 1
404: 2
```

## Authors

- Sholycul [http://github.com/Sholycul]


## Acknowledgements

Special thanks to the educational platforms and mentors that provided resources and guidance throughout this project. 

---

