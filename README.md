# Shorter distance between words
The goal of this project is to allow the user to find the shortest distance between words given a text file.
This was built using python and docker to ease the project execution.

## How to launch it
1. We need to define the file to which we are going to read its contents. To do so, we use environment variables that are configurable on our docker launch. To run the project as uploaded execute:
`docker build -t shorter-distance --build-arg text_file=words.txt .`
where the build-arg text_file is the name of the file that will be read.
2. Execute `docker run -i shorter-distance python main.py -h` to read the help.
3. Execute `docker run -i zageno python main.py {first_word} {final_word}` where the first and final words are the ones that we are looking up.

## How to run the tests
The tests can be launched with the help of pytest. All of the project dependencies are easily installed with the help of pipenv.
1. Install Pipenv if you don't have it already ([download here](https://pipenv.readthedocs.io/en/latest/)): $`pip install --user pipenv`
2. then run `pipenv install` on the project folder. This will create a virtual environment with all of the dependencies inside.
3. Run `PIPENV_DOTENV_LOCATION=.env.test pipenv run pytest -q tests.py` in order to override the .env file and use the testing configuration.

## Additional notes
If you want to run the project locally please create the `.env` file by copying the `.env.dist` available in the project. This will setup the env variable `TEXT_FILE` to load the right file searching for the words. To run the project please be sure to use `pipenv run python main.py {first_word} {final_word}` to load the .env contents.
