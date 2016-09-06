# Running the application

- Checkout code on /opt/pets-api on local computer
- Build the containers: ```docker-compose build```
- Copy settings.py.bak to settings.py and add 'mongodb' as MONGODB_HOST
- Start the application: ```docker-compose up```
- To start the application with pdb enabled: ```docker-compose run --rm --name petsapi_web_1 --service-ports web python3 manage.py runserver```

# To access mongodb
- Find the docker web container name and run: ```docker exec -it petsapi_web_1 mongo --host mongodb```

# To run tests
- Find the docker web container name and run: ```docker exec -it petsapi_web_1 python tests.py```
