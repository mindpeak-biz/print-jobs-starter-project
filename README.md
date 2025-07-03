To set up your local environment, ensure you have uv installed. 
You can install it with pip (Python's default package manager) => % pip3 install uv

Database:
This project uses Sqlite by default, but you can use MySQL by changing the value of DATABASE_URL in the .env file:

DATABASE_URL = "sqlite:///printjobs.db"

Note: You need to create a .env file since it is being excluded from being committed to git via the .gitignore file.


Running the project: 
--------------------

With uv (it replaces pip, piptools, poetry, and more):
% uv run main.py

Sync the dependencies in your toml file with uv.lock (as needed) => % uv sync

If manually activating virtualenv:
Activate the virtual environment => % source .venv/bin/activate

Run the app using uvicorn => % uvicorn main:app --host 0.0.0.0 --port 8000 --reload

You can view the API documentation and can exercise the endpoints here:  http://localhost:8000/doc 

