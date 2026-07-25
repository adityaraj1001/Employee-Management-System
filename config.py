# It contains
# configuration things like: URL, API, secretKey, database url

class Config:

    SECRET_KEY = "sha256"

    # MySQL Database Configuration
    # Password: Aditya11@
    # @ is URL encoded as %40
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Aditya11%40@localhost:3306/employee_db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    APP_NAME = "Employee Management System"
    UPLOAD_FOLDER = "uploads"
    API_KEY = "12341asdasd"
    DEBUG = True