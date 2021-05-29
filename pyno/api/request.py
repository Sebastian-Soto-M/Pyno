# curl 'https://api.notion.com/v1/pages' \
#   -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \
#   -H "Content-Type: application/json" \
#   -H "Notion-Version: 2021-05-13" \
#   --data '{
# 	"parent": { "database_id": "48f8fee9cd794180bc2fec0398253067" },
# 	"properties": {
# 		"Name": {
# 			"title": [
# 				{
# 					"text": {
# 						"content": "Tuscan Kale"
# 					}
# 				}
# 			]
# 		},
# 		"Description": {
# 			"rich_text": [
# 				{
# 					"text": {
# 						"content": "A dark green leafy vegetable"
# 					}
# 				}
# 			]
# 		},
# 		"Food group": {
# 			"select": {
# 				"name": "Vegetable"
# 			}
# 		},
# 		"Price": { "number": 2.5 }
# 	},
# 	"children": [
# 		{
# 			"object": "block",
# 			"type": "heading_2",
# 			"heading_2": {
# 				"text": [{ "type": "text", "text": { "content": "Lacinato kale" } }]
# 			}
# 		},
# 		{
# 			"object": "block",
# 			"type": "paragraph",
# 			"paragraph": {
# 				"text": [
# 					{
# 						"type": "text",
# 						"text": {
# 							"content": "Lacinato kale is a variety of kale with a long tradition in Italian cuisine, especially that of Tuscany. It is also known as Tuscan kale, Italian kale, dinosaur kale, kale, flat back kale, palm tree kale, or black Tuscan palm.",
# 							"link": { "url": "https://en.wikipedia.org/wiki/Lacinato_kale" }
# 						}
# 					}
# 				]
# 			}
# 		}
# 	]
# }'

from pydantic.main import BaseModel


class CreatePageRequest(BaseModel):
    parent = {"database_id": str}
    properties: dict
    children: list[dict]