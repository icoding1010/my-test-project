# scripts/analyze_pr.py
import os
import requests

def get_pull_request_details(repo, pr_number, token):
    url = f"https://api.github.com/repos/{repo}/pulls/{pr_number}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(url, headers=headers)
    return response.json()

def analyze_pull_request(pr_data):
    # Implement your analysis logic here
    # This is just a placeholder example
    return f"PR Analysis Report for PR #{pr_data['number']}: \n- Title: {pr_data['title']} \n- Author: {pr_data['user']['login']}"

def post_comment(repo, pr_number, token, comment):
    url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "body": comment
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

if __name__ == "__main__":
    repo = os.getenv("GITHUB_REPOSITORY")
    pr_number = os.getenv("PR_NUMBER")
    token = os.getenv("GITHUB_TOKEN")

    pr_data = get_pull_request_details(repo, pr_number, token)
    report = analyze_pull_request(pr_data)
    post_comment(repo, pr_number, token, report)
