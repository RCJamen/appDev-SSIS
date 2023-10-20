# appDev-SSIS 

A web-based Implementation of Student Information System with CRUDL Functionalities.

## Installation
1. Clone the repository on your Local Machine.

```bash
git clone git@github.com:RCJamen/appDev-SSIS.git
```

2. Install the requirements.
```bash
pip install -r requirements.txt
```

3. Create your dotenv and flaskenv file.
```bash
cp env.example .env
```
```bash
cp flaskenv.example .flaskenv
```
and modify .env and .flaskenv data for your own setup.

4. In your MySQL IDE, execute the schema.sql file located in appDev181/dbscript/

## Running Flask
1. Initiate the Virtual Environment in your Terminal.
```bash
pipenv shell
```
2. Run Flask Application
```bash
flask run
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
