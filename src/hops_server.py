import json
import requests
from flask import Flask
import ghhops_server as hs

# Initialize Flask and Hops
app = Flask(__name__)
hops = hs.Hops(app)


# Hops function to accept multiple strings from Grasshopper, and a trigger input
@hops.component(
    "/post_to_notion",
    name="Post List to Notion",
    inputs=[
        hs.HopsString("Name", "name", "Name item in the list",hs.HopsParamAccess.LIST),
        hs.HopsString("Color", "color", "Color column in Notion",hs.HopsParamAccess.LIST),
        hs.HopsBoolean("Trigger", "Trigger", "If True, post data to Notion",hs.HopsParamAccess.ITEM)
    ],
    outputs=[hs.HopsString("Result", "Result", "Result of the post operation")]
)
def post_list_to_notion(name, color, trigger):
    """
    This function posts each item to a specified column in a Notion database if the trigger is True.
    """
    data_list = name
    
    # Convert rgb-to-hex
    def rgb_to_hex(rgb):
        return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

    print(trigger)
    # Check if the trigger is set to True
    if not trigger:
        return "Trigger is False. No data posted to Notion."

    # Notion API details
    NOTION_TOKEN = {YOUR API KEY}
    DATABASE_ID = {YOUR DATABASE  ID}

    # Define the headers for the Notion API request
    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }



        # Prepare the data in the Notion format
    rows = []
    for item in range(len(data_list)):

        # Convert comma-separated RGB string to a tuple and then to hex
        rgb_values = [int(value) for value in color[item].split(',')]
        hex_color = rgb_to_hex(rgb_values)

        # Add each item as a new row in the specified column
        row_data = {
            "parent": {"database_id": DATABASE_ID},
            "properties": {
                "Name": {
                    "title": [
                        {
                            "text": {
                                "content": str(name[item])
                            }
                        }
                    ]
                },
                "Color": {
                    "rich_text": [
                        {
                         "type": "equation",
                            "equation": {
                                "expression": f"\\color{{#000}}\\colorbox{{{hex_color}}}{{\\textsf{{This is some text}}}}"  # LaTeX equation
                            },
                            "annotations": {
                                "code": True, # Treat as LaTeX code
                                "bold": False,
                                "underline": False

                            }
                        }
                    ]
                },
                
            }
        }
        rows.append(row_data)

    # Post each row to the Notion database
    results = []
    for row in rows:
        response = requests.post("https://api.notion.com/v1/pages", headers=headers, data=json.dumps(row))
        if response.status_code == 200:
            results.append(f"Success: {item}")
        else:
            results.append(f"Failed to post {item}. Error: {response.text}")

    return "\n".join(results)


# Start the Flask app
if __name__ == "__main__":
    app.run()
