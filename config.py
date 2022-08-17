import os
SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
SQLALCHEMY_DATABASE_URI = 'postgresql://zfukdmsvcybrxt:40ce75551cc787e6d1598bea9415c2fff4cb6a41b8c8ca8e9fc877fcf7416b82@ec2-52-207-15-147.compute-1.amazonaws.com:5432/db54ebs07bnlou'

# Turn off the Flask-SQLAlchemy event system and warning
SQLALCHEMY_TRACK_MODIFICATIONS = False