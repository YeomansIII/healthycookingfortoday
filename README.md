# Healthy Cooking for Today
## Getting Started
### Setup Python, pip, and virtuelenv

Pip and virtualenv are used the manage the python dependencies for the project.

```
sudo apt-get install python-pip python-dev build-essential 
sudo pip install --upgrade pip 
sudo pip install --upgrade virtualenv 
```

### Setup node and npm using Node Version Manager (nvm)

Node is used in this project for javascript task running such as compiling SASS and minifying javascript.

1. Install nvm

    ```
    curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.30.2/install.sh | bash
    ```
    After installation is complete, you must close your terminal and reopen it to use `nvm`.
2. Install the required version of node (0.12.7)

    ```
    nvm install 0.12.7
    ```
    
    Any time you need to use this version of node (every time you want to work on this project) you must run:

    ```
    nvm use 0.12.7
    ```
    
3. Install some of the required global dependencies:

    ```
    npm install -g grunt-cli
    npm install -g bower
    ```

### Setup the project
1. Navigate to a common directory where you want to store your virtual environments and github projects, below is a sample structure:

    ```
    ../development/
    
        venvs/
        
        git/
    ```
2. Navigate into the `git/` directory and clone this project if you haven't done so already

    ```
    git clone https://github.com/YeomansIII/healthycookingfortoday.git
    ```
3. Navigate into the `venvs/` directory and run 

    ```
    virtualenv healthycooking
    ```
4. Start the new virtual environment

    ```
    source healthycooking/bin/activate
    ```
5. Move into your `git/healthycookingfortoday/` directory and install the pip dependencies

    ```
    sudo apt-get update && sudo apt-get install python-dev libldap2-dev libssl-dev
    pip install -r requirements.txt
    ```
    This installs all of the required dependencies for the project which are listed in the `requirements.txt` file.
6. Install the required node dependencies and bower components, this can take a few minutes

    ```
    npm install
    bower install
    ```

### Run the project
- You are now ready to run the project! Move into the `django-project/` directory and run:

    ```
    python manage.py gruntserver
    ```
- Navigate to `localhost:8000` in your browser :)


### Every time you want to work on the project
Every time you want to work on the project you will need to remember to activate the appropriate node version and the healthycooking virtual environment:

```
nvm use 0.12.7
source ~/development/venvs/healthycooking/bin/activate
```
