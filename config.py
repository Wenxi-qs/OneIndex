class BaseConfig:
    CLIENT_ID = ''
    CLIENT_SECRET = ''
    REDIRECT_URI = 'http://localhost:5000/login/redirect'
    ACCESS_TOKEN = None
    REFRESH_TOKEN = None
    DRIVE_ID = None
    SCOPES = 'offline_access+Files.Read+Files.Read.All'


class DevelopmentConfig(BaseConfig):
    DEBUG = True


config = {
    'development': DevelopmentConfig,
}
