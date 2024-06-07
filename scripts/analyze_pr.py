import requests
import json
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

    def get_pr_overview(self):
        url = self.base_url
        print(f"in pr overview, url:{url}")
        response = requests.get(url, headers=self.headers)
        print(f"in pr overview, url:{url}, response:{response}")
        if response.status_code == 200:
            pr_data = response.json()
            return {
                'number': pr_data['number'],
                'title': pr_data['title'],
                'body': pr_data['body']
            }
        else:
            return None
    
    def get_pr_details(self):
        print("in pr details")
        url = f'{self.base_url}/{self.pr_number}'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None
        
    def get_pr_files(self):
        print("in files")
        url = f'{self.base_url}/files'
        response = requests.get(url, headers=self.headers)
        print(f"in files, url:{url}, response:{response}")
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
        print("in reviews")
        url = f'{self.base_url}/reviews'
        response = requests.get(url, headers=self.headers)
        print(f"in reviews, url:{url}, response:{response}")
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
        
    def get_pr_info(self):
        """
        Fetches and returns a dictionary containing all available information about the pull request,
        including overview, files, changes, reviews, and comments.
        """
        pr_info = {}

        # PR Overview
        pr_overview = self.get_pr_overview()
        if pr_overview:
            pr_info['overview'] = pr_overview
        else:
            pr_info['overview'] = None

        pr_details = self.get_pr_details()
        if pr_details:
            pr_info['pr_details'] = pr_details
        else:
            pr_info['pr_details'] = None

        # # PR Files
        # pr_files = self.get_pr_files()
        # if pr_files:
        #     pr_info['files'] = pr_files
        # else:
        #     pr_info['files'] = None

        # # PR Changes
        # pr_changes = self.get_pr_changes()
        # if pr_changes:
        #     pr_info['changes'] = pr_changes
        # else:
        #     pr_info['changes'] = None

        # # PR Reviews
        # pr_reviews = self.get_pr_reviews()
        # if pr_reviews:
        #     pr_info['reviews'] = pr_reviews
        # else:
        #     pr_info['reviews'] = None

        # # PR Comments
        # pr_comments = self.get_pr_comments()
        # if pr_comments:
        #     pr_info['comments'] = pr_comments
        # else:
        #     pr_info['comments'] = None

        return pr_info

    def save_pr_info(pr_data, filename):
        """
        Saves the provided PR information dictionary (`pr_data`)
        """
        with open(filename, 'w') as outfile:
            json.dump(pr_data, outfile, indent=4)

def save_swe_json(swe_json_data, filename):
    """
    Saves the SWE args data given to swe-agent as json file
    """
    with open(filename, 'w') as outfile:
        json.dump(swe_json_data, outfile, indent=4)

def main():
    # repo_url = os.getenv("GITHUB_REPOSITORY")
    pr_number = os.getenv("PR_NUMBER")
    token = os.getenv("GITHUB_TOKEN")
    repo_url = "icoding1010/my-test-project"
    # pr_number = 1
    # token = my_token
    owner, repo = repo_url.split("/")[-2], repo_url.split("/")[-1]
    base_commit = os.getenv("BASE_COMMIT")
    version = os.getenv("VERSION")
    
    github_pr = GitHubPR(owner, repo, pr_number, token)
    pr_data = github_pr.get_pr_info()
    
    if pr_data:
        # github_pr.save_pr_info(pr_data, "pr_info.json")
        # print("PR information saved as pr_info.json")
        swe_json = [{
            "problem_statement": pr_data,
            "instance_id": "SWE-agent__test-repo-i1",
            "problem_statement_source": "online",
            "repo": "https://github.com/icoding1010/my-test-project/",
            "repo_type": "github",
            "base_commit": base_commit,
            "version": version,
        }]
        print(swe_json)
        swe_json_filename = "swe_json_data.json"
        save_swe_json(swe_json, swe_json_filename)

    else:
        print("Failed to fetch PR information.")

if __name__ == "__main__":
    main()
