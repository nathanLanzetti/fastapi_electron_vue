import os

# Path of homedir and databases for the projects

HOME = os.path.join(os.path.expanduser("~"))  # get user dir
HOME_DIR = os.path.join(HOME, "ucollaborate")
DATABASE_PATH = os.path.join(HOME_DIR, "databases")
if not os.path.exists(HOME_DIR):
    os.makedirs(HOME_DIR)
if not os.path.exists(DATABASE_PATH):
    os.makedirs(DATABASE_PATH)
