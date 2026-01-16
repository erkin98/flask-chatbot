import os
from chatbot import create_app
app = create_app()
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get("FLASK_DEBUG") == "1" or os.environ.get("FLASK_ENV") == "development"
    app.run(host="0.0.0.0", port=port, debug=debug)