
# redmine_sample  
This is a project crawl data from redmine server  
  
1. Install mkvirtualenv (tools use manage environments in python) 	
> [https://medium.com/@aaditya.chhabra/virtualenv-with-virtualenvwrapper-on-ubuntu-34850ab9e765](https://medium.com/@aaditya.chhabra/virtualenv-with-virtualenvwrapper-on-ubuntu-34850ab9e765)
>[http://mkelsey.com/2013/04/30/how-i-setup-virtualenv-and-virtualenvwrapper-on-my-mac/](http://mkelsey.com/2013/04/30/how-i-setup-virtualenv-and-virtualenvwrapper-on-my-mac/)
2. Create new environment use mkvirtualenv <environment_name>
3. Install libraries: Run pip install -r requirements.txt
4. Make new file .env: cp .env_sample .env
  
   Fill data:  
      
    REDMINE_USERNAME = 'xxxxxx'  
    REDMINE_PASSWORD = 'xxxxxx'  
    CHATWORK_TOKEN = 'xxxxxxxxxxx'  
  
5. create database: python sqlalchemy_engine.py  
  
    NOTE:   
    Please read more about sqlalchemy tutorial: https://www.blog.pythonlibrary.org/2010/02/03/another-step-by-step-sqlalchemy-tutorial-part-2-of-2/  
    Document official for sql alchemy: https://docs.sqlalchemy.org/en/13/contents.html  
      
6. process data: python process_data.py