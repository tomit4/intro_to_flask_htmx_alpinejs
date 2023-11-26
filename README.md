### A Introduction To Flask, HTMX, AlpineJS (with SQLite)

This is a short introduction to Flask, HTMX, and AlpineJS (with SQLite to be used for data storage)

Follow this [basic introduction for getting started with Flask](https://flask.palletsprojects.com/en/2.2.x/quickstart/).

Follow this [introduction to using sqlite3 with Flask](https://www.digitalocean.com/community/tutorials/how-to-use-an-sqlite-database-in-a-flask-application).

Note the [official documentation for HTMX](https://htmx.org/docs).

And the [offical documentation for AlpineJS](https://alpinejs.dev/).

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

If a fresh install, to install from requirements.txt (while in venv):

```
pip install -r requirements.txt

```

**TODO**:

- [ ] Create GET, POST, PATCH, PUT, and DELETE Routes to html files for now.
- [ ] Eventually connect flask to sqlite.
- [ ] Create client in htmx, AlpineJS
- [ ] Have client influence jinja templating and return back to htmx
- [ ] Make Something with it
