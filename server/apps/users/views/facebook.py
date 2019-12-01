from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

    def post(self, request, *args, **kwargs):
        result = super(FacebookLogin, self).post(request, *args, **kwargs)
        result.data['name'] = request.user.get_full_name()
        return result
