To set up your local environment, ensure you have uv installed. 
You can install it with pip (Python's default package manager) => % pip install uv

Database:
This project uses Sqlite by default, but you can use MySQL by changing the database url following line in the mysql.py file:
engine = create_engine("sqlite:///printjobs.db") 

Running the project: 
--------------------

With uv (it replaces pip, piptools, poetry, and more):
Sync the dependencies in your toml file with uv.lock (as needed) => % uv sync
% uv run main.py

If manually activating virtualenv:
Activate the virtual environment => % source .venv/bin/activate
Run the app using uvicorn => % uvicorn main:app --host 0.0.0.0 --port 8000 --reload

You can view the API documentation and can exercise the endpoints here:  http://localhost:8000/doc 

