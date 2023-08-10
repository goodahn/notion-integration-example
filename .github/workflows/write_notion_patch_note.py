import requests
import sys
import os

import github_helper
import notion_helper

if __name__ == "__main__":
    GITHUB_TOKEN = sys.argv[1]
    REPO_OWNER = os.getenv("REPO_OWNER")
    REPO_NAME = os.getenv("REPO_NAME")
    PR_NUMBER = sys.argv[3]
    COMMIT_ID = sys.argv[4]

    NOTION_TOKEN = sys.argv[2]
    NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

    notion_task_page_id = github_helper.get_task_notion_page_id_from_pr(
        github_token=GITHUB_TOKEN,
        repo_owner=REPO_OWNER,
        repo_name=REPO_NAME,
        pr_number=PR_NUMBER,
    )
    
    notion_task_page_info = notion_helper.get_page_info(notion_token=NOTION_TOKEN, page_id=notion_task_page_id)
    print(notion_task_page_info)
    notion_patch_note_url = notion_helper.create_patch_note_page_of_task_if_patch_note_required(
        notion_token=NOTION_TOKEN,
        database_id=NOTION_DATABASE_ID,
        patch_note_title=COMMIT_ID,
        task_page_info=notion_task_page_info,
    )
    print(notion_patch_note_url)