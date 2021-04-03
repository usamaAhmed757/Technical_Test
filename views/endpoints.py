from flask_restful import Resource
from flask_restful import reqparse

from constants.constant import BLANK_ERROR_MSG
from models.models import Contact, Emails
from settings import db


class CreateContact(Resource):
    parser = reqparse.RequestParser(bundle_errors=True)
    parser.add_argument('user_name',
                        type=str,
                        required=True,
                        help=BLANK_ERROR_MSG)
    parser.add_argument('first_name',
                        type=str,
                        required=True,
                        help=BLANK_ERROR_MSG)
    parser.add_argument('last_name',
                        type=str,
                        required=True,
                        help=BLANK_ERROR_MSG)
    parser.add_argument('phone_number',
                        type=int,
                        required=True,
                        help=BLANK_ERROR_MSG)


    def post(self):
        data = CreateContact.parser.parse_args()
        user_name = data.get('user_name')
        first_name=data.get('first_name')
        last_name=data.get('last_name')
        phone_number= data.get("phone_number")
        try:
            contact=db.session.query(Contact).filter(Contact.user_name==user_name).first()
            if contact:
                return dict(message="Contact with the user_name already exist")
            new_contact=Contact(user_name=user_name,first_name=first_name,last_name=last_name,phone_number=phone_number)
            db.session.add(new_contact)
            db.session.commit()
            return dict(message="Contact has been Created Successfully",user_name=user_name,first_name=first_name,last_name=last_name,
                        phone_number=phone_number ),201
        except Exception as error:
            return dict(message=str(error), success=False), 400
class DeleteContact(Resource):
    parser = reqparse.RequestParser(bundle_errors=True)
    parser.add_argument('contact_id',
                        type=int,
                        required=True,
                        help=BLANK_ERROR_MSG)

    def delete(self):
        data = DeleteContact.parser.parse_args()
        contact_id=data.get("contact_id")
        try:
            db.session.query(Emails).filter(Emails.contact_id ==contact_id).delete(synchronize_session=False)
            db.session.query(Contact).filter(Contact.id == contact_id).delete(synchronize_session=False)
            db.session.commit()
            return dict(message="The contact is deleted successfully"),201
        except Exception as error:
            return dict(message=str(error), success=False), 400
class ListAllContacts(Resource):
    def get(self):
        try:
            contacts=Contact.query.all()
            contact_list=[]
            for contact in contacts:
                contact_list.append({"user_name":contact.user_name,"first_name":contact.first_name,"last_name":contact.last_name,
                                    "phone_number":contact.phone_number})
            return dict(all_contacts=contact_list)
        except Exception as error:
            return dict(message=str(error), success=False), 400












