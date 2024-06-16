import pwd
"""
Reference: https://docs.python.org/3/library/pwd.html
"""

def fetch_users():
    users = []
    for user in pwd.getpwall():
        if user.pw_uid  >= 1000 and 'home' in user.pw_dir:
            users.append(
                {
                    'name': user.pw_name,
                    'id': user.pw_uid,
                    'home':user.pw_dir,
                    'shell': user.pw_shell
                }
            )
    return users