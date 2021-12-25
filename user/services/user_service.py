from django.contrib.auth import authenticate, login
from ..models import User


class UserService:
    model = User

    def __init__(self, request=None, user=None):
        self.request = request
        self.user = user

    def create_user(self, *args, **kwargs):
        """
        User Create method
        :param args:
        :param kwargs:
        :return: newly created user
        """
        # TODO: Apply necessary validation
        user = self.model.objects.create_user(**kwargs)
        return user

    def get_user_list(self, *args, **kwargs):
        """
        Return user list
        :param args:
        :param kwargs:
        :return: list of users
        """
        user_list = self.model.objects.all()
        return user_list

    def get_all_active_user_list(self, *args, **kwargs):
        """
        Return all active user list
        :param args:
        :param kwargs:
        :return: list of active users
        """
        active_user_list = self.model.objects.filter(is_acvite=True)
        return active_user_list

    def user_login(self, username, password):
        """
        :param username:
        :param password:
        :return: authenticated user
        """
        authenticated_user = authenticate(username=username,password=password)
        if authenticated_user:
            login(request=self.request, user=authenticated_user)
            return authenticated_user
        else:
            return None
