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
                        type=str,
                        required=True,
                        help=BLANK_ERROR_MSG)
    parser.add_argument('email_id',
                        type=str,
                        required=True,
                        help=BLANK_ERROR_MSG)

    def post(self):
        data = CreateContact.parser.parse_args()
        user_name = data.get('user_name')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        phone_number = data.get("phone_number")
        email_id = data.get("email_id")
        try:
            contact = db.session.query(Contact).filter(Contact.user_name == user_name).first()
            email = db.session.query(Emails).filter(Emails.email_id == email_id).first()
            if contact:
                new_email = Emails(email_id=email_id, contact_id=contact.id)
                db.session.add(new_email)
                db.session.commit()
                return dict(user_name=contact.user_name,first_name=contact.first_name,last_name=contact.last_name,phone_number=
                            contact.phone_number,email_id=new_email.email_id)


            new_contact = Contact(user_name=user_name, first_name=first_name, last_name=last_name,
                                  phone_number=phone_number)

            db.session.add(new_contact)
            db.session.commit()

            new_email = Emails(email_id=email_id, contact_id=new_contact.id)
            db.session.add(new_email)
            db.session.commit()
            if contact:
                new_email = Emails(email_id=email_id, contact_id=contact.id)
                db.session.add(new_email)
                db.session.commit()

            return dict(message="Contact has been Created Successfully", user_name=user_name, first_name=first_name,
                        last_name=last_name,
                        phone_number=phone_number, email_id=email_id), 200




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
        contact_id = data.get("contact_id")
        try:
            db.session.query(Emails).filter(Emails.contact_id == contact_id).delete(synchronize_session=False)
            db.session.query(Contact).filter(Contact.id == contact_id).delete(synchronize_session=False)
            db.session.commit()
            return dict(message="The contact is deleted successfully"), 201
        except Exception as error:
            return dict(message=str(error), success=False), 400


class ListAllContacts(Resource):
    def get(self):
        try:
            contacts = Contact.query.all()
            emails=Emails.query.all()

            contact_list = []
            emails_list=[]
            for contact,email in zip(contacts,emails):
                contact_list.append(
                    {"user_name": contact.user_name, "first_name": contact.first_name, "last_name": contact.last_name,
                     "phone_number": contact.phone_number})
                emails_list.append({"emaild_id":email.email_id,"contact_id":email.contact_id})
            return dict(all_contacts=contact_list,all_emails=emails_list),200
        except Exception as error:
            return dict(message=str(error), success=False), 400
class UpdateContacts(Resource):
    parser = reqparse.RequestParser(bundle_errors=True)
    parser.add_argument('new_user_name',
                        type=str,
                        required=True,
                        help=BLANK_ERROR_MSG)
    parser.add_argument('new_first_name',
                        type=str,
                        required=True,
                        help=BLANK_ERROR_MSG)
    parser.add_argument('new_last_name',
                        type=str,
                        required=True,
                        help=BLANK_ERROR_MSG)
    parser.add_argument('new_phone_number',
                        type=str,
                        required=True,
                        help=BLANK_ERROR_MSG)
    parser.add_argument('new_email_id',
                        type=str,
                        required=True,
                        help=BLANK_ERROR_MSG)
    parser.add_argument('old_email_id',
                        type=str,
                        required=True,
                        help=BLANK_ERROR_MSG)
    parser.add_argument('contact_id',
                        type=int,
                        required=True,
                        help=BLANK_ERROR_MSG)
    def put(self):
        data = UpdateContacts.parser.parse_args()

        new_user_name = data.get('new_user_name')
        new_first_name = data.get('new_first_name')
        new_last_name = data.get('new_last_name')
        new_phone_number = data.get("new_phone_number")
        new_email_id = data.get("new_email_id")
        old_email_id=data.get("old_email_id")
        contact_id = data.get("contact_id")
        try:
            db.session.query(Contact).filter(Contact.id==contact_id).update({Contact.user_name:new_user_name,Contact.first_name:new_first_name,Contact.last_name:new_last_name,Contact.phone_number:new_phone_number },synchronize_session=False)




            db.session.commit()

            db.session.query(Emails).filter(Emails.contact_id==contact_id).filter(Emails.email_id==old_email_id).update({Emails.email_id:new_email_id},synchronize_session=False)
            db.session.commit()
            return dict(user_name=new_user_name,first_name=new_first_name,last_name=new_last_name,phone_number=new_phone_number,email_id=new_email_id)
        except Exception as error:
            return dict(message=str(error), success=False), 400
class FindByUserName(Resource):
    parser = reqparse.RequestParser(bundle_errors=True)
    parser.add_argument('user_name',
                        type=str,
                        required=True,
                        help=BLANK_ERROR_MSG)
    def get(self):
        data=FindByUserName.parser.parse_args()
        user_name=data.get("user_name")
        try:
            contact=Contact.find_by_user_name(user_name=user_name)
            return dict(user_name=contact.user_name,first_name=contact.first_name,last_name=contact.last_name)
        except Exception as error:
            return dict(message=str(error), success=False), 400













