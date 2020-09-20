# MyCart Cli App

### follow these commands to Install the App:

```
* change the schema/config.py accorgingly 

$ pip install -r requirements.txt
$ python schema/create_schema.py ./schema/mycartkb.sql
$ python myCart.py

```

### Building the Docker container (Beta)

```
$ docker build -t MyCart .
```
### Running the Docker container locally

* Note: Enter the appropriate environment variables.

```
$ docker run --network=host -d  \
-e POSTGRES_USERNAME=<POSTGRES_USERNAME> \
-e POSTGRES_PASSWORD=<POSTGRES_PASSWORD> \
-e POSTGRES_HOST_NAME=<POSTGRES_HOST_NAME> \
-e POSTGRES_PORT='5432' \
-e POSTGRES_DB_NAME=<POSTGRES_DB_NAME> 

MyCart
```

### Testing the app

```
python tests.py
```
