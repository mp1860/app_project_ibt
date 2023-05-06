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
4. Favorite Coin
    - share your favorite coin with the developers

## Setup (if desire to run locally)

This is only necessary if you desire to run the app locally, otherwise you can utilize our hosted server located at 

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

> NOTE: the "google-credentials.json" file has been ignored from version control via the ".gitignore" file, to avoid seeing / exposing these credentials on GitHub

## Usage

Run the web application (then view in the browser at localhost:5000):

```sh
flask run
```
