from rich.console import Console
from rich.table import Table
console = Console()

def print_header():
    console.print("\nGitHire - GitHub Recruiter Assistant")
    console.print("=" * 50)

def display_candidate_summary(candidate):
    table = Table(title="Candidate Summary")
    table.add_column("Field", style="cyan")
    table.add_column("Value", style="green")
    for key, value in candidate.items():
        table.add_row(key, str(value))
    console.print(table)

def display_languages(languages):
    table = Table(title="Top Languages")
    table.add_column("Language", style="cyan")
    table.add_column("Repositories", style="green")
    for language, count in languages:
        table.add_row(language, str(count))
    console.print(table)

def display_top_repositories(repositories):
    table = Table(title="Top Repositories")
    table.add_column("Repository", style="cyan")
    table.add_column("Language")
    table.add_column("Stars")
    table.add_column("Forks")
    table.add_column("Updated")
    for repo in repositories:
        table.add_row(
            repo["Repository"],
            repo["Language"],
            str(repo["Stars"]),
            str(repo["Forks"]),
            repo["Updated"])
    console.print(table)

def display_repository_health(health):
    table = Table(title="Repository Health")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green")
    for key, value in health.items():
        table.add_row(key, str(value))
    console.print(table)

def display_recruiter_notes(notes):
    console.print("\n[bold yellow]Recruiter Notes[/bold yellow]\n")
    for note in notes:
        console.print(f"• {note}")