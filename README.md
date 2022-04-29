# _Cal_Chat_

## Setup

```bash
# create virtual environment
python3 -m venv venv
# enable virtual environment
source venv/bin/activate
# install dependencies
pip install -U pip wheel
pip install -r requirements.txt
# set up database
python3 ./manage.py migrate
# run server
python3 ./manage.py runserver
```
