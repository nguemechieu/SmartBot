

class user (object):


    def __init__ (self):
        self.username = None
        self.password = None
        self.email = None
        self.first_name = None
        self.last_name = None
        self.middle_name = None
        self.is_active = None
        self.is_staff = False
        self.is_superuser = False
        self.groups = []
        self.user_permissions = []
        self.user_permissions_groups = []
