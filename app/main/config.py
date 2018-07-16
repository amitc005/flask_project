class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Password@123@localhost:3306/texada_project'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True


config_by_name = dict(
    dev=DevelopmentConfig,
)
