# have site running
# have a git repo
# have button on raspi that updates the site;
    # shuts down site
    # shows maintainance page
    # pulls new develop from git
    # restarts site
# have a menu structure

from app import app

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80)
    # app.run(host='0.0.0.0', port=80)