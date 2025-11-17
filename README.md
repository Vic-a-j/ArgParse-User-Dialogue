# 📝 ArgParse-User-Dialogue
This is a small script testing Argparse arguments and Dockerizing a basic python application. Within the container you should be able to run the script and log changes to user data into **"logs/dialogue.log"**.

# ❓ How to run:


### Docker

This is a dockerized **python-3.12** and can be ran with **Makefile** commands as follows:

1) _"make ps"_ -> ```docker-compose ps```

2) _"make build"_ -> ```docker-compose build```

3) _"make build-clean"_ -> ```docker-compose build-clean```

4) _"make exec"_ -> ```docker-compose exec server bash```

5) _"make up"_ -> ```docker-compose up```

6) _"make down"_ -> ```docker-compose down```


### Testing

Testing can be done inside of the container. Once it's spun up you can exec into it and test the script itself.

1) Make a build or new clean build.
2) Exec into the container.
3) Inside the container run commands: ```python argparse_dialogue.py --age [age] --name [name] --gender [male]```


### Usage

The script takes in 4 arguments - age, name, gender, and city. Given these it will ask the user to modify initially inserted attributes to the user object. Changes will be inserted into a log file under logs and will print out if any modifications were made.

```
usage: UserProcessor [-h] -a AGE -n NAME -g GENDER [-c CITY]

options:
  -h, --help            show this help message and exit
  -a AGE, --age AGE     (int) Age of the user.
  -n NAME, --name NAME  (str) Name of the user.
  -g GENDER, --gender GENDER
                        (str) Gender of the user.
  -c CITY, --city CITY  (str) City of the user.
```