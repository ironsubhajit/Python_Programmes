"""
Implement a @access_control decorator that can be used like this:
@access_control(access_level)
def delete_some_file(filename):
    # perform the deletion operation
    print('{} is deleted!'.format(filename))
Your decorator should meet the following requirements:
- It takes in an argument `access_level` and would compare the current user's role with the access level.
- You can get the current user's role, represented by an integer, by calling the `get_current_user_role()` function.
    You don't need to implement this function, we will take care of it for you.
- You may assume smaller access level value would have higher privilege. For example, 0 - admin, 1 - user, 2 - guest.
    So you can check if the user has proper access level like this:
if get_current_user_role() <= access_level:
    # do something
else:
    # forbid
- If the user has the proper access level, we allow the user to call the function (that has this decorator).
- If the user does not have a proper access level, we raise a `PermissionError` with the message:
    'You do not have the proper access level.'
- The decorator should be generic, which means it can be applied to any function that has any amount of
    arguments (or key word arguments).
- Your decorator should keep the original function's `__name__` and `__doc__` strings.
"""

import functools as ft

from random import randint


def get_current_user_role():
    return randint(0, 3)


def access_control(access_level: int):
    def my_decorator(func):
        @ft.wraps(func)
        def secure_func(*args, **kwargs):
            if get_current_user_role() <= access_level:
                return func(*args, **kwargs)
            else:
                return 0


        return secure_func
    return my_decorator


@access_control(1)
def delete_some_file(filename):
    """
    0. Admin
    1. User
    2. Guest
    """
    # perform the deletion operation
    print('{} is deleted!'.format(filename))
    return True


if __name__ == '__main__':
    status = False
    count = 1
    while not status:
        status = delete_some_file("Restricted File")
        if not status:
            print(f"attempt: {count}\n Not Deleted!")
            count = count + 1
        elif status:
            print(f"File Deleted on Attempt: {count}")
