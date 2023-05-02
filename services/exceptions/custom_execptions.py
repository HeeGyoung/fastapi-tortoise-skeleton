from fastapi import HTTPException, status


class UnauthorizedException(HTTPException):
    def __init__(self, message: str):
        super(UnauthorizedException, self).__init__(
            status.HTTP_401_UNAUTHORIZED, message
        )


class ForbiddenException(HTTPException):
    def __init__(self, message: str):
        super(ForbiddenException, self).__init__(status.HTTP_403_FORBIDDEN, message)
