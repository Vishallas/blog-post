from dotenv import load_dotenv

from main import app

load_dotenv()
app.run(port=8000)
