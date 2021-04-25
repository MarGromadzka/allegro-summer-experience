# allegro-summer-experience

### Author
Marianna Gromadzka

### Technologies
- Python 3.9.4
- Flask 1.1.2

## Launch

Using Azure hosting:
- To get star summary: https://flaskreposearcher.azurewebsites.net/starsum/MarGromadzka
- To get repos list: https://flaskreposearcher.azurewebsites.net/list/MarGromadzka



Locally:

Run this commends in terminal to install libraries:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
Then in your git repository directory:
```
python app.py
```
Then in your your browser open:
- http://localhost:5000/list/MarGromadzka to get list of repositories
- http://localhost:5000/starsum/MarGromadzka to get star summary

You can view info about other users by changing last part of link. 

## Warning
Github api has 5000 reguest per hour limit.
