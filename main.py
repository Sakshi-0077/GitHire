from github_api import get_profile, get_repositories
from analyzer import analyze_candidate, get_top_languages, get_top_repositories, repository_health, recruiter_notes
from report import print_header, display_candidate_summary, display_languages, display_top_repositories, display_repository_health, display_recruiter_notes

def main():
    print_header()
    username = input("Enter GitHub Username: ").strip()
    print("\nFetching GitHub profile...\n")
    profile = get_profile(username)
    if profile is None:
        print("User not found!")
        return
    
    repos = get_repositories(username)
    candidate = analyze_candidate(profile)
    languages = get_top_languages(repos)
    top_repos = get_top_repositories(repos)
    health = repository_health(repos)
    notes = recruiter_notes(profile, repos)

    display_candidate_summary(candidate)
    display_languages(languages)
    display_top_repositories(top_repos)
    display_repository_health(health)
    display_recruiter_notes(notes)

if __name__ == "__main__":
    main()