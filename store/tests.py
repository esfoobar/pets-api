from application import create_app as create_app_base
from mongoengine.connection import _get_db
import unittest
import json

from settings import MONGODB_HOST, MONGODB_DB
from store.models import Store
from application import fixtures

class StoreTest(unittest.TestCase):

    def create_app(self):
        self.db_name = 'pets-api-test'
        return create_app_base(
            MONGODB_SETTINGS={'DB': self.db_name,
                'HOST': MONGODB_HOST},
            TESTING=True,
            WTF_CSRF_ENABLED=False,
            SECRET_KEY = 'mySecret!',
        )

    def setUp(self):
        self.app_factory = self.create_app()
        self.app = self.app_factory.test_client()

    def tearDown(self):
        db = _get_db()
        db.client.drop_database(db)

    def app_dict(self):
        return json.dumps(dict(
                app_id="pet_client",
                app_secret="pet_secret"
                ))

    def store_dict(self):
        return json.dumps(dict(
            neighborhood="Bay Ridge",
            street_address="1112 Bay Ridge Avenue",
            city="Brooklyn",
            state="NY",
            zip="11209",
            phone="718-222-2445"
            ))

    def create_api_app(self):
        # create our app
        rv = self.app.post('/apps/',
            data=self.app_dict(),
            content_type='application/json')

    def generate_access_token(self):
        # generate an access token
        rv = self.app.post('/apps/access_token/',
            data=self.app_dict(),
            content_type='application/json')
        self.token = json.loads(rv.data.decode('utf-8')).get('token')

    def headers(self):
        return {
            'X-APP-ID': 'pet_client',
            'X-APP-TOKEN': self.token
            }

    def test_stores(self):
        # get app up and running
        self.create_api_app()
        self.generate_access_token()

        # create a store
        rv = self.app.post('/stores/',
            headers=self.headers(),
            data=self.store_dict(),
            content_type='application/json')
        assert rv.status_code == 201

    def test_pagination(self):
        # import fixtures
        fixtures(self.db_name, "store", "store/fixtures/stores.json")
