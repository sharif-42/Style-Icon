from ..models import User


class UserService:
    model = User

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
