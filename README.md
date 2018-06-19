# KungFuSchool
A student information management system.

#### Project Requirements
- Python (>= 3.6.1)
- Virtual Environment Manager (Optional)
- Flask

#### How To Run Project
- Fork project from GitHub https://github.com/bimbo-dev/KungFuSchool.git
- Create virtual environment (Miniconda has been used in this project as the virtual environment manager), and activate the virtual environment.
- Install all the project requirements in the ‘requirements.txt’ by running the command “pip install -r requirements.txt” in your terminal.
- Set the FLASK_APP environment variable by executing the command “export FLASK_APP=run.py”.
- Initialize the database by executing the command “flask db init”, then create the first migration with the command “flask db migrate” and finally update the database with the command “flask db upgrade”.
- Initialize the database with some data by running a command “flask seed_database”. The implementation of the seed method can be found in ‘app/models/seeds.py’.
- Execute the application with the command “flask run”.

#### Login Credentials
 - Username : admin 
 - Password: Password123!
