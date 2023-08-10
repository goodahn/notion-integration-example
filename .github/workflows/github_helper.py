import requests

def _get_comments_of_pull_request(github_token, repo_owner, repo_name, pr_number):
    github_headers = {
        "Accept":"application/vnd.github+json",
        "Authorization":f"Bearer {github_token}",
        "X-GitHub-Api-Version":"2022-11-28",
    }

    github_api_endpoint = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues/{pr_number}/comments"
    resp = requests.get(url=github_api_endpoint, headers=github_headers)
    data = resp.json()
    return data

def get_task_notion_page_id_from_pr(*, github_token, repo_owner, repo_name, pr_number):
    data = _get_comments_of_pull_request(github_token, repo_owner, repo_name, pr_number)

    comment = {}
    for _comment in data:
        if _comment["user"]["login"] == "notion-workspace[bot]":
            comment = _comment
            break

    notion_url = comment["body"].split("]")[-1].replace("(", "").replace(")","")
    print(notion_url)
    page_id = notion_url.split("/")[-1].split("?")[0].split("-")[-1]
    return page_id