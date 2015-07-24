from django.contrib.auth.models import User


# Thanks to:
# http://www.masnun.com/2014/01/03/python-social-auth-custom-pipeline.html

def associate_by_email(**kwargs):
    try:
        email = kwargs['details']['email']
        kwargs['user'] = User.objects.get(email=email)
    except:
        pass
    return kwargs
