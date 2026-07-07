# GitHire - GitHub Recruiter Assistant

GitHire is a Python-based application that helps recruiters quickly analyze a candidate's GitHub profile.

Instead of manually opening every repository, GitHire summarizes the most important information such as candidate details, programming languages, top repositories, repository quality, and recruiter notes.

---

## Features

- Fetch GitHub profile using GitHub REST API
- Display candidate summary
- Detect top programming languages
- Show top repositories based on stars
- Analyze repository health
- Generate recruiter-friendly notes
- Beautiful terminal report using Rich

---

## Tech Stack

- Python
- Requests
- Rich
- GitHub REST API

---

## Project Structure

```
GitHire/
│
├── main.py
├── github_api.py
├── analyzer.py
├── report.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/GitHire.git
```

Move into the project

```bash
cd GitHire
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python main.py
```

---

## Example Output

```
GitHire - GitHub Recruiter Assistant

Candidate Summary
------------------------------
Name: Sakshi Shah
Username: Sakshi-0077
Followers: 10
Following: 8
Public Repositories: 12

Top Languages
------------------------------
Python
JavaScript
SQL

Top Repositories
------------------------------
GitHire
KaamSetu
AI Workforce

Repository Health
------------------------------
Repositories with Description: 10
Repositories with Stars: 5

Recruiter Notes
------------------------------
✔ Good GitHub bio
✔ Uses multiple programming languages
✔ Good number of repositories
```

---

## Python Concepts Used

- Functions
- Modules
- Imports
- Lists
- Dictionaries
- Loops
- Conditions
- Counter
- Sorting
- Lambda Functions
- API Requests
- JSON
- Error Handling
- Rich Library

---

## Future Improvements

- Export report to PDF
- Export report to CSV
- Streamlit Web Interface
- README quality checker
- Repository activity analysis

---

## Author

Sakshi Shah