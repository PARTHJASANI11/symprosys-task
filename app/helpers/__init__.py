import datetime

import jwt

from app.core import TOKEN_SECRET_KEY, task_logger


class Helper:
    """Helper class to define helper methods"""

    @staticmethod
    def generate_access_token(user_name: str):
        """Method to generate an access token"""
        try:
            data = {
                "sub": user_name,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
                }
            jwt_token = jwt.encode(data, TOKEN_SECRET_KEY, algorithm="HS256")
            return jwt_token
        except Exception as e:
            task_logger.excption("Error while generating access token", e)


helper = Helper()