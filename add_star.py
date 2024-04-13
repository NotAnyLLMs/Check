import requests

def star_all_repos_of_user(username, token):
    """
    Stars all repositories of a GitHub user.

    Args:
        username (str): The username of the GitHub user.
        token (str): Your GitHub personal access token.

    Returns:
        bool: True if successful, False otherwise.
    """
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    url = f"https://api.github.com/users/{username}/repos"

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to retrieve repositories for user {username}. Status code: {response.status_code}")
        return False

    repos = response.json()

    for repo in repos:
        if not star_github_repo(username, repo['name'], token):
            return False

    print(f"All repositories of user {username} starred successfully.")
    return True

def star_github_repo(owner, repo, token):
    """
    Stars a GitHub repository.

    Args:
        owner (str): The owner of the repository.
        repo (str): The name of the repository.
        token (str): Your GitHub personal access token.

    Returns:
        bool: True if successful, False otherwise.
    """
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3.star+json"
    }
    url = f"https://api.github.com/user/starred/{owner}/{repo}"

    response = requests.put(url, headers=headers)

    if response.status_code == 204:
        print(f"Starred {owner}/{repo} successfully.")
        return True
    else:
        print(f"Failed to star {owner}/{repo}. Status code: {response.status_code}")
        return False

# Example usage:
username = "CRLannister"
github_token = "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"

star_all_repos_of_user(username, github_token)
