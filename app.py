from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy

# from flask_migrate import Migrate, MigrateCommand
# from flask_script import Manager

app = Flask(__name__, template_folder='templates')
app.config.from_object(Configuration)

db = SQLAlchemy(app)


# Из за путаницы с базой, в итоге пресодал её полностью,
# этот код пока закомментирован

# migrate = Migrate(app, db)
# manager = Manager(app)
# manager.add_command('db', MigrateCommand)


