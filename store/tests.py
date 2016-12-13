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

        # import fixtures
        fixtures(self.db_name, "store", "store/fixtures/stores.json")

    def tearDown(self):
        db = _get_db()
        db.client.drop_database(db)

    def app_dict(self):
        return json.dumps(dict(
                app_id="pet_client",
                app_secret="pet_secret"
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

    def test_create_store(self):
        # get app up and running
        self.create_api_app()
        self.generate_access_token()

        print(Store.objects.all().count())
