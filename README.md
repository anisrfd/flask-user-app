# Python Flask User Create App

 Simple python flask user create, delete, update app with sqlite database.
 
 
### Installation instructions (for linux)

Run the commands in a terminal or command-prompt.

- Install `Python 3.6 or >3.6` for your operating system, if it does not already exist.

  - For [Mac](https://www.python.org/ftp/python/3.6.8/python-3.6.8-macosx10.9.pkg)

  - For [Windows](https://www.python.org/ftp/python/3.6.8/python-3.6.8-amd64.exe)

  - For Ubuntu/Debian

  ```bash
  sudo apt-get install python3.6
  ```

  Check if correct version of Python (3.6) is installed.

  ```bash
  python --version
  ```
  
* Clone the project from github on your local machine.   
    ```
    git clone https://github.com/anisrfd/flask-user-app.git
    ```

* open the project directory.
    ```
    cd flask-user-app/
    ```
* Get `virtualenv`.

    ```bash
    pip install virtualenv
    ``` 
* Create a virtual environment named `venv` using python`3.6` or > `3.6` and activate environment.  
    ```
    python3 -m venv venv
    ```
    ```
    source venv/bin/activate
    ```
* Upgrade pip if needed.  
    ```
    pip install --upgrade pip
    ```
* Install python dependencies from requirements.txt.
    ```
    pip install -r requirements.txt
    ```
* Given a crudapp.py file with the application in it named app this is how it can be run.
    ```
    export FLASK_APP=crudapp.py
    ```
* Initialize the database .
    ```
    flask db init
    ```
    ```
    flask db migrate -m "entries table"
    ```
    ```
    flask db upgrade
    ```
* To run the project at http://127.0.0.1:5000/:
    ```
    flask run
    ```

