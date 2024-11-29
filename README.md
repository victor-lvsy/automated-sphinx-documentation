# Automated Sphinx Documentation

Welcome to the Automated Sphinx Documentation repository! This project automates the creation of docstring-formatted comments within your Python code, using the OpenAI API to enhance clarity and comprehensiveness, making it easier to generate Sphinx-compatible documentation later.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Overview

This repository provides a tool to automatically add docstring-formatted comments to your Python code using the OpenAI API. These comments can then be utilized by Sphinx or similar documentation tools to generate professional documentation.

## Features

- Automatically generate docstring-style comments in Python code
- Utilizes OpenAI API to enhance comment generation
- Simple setup and execution
- Facilitates the creation of Sphinx-compatible documentation

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/automated-sphinx-documentation.git
   cd automated-sphinx-documentation
   ```

2. **Install Dependencies**
   Ensure you have Python and pip installed. Then, install the necessary packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up OpenAI API Key**
   Create a `.env` file in the root directory of your repository and add your OpenAI API key:
   ```plaintext
   OPENAI_API_KEY=your_openai_api_key_here
   ```

   This key allows the script to interact with the OpenAI API to generate enhanced comments.

## Usage

To add docstring comments to your Python code, first ensure your code contains placeholders where you want the comments to be generated. Execute the `main.py` script, specifying the directories for input and output.

1. **Prepare Your Source Code**
   Ensure that your input folder contains the Python source files you wish to enhance with docstring comments. Add `"""TODO"""` placeholders in your code where you want the automated comments to be generated.

2. **Run the Script**
   Execute the main script. You will be prompted to enter the source and destination directories:
   ```bash
   python main.py
   ```

   You will be asked:
   - "Enter code directory to be commented": Provide the path to the directory containing your source code.
   - "Where do you want the commented code directory to be? please give the path of the root folder": Provide the path where you want the processed code to be saved.

3. **Review Your Code**
   Upon completion, navigate to the output directory to review the source code that has been enhanced with docstring-formatted comments.

## Example

```bash
# Run main.py and follow the prompts
python main.py
```

This will process the Python files in your specified input directory, adding docstring comments in place of `"""TODO"""` placeholders, and saving a code of your code with comments in your specified output directory.

## Contributing

We welcome contributions to improve this project. Please fork the repository, create a branch for your feature or bug fix, and submit a pull request for review.

1. **Fork the Repository**
2. **Create a Branch**: `git checkout -b feature-name`
3. **Commit Your Changes**: `git commit -m 'Add new feature'`
4. **Push to Your Branch**: `git push origin feature-name`
5. **Submit a Pull Request**

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

Thank you for using Automated Sphinx Documentation. We hope it assists you in creating clear and comprehensive docstring comments for your projects! If you have any questions or require assistance, feel free to open an issue in this repository.