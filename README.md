Running the project: 
--------------------

With uv:
% uv run main.py

If manually activating virtualenv:
Activate the virtual environment => % source .venv/bin/activate
Run the app using uvicorn => % uvicorn main:app --host 0.0.0.0 --port 8000 --reload