### A Introduction To Flask, HTMX, AlpineJS (with SQLite)

This is a short introduction to Flask, HTMX, and AlpineJS (with SQLite to be used for data storage)

Follow this [basic introduction for getting started with Flask](https://flask.palletsprojects.com/en/2.2.x/quickstart/).

Follow this [introduction to using sqlite3 with Flask](https://www.digitalocean.com/community/tutorials/how-to-use-an-sqlite-database-in-a-flask-application).

Note the [official documentation for HTMX](https://htmx.org/docs).

And the [offical documentation for AlpineJS](https://alpinejs.dev/).

Of Interest also might be [this link on using jinja templates with AlpinJS](https://gigi.nullneuron.net/gigilabs/minimal-web-application-with-flask-and-alpinejs/).

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

Whenever installing a new dependency, make sure to update your requirements.txt
file (while in venv):

```
rm requirements.txt && pip freeze > requirements.txt
```

If a fresh install, to install from requirements.txt (while in venv):

```
pip install -r requirements.txt

```

**TODO**:

- [ ] Create GET, POST, PATCH, PUT, and DELETE Routes to html files for now.
- [x] Eventually connect flask to sqlite.
- [ ] Consider dropping AlpineJS in favor of using Flask's native Jinja
      templating engine. There are some strange caveats to utilizing AlpineJS in this
      manner (e.g. Jinja SQL macros instead of using python's json library).
- [ ] Have client influence jinja templating and return back to htmx
- [ ] Make Something with it
