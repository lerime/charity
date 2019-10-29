from app.account.models import StudentAuthToken

from rest_framework.authentication import TokenAuthentication


class StudentAuthentication(TokenAuthentication):
    model = StudentAuthToken

    def authenticate_credentials(self, key):
        try:
            token = self.model.objects.select_related('user').get(key=key)
        except self.model.DoesNotExist:
            return (None, '')

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))

        return (token.user, token)