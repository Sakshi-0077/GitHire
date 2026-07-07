from collections import Counter

def analyze_candidate(profile, repos):
    if not profile:
        return None
    
    analysis = {}
    analysis["Name"] = profile.get("name", "Not Available")
    analysis["Username"] = profile.get("login")
    analysis["Bio"] = profile.get("bio", "No Bio")
    analysis["Followers"] = profile.get("followers")
    analysis["Following"] = profile.get("following")
    analysis["Public Repositories"] = profile.get("public_repos")
    analysis["Created"] = profile.get("created_at")[:10]
    return analysis

def get_top_languages(repos):
    languages = []
    for repo in repos:
        if repo["language"]:
            languages.append(repo["language"])
    return Counter(languages).most_common(5)

def get_top_repositories(repos):
    sorted_repos = sorted(
        repos,
        key=lambda repo: repo["stargazers_count"],
        reverse=True)
    top_repositories = []
    for repo in sorted_repos[:5]:
        top_repositories.append({
            "Repository": repo["name"],
            "Language": repo["language"] or "N/A",
            "Stars": repo["stargazers_count"],
            "Forks": repo["forks_count"],
            "Updated": repo["updated_at"][:10]})
    return top_repositories

def repository_health(repos):
    total = len(repos)
    description = 0
    stars = 0
    forks = 0
    for repo in repos:
        if repo["description"]:
            description += 1
        if repo["stargazers_count"] > 0:
            stars += 1
        if repo["forks_count"] > 0:
            forks += 1
    return {
        "Total Repositories": total,
        "Repositories with Description": description,
        "Repositories with Stars": stars,
        "Repositories with Forks": forks
    }

def recruiter_notes(profile, repos):
    notes = []
    if profile.get("bio"):
        notes.append("Good GitHub bio")
    else:
        notes.append("Add a GitHub bio")
    if len(repos) >= 5:
        notes.append("Good number of public repositories")
    else:
        notes.append("Build more public repositories")
    if len(get_top_languages(repos)) >= 3:
        notes.append("Uses multiple programming languages")
    else:
        notes.append("Try learning more technologies")
    return notes