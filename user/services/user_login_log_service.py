from django.utils import timezone

from ..models import UserLoginLog


class UserLoginLogService:
    """The service class for logging customer login attempts. """

    def __init__(self, request=None):
        self.request = request

    model = UserLoginLog

    def log_login_attempt(self, username, is_successful=True):
        """
        The static method for logging login attempts

        :param username: The username used to sign in with
        :param email: The email used to sign in with
        :param is_successful: The result of the attempt
        :return:
        """
        attempted_time = timezone.now()
        # TODO: Need to work for browser and IP-address
        browser = None
        ip_address = None

        user_login_log = UserLoginLog.objects.create(
            used_user_name=username,
            used_email=self.request.data.get("email", ""),
            is_successful=is_successful,
            attempted_time=attempted_time,
            browser=browser,
            ip_address=ip_address,
        )
        return user_login_log
