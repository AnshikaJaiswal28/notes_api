# notes_api

A simple note-taking application API built with Django and Django REST Framework. This API provides functionality to create, read, update, and delete notes, and comes with integrated Swagger documentation for easy API exploration.

Features- 
1)Create a new note
2)Retrieve a list of notes
3)Get details of a single note
4)Update a note (full or partial updates)
5)Swagger UI for API exploration


Technologies Used-
1)Python 3.10+
2)Django 4.0+
3)Django REST Framework
4)MySQL (or any other DB you prefer)
5)Swagger (drf-yasg)


Before you begin, ensure you have met the following requirements:

1)You have installed Python >= 3.10
2)You have installed MySQL
3)You have installed pip and virtualenv
4)You have a MySQL database set up and running


Getting Started
Follow the instructions below to set up and run the project locally.

1. Clone the Repository-
git clone https://github.com/yourusername/notes-api.git
cd notes-api

3. Create and Activate a Virtual Environment (Here 'myenv' is the virtual environment name I used. You can give it any name)
Create a virtual environment to isolate your project dependencies - python -m venv myenv


Activate the virtual environment (for Windows) - myenv\Scripts\activate
Activate the virtual environment (for macOS/Linux) - source myenv/bin/activate

3. Install Project Dependencies
Once the virtual environment is active, install the required Python packages: pip install -r requirements.txt


4. Configure MySQL Database
Create a MySQL database and configure the connection in the settings.py file. Open notesapp/settings.py and add the following details in the DATABASES section:


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

5. Apply Migrations
Run the following commands to create the necessary database tables:

python manage.py makemigrations
python manage.py migrate


6. Run the Development Server
Once the migrations are complete, start the Django development server: python manage.py runserver


The API will now be accessible at http://127.0.0.1:8000/. This is just the landing page. For testing go to  http://127.0.0.1:8000/api/notes . 

#API Documentation
To explore and test the API, navigate to the Swagger UI at:  http://127.0.0.1:8000/swagger/

Available Endpoints:
POST /api/notes/ - Create a new note
GET /api/notes/query/ - Retrieve a list of notes
GET /api/notes/{id}/ - Retrieve details of a specific note
PUT /api/notes/{id}/update/ - Update a note
PATCH /api/notes/{id}/update/ - Partially update a note


#Contributing
If you would like to contribute to this project, feel free to submit a pull request. Contributions are always welcome! Email me at - jaiswalanshika2000@gmail.com
