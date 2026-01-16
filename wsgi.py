from chatbot import create_app

# Used by production servers (e.g. gunicorn) as `wsgi:app`.
app = create_app()