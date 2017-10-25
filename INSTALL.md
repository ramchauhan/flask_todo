git clone git@github.com:ramchauhan/flask_todo.git
cd flask_todo

# create virtualenv and install dependency
virtualenv -p /usr/lib/python3.5 env
source env/bin/activate
pip install -r requirements.txt

# run the application
python rest_api/app.py



