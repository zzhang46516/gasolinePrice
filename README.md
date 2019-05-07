# gasolinePrice

Regular Gasoline Price

Fetching data from website and show the release date and regular price by state


Getting Started

    git clone git@github.com:zzhang46516/gasolinePrice.git

    or download from https://github.com/zzhang46516/gasolinePrice

Prerequisites

    Python 3.7
    Postgres

with pipenv:

    pipenv install -r requirements.txt
    
with pip:

    pip install -r requirements.txt



Installing

    MacOS:
        create database "rgp"
        in folder my_app:
            run python manage.py migrate
        in folder RegularGasolinePrices:
            run scrapy crawl gasolineprices
        back to forlder my_app:
            run python manage.py runserver
    
    Windows:
        pip install pypiwin32
        
        download Twisted from https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted to root directory
            in filename cp**, ** is your python version
        pip install Twisted*(downloaded Twisted filename)
        
        in folder my_app:
            run python manage.py migrate
        in folder RegularGasolinePrices:
            run scrapy crawl gasolineprices
        back to forlder my_app:
            run python manage.py runserver
        

Next:
    
    open http://localhost:8000 in browser
