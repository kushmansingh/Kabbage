import os
from kabbage import app

port = int(os.environ.get('PORT', 5000))
app.run()