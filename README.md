# restAPI (Python + Flask)

A small example REST API using Python and Flask. This repository contains a minimal Flask app in `src/main.py` with a root endpoint and an Armstrong-number checker endpoint.

## Features
- GET `/` — returns a simple greeting ("Hello, World!").
- GET `/armstrong/<int:n>` — returns whether `n` is an Armstrong number as JSON.

## Requirements
- Python 3.8+ recommended. If you use Python 3.13, be aware some older package wheels may not support it; prefer 3.11 for maximum compatibility.
- Flask (install into the virtual environment used to run the app).

## Quick start (Windows, cmd.exe)

1. Open a cmd prompt and change to the project folder.

2. (Optional) Create and activate a virtual environment if you don't already have one:

```batch
python -m venv .venv
.venv\Scripts\activate.bat
```

3. Upgrade pip and install Flask:

```batch
python -m pip install --upgrade pip
python -m pip install flask
```

4. Run the app:

```batch
python src\main.py
```

Or using the Flask CLI:

```batch
set FLASK_APP=src.main
python -m flask run
```

By default the app runs on `http://127.0.0.1:5000`.

## Endpoints

- `GET /` — Returns a plain text greeting.
- `GET /armstrong/<int:n>` — Returns JSON with the properties:
	- `Number`: the queried number
	- `Armstrong`: true/false
	- `Server IP`: server address

Example response for an Armstrong number:

```json
{
	"Number": 153,
	"Armstrong": true,
	"Server IP": "127.0.0.1:5000"
}
```

## Example requests

Using curl (Windows 10+ has curl):

```batch
curl http://127.0.0.1:5000/
curl http://127.0.0.1:5000/armstrong/153
```

Using Python requests:

```python
import requests
print(requests.get('http://127.0.0.1:5000/').text)
print(requests.get('http://127.0.0.1:5000/armstrong/153').json())
```

## Troubleshooting

- ImportError / ModuleNotFoundError on `from flask import ...`:
	- Verify the Python interpreter used to run the app is the same one that has Flask installed.
	- Activate the virtualenv before running, or run with the venv Python explicitly: `path\to\venv\Scripts\python.exe src\main.py`.
	- Check where Flask is installed:

		```batch
		python -m pip show flask
		python -c "import flask,sys; print(flask.__file__, flask.__version__, sys.executable)"
		```

	- Look for accidental filename/package shadowing: make sure there isn't a `flask.py` file or a `flask/` folder in your project that could shadow the real package.
	- Paths containing unusual characters (for example `&` in the folder name) can sometimes cause issues in tools or when launching processes; if you run into mysterious import problems, try moving the project to a simple path like `C:\Projects\restAPI` and retest.

- Flask install fails on your Python version:
	- Use `py -3.11 -m venv .venv311` to create a 3.11 venv if you have 3.11 installed, then install Flask there.

## Development notes
- Main app file: `src/main.py`.
- If you change the entry point, update `FLASK_APP` accordingly.
