## Installation

1. **Clone the repository**:
   
   git@github.com:alamin589/ordertask.git

2. **Create venv**:
 
 Python3 -m venv venv
 
3. **Activate venv**:

source venv/bin/activate  

4. **Install the required packages**:

pip install -r requirements.txt

5. **create migrations**: 

python manage.py makemigrations

6. **migrate database**:: 

python manage.py migrate

7. **Run**: 

python manage.py runserver
