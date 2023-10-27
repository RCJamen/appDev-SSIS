# appDev-SSIS 
![Screenshot from 2023-10-20 08-56-20](https://github.com/RCJamen/appDev-SSIS/assets/57859978/94257749-01dd-43ce-af35-33114850fd3f)
A web-based Implementation of Student Information System with CRUDL Functionalities.

## Installation
1. Clone the repository on your Local Machine.

```bash
git clone git@github.com:RCJamen/appDev-SSIS.git
```
```bash
cd appDev-SSIS
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

4. Run this Schema Script for Database Configuration
```bash
python3 setup_database.py
```

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
