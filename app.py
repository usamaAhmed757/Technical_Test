from flask_migrate import Migrate
from flask_migrate import MigrateCommand
from models.models import Contact,Emails
from flask_script import Manager
from settings import app_instance
from settings import db
from flask_restful import Api

from views.endpoints import CreateContact
from views.endpoints import DeleteContact
from views.endpoints import  ListAllContacts


migrate = Migrate(app_instance, db)
managers_script = Manager(app_instance)
managers_script.add_command('db', MigrateCommand)

api=Api(app_instance)
api.add_resource(CreateContact,'/create/contact')
api.add_resource(DeleteContact,'/delete/contact')
api.add_resource(ListAllContacts,'/list/all/contacts')

if __name__ == '__main__':
    app_instance.run()

