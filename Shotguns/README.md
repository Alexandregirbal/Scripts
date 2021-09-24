# Python repo to shotgun some stuff on the world wide web.

## Requirements

This project has been build with `python 3.8.10`, please check your version out before starting (`3.7+` should be fine).
Install `pip` and then install the required packages with the following command:

    pip install -r requirements.txt

You can also use a virtual environment (recommended).

## Setup

- Be sure to have a subscription active on Kamernet
- Save your favorite search and filters, it must be the first one to appear when you go to your saved searches (/alerts).
- Rename `default.env` to `.env` and update its content with your Kamernet credentials.
- Go in main.py and modify the `MESSAGE` variable to the one you want. Keep in mind that you can access the owner's name with the `{owner_name}` key word.
- Still in main.py modify `CITIES` to the only cities you want to send messages to.

## Run

Run it like any other pyton script.

    python3 ./src/main.py
