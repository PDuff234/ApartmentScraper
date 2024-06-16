
# README: Setting Up a Python Virtual Environment and Installing Packages

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Windows Instructions](#windows-instructions)
   - [Creating a Virtual Environment](#creating-a-virtual-environment-on-windows)
   - [Activating the Virtual Environment](#activating-the-virtual-environment-on-windows)
   - [Installing Packages](#installing-packages-on-windows)
   - [Running Python](#running-python-on-windows)
3. [Linux Instructions](#linux-instructions)
   - [Creating a Virtual Environment](#creating-a-virtual-environment-on-linux)
   - [Activating the Virtual Environment](#activating-the-virtual-environment-on-linux)
   - [Installing Packages](#installing-packages-on-linux)
   - [Running Python](#running-python-on-linux)
4. [Deactivating the Virtual Environment](#deactivating-the-virtual-environment)
5. [Additional Tips](#additional-tips)

## Prerequisites
- Python installed on your system (Python 3.6 or higher recommended).
- `pip` (Python's package installer) should be installed. It is typically included with Python.

## Windows Instructions

### Creating a Virtual Environment on Windows
1. Open Command Prompt or PowerShell.
2. Navigate to the project directory where you want to create the virtual environment.
3. Run the following command to create a virtual environment:

   ```sh
   python -m venv venv
   ```

   This will create a directory named `venv` in your project directory.

### Activating the Virtual Environment on Windows
1. To activate the virtual environment, run:

   ```sh
   .\venv\Scripts\activate
   ```

   You should see `(venv)` preceding your command prompt, indicating that the virtual environment is active.

### Installing Packages on Windows
1. With the virtual environment activated, you can now install packages using `pip`. For example, to install the `requests` package, run:

   ```sh
   pip install requests
   ```

2. You can also install multiple packages from a `requirements.txt` file:

   ```sh
   pip install -r requirements.txt
   ```

### Running Python on Windows
1. To run a Python script with the virtual environment active, simply use the `python` command:

   ```sh
   python script_name.py
   ```

## Linux Instructions

### Creating a Virtual Environment on Linux
1. Open a terminal.
2. Navigate to the project directory where you want to create the virtual environment.
3. Run the following command to create a virtual environment:

   ```sh
   python3 -m venv venv
   ```

   This will create a directory named `venv` in your project directory.

### Activating the Virtual Environment on Linux
1. To activate the virtual environment, run:

   ```sh
   source venv/bin/activate
   ```

   You should see `(venv)` preceding your command prompt, indicating that the virtual environment is active.

### Installing Packages on Linux
1. With the virtual environment activated, you can now install packages using `pip`. For example, to install the `requests` package, run:

   ```sh
   pip install requests
   ```

2. You can also install multiple packages from a `requirements.txt` file:

   ```sh
   pip install -r requirements.txt
   ```

### Running Python on Linux
1. To run a Python script with the virtual environment active, simply use the `python` command:

   ```sh
   python script_name.py
   ```

## Deactivating the Virtual Environment
1. To deactivate the virtual environment and return to the global Python environment, run:

   ```sh
   deactivate
   ```

## Additional Tips
- To check which packages are installed in your virtual environment, run:

  ```sh
  pip list
  ```

- To freeze the current environment's packages into a `requirements.txt` file, run:

  ```sh
  pip freeze > requirements.txt
  ```

- It's good practice to include the `venv` directory in your `.gitignore` file if you're using version control, to avoid committing it to your repository.
