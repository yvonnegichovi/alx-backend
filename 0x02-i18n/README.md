# 0x02. i18n

## Back-end

**Weight:** 1

**Project Timeline:**
- **Start:** Jul 2, 2024, 6:00 AM
- **End:** Jul 3, 2024, 6:00 AM
- **Checker Release:** Jul 2, 2024, 12:00 PM
- **Manual QA Review:** Request it when you are done with the project
- **Auto Review:** Will be launched at the deadline

## Resources
Read or watch:
- Flask-Babel
- Flask i18n tutorial
- pytz

## Learning Objectives
- Learn how to parametrize Flask templates to display different languages
- Learn how to infer the correct locale based on URL parameters, user settings, or request headers
- Learn how to localize timestamps

## Requirements
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` style (version 2.5)
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- All your `*.py` files should be executable
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions and methods should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)' and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining the purpose of the module, class, or method (the length of it will be verified)
- All your functions and coroutines must be type-annotated

## Tasks

### 0. Basic Flask app
Create a basic Flask app in `0-app.py`. Create a single `/` route and an `index.html` template that outputs “Welcome to Holberton” as the page title (`<title>`) and “Hello world” as the header (`<h1>`).

**Repo:**
- GitHub repository: `alx-backend`
- Directory: `0x02-i18n`
- File: `0-app.py`, `templates/0-index.html`

### 1. Basic Babel setup
Install the Babel Flask extension:
```bash
$ pip3 install flask_babel==2.0.0
```
Instantiate the Babel object in your app and store it in a module-level variable named `babel`. Create a `Config` class with a `LANGUAGES` attribute equal to `["en", "fr"]`. Set Babel’s default locale to `"en"` and timezone to `"UTC"`. Use this class as config for your Flask app.

**Repo:**
- GitHub repository: `alx-backend`
- Directory: `0x02-i18n`
- File: `1-app.py`, `templates/1-index.html`

### 2. Get locale from request
Create a `get_locale` function with the `babel.localeselector` decorator. Use `request.accept_languages` to determine the best match with your supported languages.

**Repo:**
- GitHub repository: `alx-backend`
- Directory: `0x02-i18n`
- File: `2-app.py`, `templates/2-index.html`

### 3. Parametrize templates
Use the `_` or `gettext` function to parametrize your templates. Use the message IDs `home_title` and `home_header`. Create a `babel.cfg` file containing:
```
[python: **.py]
[jinja2: **/templates/**.html]
extensions=jinja2.ext.autoescape,jinja2.ext.with_
```
Initialize your translations with:
```bash
$ pybabel extract -F babel.cfg -o messages.pot .
$ pybabel init -i messages.pot -d translations -l en
$ pybabel init -i messages.pot -d translations -l fr
```
Edit files `translations/[en|fr]/LC_MESSAGES/messages.po` to provide the correct value for each message ID for each language. Compile your dictionaries with:
```bash
$ pybabel compile -d translations
```
Reload the home page of your app and verify the correct messages show up.

**Repo:**
- GitHub repository: `alx-backend`
- Directory: `0x02-i18n`
- File: `3-app.py`, `babel.cfg`, `templates/3-index.html`, `translations/en/LC_MESSAGES/messages.po`, `translations/fr/LC_MESSAGES/messages.po`, `translations/en/LC_MESSAGES/messages.mo`, `translations/fr/LC_MESSAGES/messages.mo`

### 4. Force locale with URL parameter
Implement a way to force a particular locale by passing the `locale=fr` parameter to your app’s URLs. In your `get_locale` function, check if the incoming request contains a `locale` argument and return it if it is a supported locale. Otherwise, resort to the previous default behavior.

**Repo:**
- GitHub repository: `alx-backend`
- Directory: `0x02-i18n`
- File: `4-app.py`, `templates/4-index.html`

### 5. Mock logging in
Create a user login system by copying the following user table into `5-app.py`:
```python
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}
```
Define a `get_user` function that returns a user dictionary or `None` if the ID cannot be found or if `login_as` was not passed. Define a `before_request` function and use the `app.before_request` decorator to make it execute before all other functions. Use `get_user` to find a user if any, and set it as a global on `flask.g.user`. Display a welcome message in the HTML template if a user is logged in, otherwise display a default message.

**Repo:**
- GitHub repository: `alx-backend`
- Directory: `0x02-i18n`
- File: `5-app.py`, `templates/5-index.html`

### 6. Use user locale
Change your `get_locale` function to use a user’s preferred locale if it is supported. The order of priority should be:
1. Locale from URL parameters
2. Locale from user settings
3. Locale from request header
4. Default locale

**Repo:**
- GitHub repository: `alx-backend`
- Directory: `0x02-i18n`
- File: `6-app.py`, `templates/6-index.html`

### 7. Infer appropriate time zone
Define a `get_timezone` function and use the `babel.timezoneselector` decorator. The logic should be the same as `get_locale`. Validate that the timezone is valid using `pytz.timezone` and handle the `pytz.exceptions.UnknownTimeZoneError` exception.

**Repo:**
- GitHub repository: `alx-backend`
- Directory: `0x02-i18n`
- File: `7-app.py`, `templates/7-index.html`

### 8. Display the current time
Based on the inferred timezone, display the current time on the home page in the default format. Use the following translations:
```
msgid   English                         French
current_time_is   "The current time is %(current_time)s."   "Nous sommes le %(current_time)s."
```

**Repo:**
- GitHub repository: `alx-backend`
- Directory: `0x02-i18n`
- File: `app.py`, `templates/index.html`, `translations/en/LC_MESSAGES/messages.po`, `translations/fr/LC_MESSAGES/messages.po`
