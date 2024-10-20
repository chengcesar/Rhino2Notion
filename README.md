# Rhino2Notion
 Rhino integration with Notion

![Logo](/img/Thumbnail.png)

# Post List to Notion via Grasshopper + Hops

This project provides a Python Flask application using Grasshopper Hops to post a list of items from Grasshopper to a Notion database. The items include Name, Color (converted from RGB to hex), Number, and Tag columns in the Notion database.

## Features
- Accepts lists of items (Name, Color, Number, and Tag) from Grasshopper via Hops.
- Converts RGB color values to hex for the Color column in Notion.
- Posts the data to a specified Notion database using the Notion API.
- Trigger-based: Data is only posted when the trigger input is set to `True`.

## Prerequisites

Make sure you have the following installed:
- [Python 3.x](https://www.python.org/downloads/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/installation/)
- [ghhops-server](https://github.com/mcneel/compute.rhino3d/tree/master/src/GhHopsServer)
- [requests](https://docs.python-requests.org/en/latest/)
- A [Notion API Integration](https://developers.notion.com/docs/getting-started) with access to a database

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
    ```

2. **Install the required Python packages:**:
You can install the required packages using pip:

```bash
pip install flask ghhops_server requests
```

3. **Configure Notion API::**:
- Replace the placeholder values NOTION_TOKEN and DATABASE_ID in the script with your Notion API token and the ID of your target Notion database.

## Usage

1. **Running the Flask App**:

  ```bash
  python app.py
  
  ```

This will start the Flask app on http://127.0.0.1:5000/, where Grasshopper Hops will send requests.

2. **Setting up Grasshopper Hops**:

In Grasshopper, set up the Hops component to connect to the Flask server. Use the Hops component to pass data to the Python app. The function post_to_notion accepts the following inputs:

In Grasshopper, set up the Hops component to connect to the Flask server. Use the Hops component to pass data to the Python app. The function post_to_notion accepts the following inputs:

- **Name**: A list of strings representing the names of items.
Color: A list of RGB values in the format "255,0,0".
Number: A list of numbers (as float).
Tag: A list of strings representing the tags to be assigned to items in Notion.
Trigger: A boolean value to trigger the post operation. The data is only sent to Notion if this is True.