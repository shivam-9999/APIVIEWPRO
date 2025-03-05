Create a folder on desktop to create the folder(GPT_EVAL)
3. Create a virtual environment
4. pip install virtualenv
5. virtualenv myenv
6. Activate the environment
7. pip install djangorestframework.
8. django-admin startproject GPT_EVAL
9. cd GPT_EVAL
10. python [manage.py](http://manage.py/) startapp eval_app

```
# register your app in settings.py in "INSTALLED apps"
```

1.  navigatse to [models.py](http://models.py/) file and create two models
2.  migrate your project
3. python [manage.py](http://manage.py/) makemigrations
4. python [manage.py](http://manage.py/) migrate
5.  register your models
    
    [admin.py](http://admin.py/)
    
    admin.site.register ("Nameof model")
    
6. create superuser
    
    python [manage.py](http://manage.py/) createsuperuser
    
    project Folder
