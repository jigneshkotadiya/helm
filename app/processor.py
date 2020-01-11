from django.conf import settings

def debug_context(request):
    debug_flag = settings.DEBUG
    return{"debug_flag":debug_flag}
