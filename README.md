# symprosys-task

### Requirement
- Python >= 3.13
- PostgreSQL >= 14

### Steps to run the code
- Install UV package using `pip install uv`
- Initialize virtual environment and install all the dependencies using `uv sync`
- Update the required environment variables in `.env` file
- To update the latest database model, run `alembic upgrade head`
- To start the server, run `python start_app.py`
- To show the generated swagger doc, open http://localhost:8000/docs