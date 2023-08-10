import requests
import datetime

def get_page_info(*, notion_token, page_id):
    notion_headers = {
        "Notion-Version":"2022-06-28",
        "Content-Type":"application/json",
        "Authorization":f"Bearer {notion_token}",
    }
    notion_api_endpoint = f"https://api.notion.com/v1/pages/{page_id}"
    resp = requests.get(url=notion_api_endpoint, headers=notion_headers)
    data = resp.json()
    return data

def create_patch_note_page_of_task_if_patch_note_required(*, notion_token, database_id, patch_note_title, task_page_info):
    task_page_id = task_page_info["id"]
    notion_headers = {
        "Notion-Version":"2022-06-28",
        "Content-Type":"application/json",
        "Authorization":f"Bearer {notion_token}",
    }
    notion_api_endpoint = "https://api.notion.com/v1/pages"
    data = {
        "parent":{"database_id":database_id},
        "properties": {
            "title": { "title": [ { "type": "text", "text": { "content": f"{patch_note_title}" } } ] },
        },
        "children":[
            {
                "object":"block",
                "type":"bulleted_list_item",
                "bulleted_list_item":{
                    "rich_text":[
                        {
                            "type":"text",
                            "text": {
                                "content":"티켓 링크: "
                            },
                            "annotations":{
                                "bold":True,
                            }
                        },
                        {
                            "type":"mention",
                            "mention": {
                                "type":"page",
                                "page": {
                                    "id": task_page_id,
                                }
                            }
                        }
                    ]
                }
            }
        ]
    }
    resp = requests.post(url=notion_api_endpoint, headers=notion_headers, json=data)
    data = resp.json()
    print(data)
    return data["url"]