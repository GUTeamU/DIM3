DIM3 - Requirements Tracker
===========================

### Setup

1. Create and run your virtual enviroment.
    ```bash
    virtualenv VENV
    source VENV
    ```

2. Install the dependencies
    ```bash
    pip install -r requirements.txt
    ```

3. Setup the database
    ```bash
    python requirementsTracker/manage.py syncdb
    ```

4. Start the application
    ```bash
    python requirementsTracker/manage.py runserver
    ```
