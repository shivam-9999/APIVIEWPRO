#  create a folder
     mkdir _
     cd _
# Create a virtual environment
     pip install virtualenv
     virtualenv myenv
     
# Activate the environment
    source/myenv/bin/activate
    
# Install djgnorestframework
     pip install djangorestframework.
     
# create Server
     django-admin startproject project_name

# Start app
     python manage.py startapp  project_name

# migeate your project
     1. python [manage.py](http://manage.py/) makemigrations
     2. python [manage.py](http://manage.py/) migrate

# create superuser
    python manage.py createsuperuser
    project Folder

# runserver 
     python manage.py runserver



# git commands 
     git init
     git remote add origin url
     git status
     git add .
     git commit -m "initial commit"
     git branch -m main
     git push -u origin main
     git pull origin main --rebase
     git rebase --continue
     
     
     
     
