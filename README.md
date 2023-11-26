### A Introduction To Flask, HTMX, AlpineJS (with SQLite)

This is a short introduction to Flask, HTMX, and AlpineJS (with SQLite to be used for data storage)

Follow this [basic introduction](https://flask.palletsprojects.com/en/2.2.x/quickstart/).

To start new python virtual environment (uses [virtualenvwrapper on Artix](https://wiki.archlinux.org/title/Python/Virtual_environment)):

```
mkvirtualenv envname (flask)
```

And then activate that venv:

```
workon envname (flask)
```

To Install new packages (while in venv):

```
pip install <package-name>
```

And to end venv:

```
deactivate
```

To start, simply (while in venv):

```
python index.py
```

To install from requirements.txt (while in venv):

```
pip install -r requirements.txt

```

**TODO**:

- [ ] Create GET, POST, PATCH, PUT, and DELETE Routes to html files for now.
- [ ] Eventually connect flask to sqlite.
- [ ] Create client in htmx, AlpineJS
- [ ] Have client influence jinja templating and return back to htmx
- [ ] Make Something with it
