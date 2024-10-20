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

