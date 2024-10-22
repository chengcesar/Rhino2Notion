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

3. **Configure Notion API**:
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
- **Color**: A list of RGB values in the format "255,0,0".
- **Number**: A list of numbers (as float).
- **Tag**: A list of strings representing the tags to be assigned to items in Notion.
- **Trigger** : A boolean value to trigger the post operation. The data is only sent to Notion if this is True.

3. **Example Grasshopper Setup**:

In Grasshopper, your setup might look something like this:

- Connect a **Panel** to the Hops inputs for "Name", "Color", "Number", and "Tag".
- Set up a **Boolean Toggle** for the "Trigger" input.
- Once the "Trigger" is set to *True*, the function will post the data to the Notion database.

4. **Example Grasshopper Setup**:

- **Name**: ["Item 1", "Item 2"]
- **Color**: ["255,0,0", "0,255,0"] (Red and Green)
- **Number**: [100, 200]
- **Tag**: ["Category 01", "Category 2"]
- **Trigger**: True

When you trigger the operation, the Flask app will post this data to your Notion database.

5. **Example Notion Database Structure**:

Your Notion database should have the following columns:

- **Name**: A title field.
- **Color**: A rich text field that accepts LaTeX equations to render colors.
- **Number**: A number field.
- **Tag**: A select field with predefined tags.

The Flask app will convert the RGB colors into hex format and render them as a colored LaTeX expression in the Notion database.

6. **Data Formatting and RGB to Hex Conversion**:

The script includes a helper function that converts RGB colors to hex format before posting to the Notion database. The RGB values are passed from Grasshopper as strings (e.g., "255,0,0" for red), and the function converts these values to hex (e.g., "#FF0000").

7. **Handling Trigger Input**:

The operation to post data to Notion only proceeds if the Trigger input is set to True. If the trigger is False, the script does not perform any actions. This allows for controlled posting from Grasshopper when needed.

8. **Notion API Details**:

Make sure you have set up the Notion Integration with a valid API key and have access to your Notion database’s ID. Replace the placeholders in the Python script with your actual NOTION_TOKEN and DATABASE_ID.

9. **Posting to Notion**:

Once the trigger is activated, the data is sent to the Notion API with the following structure:

10. **Example Output**:

![img](/img/Landscape_template1920x1080-Shapes2_1.gif)

## USE CASES:

![img](/img/GIF-r2n.gif)

- **Architectural Design Documentation:** Interactive documents allow architects and stakeholders to review 3D models and design elements in real-time, enabling them to filter geometry by attributes such as material, area, and volume. Stakeholders can visualize specific parts of a design or compare alternative solutions instantly, with the ability to sort and filter data directly in Notion.
- **Product Development & Iteration:** Design teams working on product development can use interactive documents to track and store parametric data like dimensions, materials, and part counts. As the product evolves, the document dynamically updates, allowing teams to create custom charts that analyze changes over time and ensure the product meets design specifications.
- **Urban Planning Data Collaboration:** For city planners and urban designers, interactive documents centralize vast amounts of data, such as zoning information, building heights, or environmental impacts. Through Notion's filtering and sorting capabilities, teams can create dashboards that highlight key metrics for each city zone, making it easier to communicate data-driven decisions to public officials or community stakeholders.
- **Client & Stakeholder Reporting:** Instead of delivering static reports, firms can provide clients with interactive documents that give them the power to sort, filter, and even edit information on their projects. For example, clients can review cost breakdowns, material selections, and project timelines in a fully interactive format, fostering greater transparency and collaboration.