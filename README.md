# redmine_sample
This is a project crawl data from redmine server

1. Create new environment 
2. Run pip install -r requirements.txt to install libraries
2. Make new file .env 

   Fill data:
    
   	REDMINE_USERNAME = 'xxxxxx'
		REDMINE_PASSWORD = 'xxxxxx'
		CHATWORK_TOKEN = 'xxxxxxxxxxx'

3. create database: python sqlalchemy_engine.py
		NOTE: 
		please read more about sqlalchemy tutorial: https://www.blog.pythonlibrary.org/2010/02/03/another-step-by-step-sqlalchemy-tutorial-part-2-of-2/
		Document official for sql alchemy: https://docs.sqlalchemy.org/en/13/contents.html
		
4. process data: python process_data.py
