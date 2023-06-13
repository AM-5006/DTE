# Facebook Page Automation

This is a Flask web application that allows users to post messages on a Facebook page using their access token. The application provides both manual and automated methods for filling in the form.

## Table of Contents
    Installation
    Usage
    File Structure
    Contributing

### Installation
To run the Facebook Page Poster application, follow these steps:
1. Clone the repository to your local machine.
2. Install the required dependencies by running the following command: ```pip3 install -r requirements.txt```

### Usage
1. Manual Method:
* Make sure you have a Facebook access token with the necessary permissions to post on a page. You can obtain an access token from the Facebook Developer website.
* Run the Flask application by executing the following command in the project's root directory: ```python app.py```
* Access the application by opening a web browser and navigating to http://localhost:5000.
* Fill in the access token, page ID, and message fields in the form and submit it.
* If the access token and page ID are valid, the message will be posted on the specified Facebook page.
* The application will display a success message with the page ID and post ID of the created post.
* If there are any errors during the process, an error message will be displayed with the details.


2. Automated Method:
* Follow the steps of Manual Method.
* Modify the token.json file with your access token, page ID, and message.
* Run the automate.py script on seperate terminal using the following command: ```python automate.py```
* The script will open a Firefox browser and automatically fill in the form with the data from ```token.json```.
* If the access token and page ID are valid, the message will be posted on the specified Facebook page.
* The script will navigate back to the index page after the form submission.

### File Structure
The file structure of the project is as follows:
```
|-- app.py                    # Flask application script
|-- automate.py               # Script for automating Facebook page posts
|-- requirements.txt          # Required dependencies
|-- templates
|   |-- base.html             # Base HTML template
|   |-- error.html            # Error HTML template
|   |-- index.html            # Index HTML template
|   `-- success.html          # Success HTML template
`-- token.json                # JSON file for storing Facebook access token, page id and message
```

* `app.py`: This file contains the Flask application code, including the routes and functions for posting on Facebook and validating access tokens.
* `automate.py`: This script uses Selenium to automate filling in the form with data from token.json and submitting it.
* `requirements.txt`: This file lists the dependencies required by the application. You can install them using pip.
* `templates`: This directory contains the HTML templates used for rendering the web pages.
  * `base.html`: This is the base HTML template that provides the common structure for other templates.
  * `error.html`: This template is rendered when there is an error during the process, displaying the error message and a link to the Facebook Graph API Explorer.
  * `index.html`: This template is rendered as the index page, which displays the form for submitting the access token, page ID, and message.
  * `success.html`: This template is rendered when the message is successfully posted, displaying the page ID and post ID of the created post.
* `token.json`: This JSON file stores the Facebook access token, page ID, and default message for automated form filling.

### Contributing
Contributions to the Facebook Page Poster project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
