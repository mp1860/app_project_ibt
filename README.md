# AppProject

Full stack web application built in Python with the [Flask](https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/flask.md) framework. 

## Overview

1. Crypto Overview 
    - what is cryptocurrency
    - why is it popular
    - different kinds of crypto
2. Crypto History 
    - timeline of historical Crypto events
    - chart of cryptocurrency market cap
3. Crypto Dashboard
    - see latest price of popular cryptocurrencies
4. Favorite Coin [spreadsheet](https://docs.google.com/spreadsheets/d/1KZvj7sb9L3xke4eH4ky3vg5xX0vcNTZxGCfJyR_xrvI)
    - share your favorite coin with the developers

## Setup (if desire to run locally)

This is only necessary if you desire to run the app locally, otherwise you can utilize our hosted server located at https://ultimate-crypto-app.onrender.com/

### Prerequisites

To run this app, you'll need to have Anaconda, Python, and Pip installed (specifically Python version 3.10+).

### Installation

Make a copy of the template repository from GitHub. Clone your copy of the repo onto your local computer, for example onto your Desktop.

Navigate to the local repository from the command line, for example:

```sh
cd ~/Desktop/app-project_ibt
```

> NOTE: it is important to navigate to the root directory before running any of the commands below.


Create new virtual environment (first time only):

```sh
conda create -n dashboard-env python=3.10
```

Activate the virtual environment (first time, or whenever you return to the project):

```sh
conda activate dashboard-env
```

> NOTE: it is important to activate the virual environment before running any of the commands below.

Install package dependencies (first time only):

```sh
pip install -r requirements.txt
```

> NOTE: if you see an error after running this package installation command, make sure you have first navigated to the root directory of your local repository, where the "requirements.txt" file exists.

### Services

You'll also need to obtain a "premium" access [AlphaVantage API Key](https://www.alphavantage.co/support/#api-key) and set it as the `ALPHAVANTAGE_API_KEY` environment variable (see configuration section below).


## Configuration

### .env Setup
Create a new file called ".env" in the root directory of your local repository, and place inside contents like the following:

```sh
# this is the ".env" file...

# telling flask where our app is defined:
FLASK_APP="web_app"

# for interfacing with the AlphaVantage API:
ALPHAVANTAGE_API_KEY="..."
GOOGLE_SHEETS_DOCUMENT_ID="..."
```

> NOTE: when you push your repository to GitHub, the ".env" file does not show up - this is desired behavior, as designated by the ".gitignore" file, to prevent our secret credentials stored in the ".env" file from being uploaded or exposed on GitHub.


### Google APIs Setup

To interface with Google APIs, the app will need access to a local "service account" credentials file.

#### Enabling APIs

From the [Google APIs Dashboard](https://console.cloud.google.com/apis/dashboard) page, search for and "enable" any API(s) of interest, in this case the Google Sheets API.

#### Service Account Credentials

From the [Google API Credentials](https://console.cloud.google.com/apis/credentials) page, create a new service account as necessary.

For the chosen service account, create new JSON credentials file as necessary from the "Keys" menu, then download the resulting JSON file.

Move the service account credentials JSON file into the root directory of this repo, and rename it as "ibt-proj-81e46f86a85f.json".

> NOTE: the "ibt-proj-81e46f86a85f.json" file has been ignored from version control via the ".gitignore" file, to avoid seeing / exposing these credentials on GitHub

## Usage

Run the web application (then view in the browser at localhost:5000):

```sh
flask run
```
## Setup (if desire to host server on Render)

Follow this guide if you would like to deploy your host your application on a free server provided by the Render platform.

References:
  + https://render.com/docs/deploy-flask

### Render Setup

Login to [Render](https://dashboard.render.com) and visit the dashboard.

Create a New "Web Service". Choose your own repository by specifying its public URL.

Specify start command:

```
gunicorn "web_app:create_app()"
```

Choose instance type of "free".

Under the "Advanced" options, set the following environment variables (specifying your own API Key values):


```sh
ALPHAVANTAGE_API_KEY="..."
GOOGLE_SHEETS_DOCUMENT_ID="..."
service_file="ibt-proj-81e46f86a85f.json"
```

Also set two [secret configuration files]. One called "ibt-proj-81e46f86a85f.json", and paste the contents from your google service account credentials file (as referenced above). Another called ".env", and paste the contents from your .env file (as referenced above). 


Finally, click to "Create" the web service.


### Render Deploys

Whenever you push new code to the desingated branch in your GitHub repository, it will trigger a new deployment to update your hosted site.

You can also trigger builds manually.

