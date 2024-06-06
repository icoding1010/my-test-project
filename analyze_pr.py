import requests
import os

class GitHubPR:
    def __init__(self, owner, repo, pr_number, token):
        self.owner = owner
        self.repo = repo
        self.pr_number = pr_number
        self.headers = {
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.v3+json'
        }
        self.base_url = f'https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}'

    def get_pr_details(self):
        url = self.base_url
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            pr_data = response.json()
            return {
                'number': pr_data['number'],
                'title': pr_data['title'],
                'body': pr_data['body']
            }
        else:
            return None

    def get_pr_files(self):
        url = f'{self.base_url}/files'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_pr_changes(self):
        url = self.base_url
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            pr_data = response.json()
            return {
                'additions': pr_data['additions'],
                'deletions': pr_data['deletions'],
                'changed_files': pr_data['changed_files']
            }
        else:
            return None

    def get_pr_reviews(self):
        url = f'{self.base_url}/reviews'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_pr_comments(self):
        url = f'{self.base_url}/comments'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None

def main():
    # repo_url = os.getenv("GITHUB_REPOSITORY")
    # pr_number = os.getenv("PR_NUMBER")
    # token = os.getenv("GITHUB_TOKEN")
    repo_url = https://github.com/icoding1010/my-test-project/
    pr_number = 1
    token = os.getenv("GITHUB_TOKEN")
    owner, repo = repo_url.split("/")[-2], repo_url.split("/")[-1]

    github_pr = GitHubPR(owner, repo, pr_number, token)
    
    pr_details = github_pr.get_pr_details()
    if pr_details:
        print(f"PR Number: {pr_details['number']}")
        print(f"Title: {pr_details['title']}")
        print(f"Body: {pr_details['body']}")
    else:
        print("Failed to fetch PR details.")
    
    pr_files = github_pr.get_pr_files()
    if pr_files:
        print("Files:")
        for file in pr_files:
            print(f"- {file['filename']} (Status: {file['status']})")
    else:
        print("Failed to fetch PR files.")
    
    pr_changes = github_pr.get_pr_changes()
    if pr_changes:
        print(f"Additions: {pr_changes['additions']}")
        print(f"Deletions: {pr_changes['deletions']}")
        print(f"Changed Files: {pr_changes['changed_files']}")
    else:
        print("Failed to fetch PR changes.")
    
    pr_reviews = github_pr.get_pr_reviews()
    if pr_reviews:
        print("Reviews:")
        for review in pr_reviews:
            print(f"- {review['user']['login']}: {review['state']} - {review['body']}")
    else:
        print("Failed to fetch PR reviews.")
    
    pr_comments = github_pr.get_pr_comments()
    if pr_comments:
        print("Comments:")
        for comment in pr_comments:
            print(f"- {comment['user']['login']}: {comment['body']}")
    else:
        print("Failed to fetch PR comments.")

if __name__ == "__main__":
    main()
