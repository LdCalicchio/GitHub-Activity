# GitHub Activity CLI

## Description
A simple command-line interface (CLI) tool designed to fetch and display recent activity for a specified GitHub user directly in the terminal.
This project was created as part of the Python Developer roadmap. You can find the original project idea here: https://roadmap.sh/projects/github-user-activity

## Features
- Fetch recent public events for any GitHub user.
- Display activity details such as PushEvents, IssuesEvents, and WatchEvents.
- Clean and readable output format.

## Project Structure
```text
github_activity_cli/
├── src/           # Source code for the CLI
├── .gitigonre     # gitignore file
├── pyproject.toml # File responsable for the project configuration
└── README.md      # Project documentation

src/
└── github_activity/          
    ├── api.py     
    ├── cli.py 
    └── functions.py 
```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/username/github_activity_cli.git
   ```
2. Navigate to the project directory and install the required dependencies.

## Usage
Run the tool by passing the GitHub username as an argument:

```bash
# Example command
./github-activity <username>
```
