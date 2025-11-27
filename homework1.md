# Building a TODO application in Django.

## Basic requirements

The app should be able to do the following:

* Create, edit and delete TODOs
* Assign due dates
* Mark TODOs as resolved

You will only need Python to get started (we also recommend that you use `uv`). We'll write the app using Django.

## Installing uv

In [homework1](homework1) folder, doo the initial setup for uv:

* create and activate a virtualenv (`python -m venv .venv && source .venv/bin/activate`)
* install uv (`pip install uv`)
* run `uv init`

After that, you can add dependencies via `uv add <package>` and run your project with `uv exec <cmd>`.

##  Installing Django

`uv add Django`

## Initial flow to create the app

* Scaffolded the Django project with `django-admin startproject todo .`.
* Created the `todos` app via `python manage.py startapp todos` and registered it in `todo/settings.py`.
* Implemented the `Todo` model with title, description, due date, resolved flag, and timestamp fields plus a default ordering.
* Added `TodoForm`, wired it into create/edit generic views, and provided a toggle view for marking tasks resolved.
* Registered the model with the admin, added the app URLs via `todo/urls.py`, and defined CRUD routes in `todos/urls.py`.
* Created simple templates for listing tasks, rendering the form, and confirming deletes so the app is navigable.
