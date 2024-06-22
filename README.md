# Student Report Card Project

This Django project manages student information, including departments, student IDs, marks for various subjects, and generates ranks based on total marks.

## Features
- Search functionality to find students by name, department, ID, email, age, or address.  
- View and manage student marks for each subject.  
- Automatic generation of student ranks based on total marks.  
- Pagination of student records for easier navigation.

## Prerequisites
- Python 3.x  
- Django 5.0.x  
- Other dependencies listed in requirements.txt
```makefile
asgiref==3.8.1
Django==5.0.6
Faker==25.8.0
python-dateutil==2.9.0.post0
six==1.16.0
sqlparse==0.5.0
tzdata==2024.1
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/bhaskar-nie/reportcardproj.git
cd reportcardproj
```
### 2. Set up virtual environment (optional but recommended)

```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Apply database migrations
```bash
python manage.py migrate
```
### 5. Create a superuser (to access admin panel)
```bash
python manage.py createsuperuser
```

## Running the Project

### 1. Start the development server

```bash
python manage.py runserver
```
### 2. Access the application

Open your web browser and go to `http://127.0.0.1:8000/`

### 3. Admin Panel
- Navigate to `http://127.0.0.1:8000/admin/`  
- Log in using the superuser credentials created earlier.  
- Use the admin panel to manage Student, Department, Subject, Student ID, Subject Marks, and Rank data.


## Usage

### Search for Students

To search for students:

1. Enter a search query in the search bar located on the homepage (`/`).
2. You can search by name, department, ID, email, age, or address.

### View Student Marks

To view a student's marks in different subjects:

1. From the list of students displayed, click on a student's ID.
2. You will be redirected to a page showing the student's marks in various subjects.

### View Student Rank

To view a student's rank based on total marks:

1. Navigate to the student details page.
2. The student's current rank will be displayed based on their total marks.

## Populating the Database
To populate the database with initial data, run the following commands in your terminal:

### 1. Seed Students, Subject Marks, and Ranks

```bash
python seed.py seed_db
python seed.py create_subject_marks
python seed.py generate_rank
```
## Testing
To run tests:
```bash
python manage.py test
```

## Deployment
For deploying Django applications, please refer to [Django's official deployment documentation](https://docs.djangoproject.com/en/5.0/howto/deployment/).
## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your proposed changes.

## Contact

For support or questions, [Contact me](mailto:official.beingbhaskar@gmail.com).

## Notes

- Ensure your virtual environment is activated before running any commands (`source env/bin/activate`).
- Adjust the number of students (`n`) as needed in `seed_db()` function for testing or production scenarios.
- Customize the project further based on your specific requirements or enhancements.
