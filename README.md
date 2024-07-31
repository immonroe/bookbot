# Bookbot - The Text Analysis Tool

This is a simple text analysis tool written in Python. It reads a text file and generates a report with the following information:
- The total number of words.
- The most common word.
- The frequency of each character (in descending order).
- The frequency of punctuation marks (excluding numbers).

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Files](#files)
- [Contributing](#contributing)

## Installation

No special dependencies are required for this project, only Python 3.x. You can check if Python is installed by running:

```bash
python --version
```
## Usage

To use this tool, follow these steps:

Clone the repository:

```bash
git clone https://github.com/github-username/repo-name
cd repo-name
```
Run the script with the path to your text file as an argument:

```bash
python text_analysis.py path/to/your/textfile.txt
```
## Example

Here is an example of how to run the script and its output:

Command:

```bash
python text_analysis.py path/to/your/textfile.txt
```

Output
```sql
--- Begin report of your-textfile.txt ---
1024 words found in the document
The most common word is 'the' which was found 40 times.

Character frequency (descending order):
Character 'e' is found 300 times.
Character 't' is found 224 times.
...

Punctuation frequency:
',' : 20
'.' : 15
...

--- End of report ---
```

## Files

- `text_analysis.py`: The main script for text analysis.
- `test.py`: A script for testing the analysis tool with a predefined text (e.g., Frankenstein).

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

- Fork the repository.
- Create your feature branch (git checkout -b feature/AmazingFeature).
- Commit your changes (git commit -m 'Add some AmazingFeature').
- Push to the branch (git push origin feature/AmazingFeature).
- Open a pull request.