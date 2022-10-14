from os import access
import jwt, datetime

# if __name__ == "__main__":

def create_access_token(id):
    return jwt.encode({
        'user_id':id,
        'exp':datetime.datetime.utcnow()+ datetime.timedelta(seconds=1000),
        'iat':datetime.datetime.utcnow()
    },'nayan_access',algorithm='HS256')

def create_refresh_token(id):
    return jwt.encode({
        'user_id':id,
        'exp':datetime.datetime.utcnow()+ datetime.timedelta(days=7),
        'iat':datetime.datetime.utcnow()
    },'nayan_refresh',algorithm='HS256')