from yalexs.api import Api 
from yalexs.authenticator import Authenticator
import misc

api = Api(timeout=20)
authenticator = Authenticator(api, "email", misc.email, misc.august_password)
all_locks = api.get_locks(misc.august_token)


class Lock:
    def __init__(self, name, id, api):
        self.name = name
        self.id = id
        self.api = api
        self.token = misc.august_token

    def unlock(self):
        self.api.unlock(self.token, self.id)

    def lock(self):
        self.api.lock(self.token, self.id)


def get_locks_and_ids():
    name_and_id = {}
    for lock in all_locks:
        name_and_id[lock.device_name] = lock.device_id
    return name_and_id


def get_first_lock():
    locks = get_locks_and_ids()
    for lock in locks:
        return Lock(lock, locks[lock], api)



# authentication = authenticator.authenticate()

# State can be either REQUIRES_VALIDATION, BAD_PASSWORD or AUTHENTICATED
# You'll need to call different methods to finish authentication process, see below
# state = authentication.state

# If AuthenticationState is BAD_PASSWORD, that means your login_method, username and password do not match

# If AuthenticationState is AUTHENTICATED, that means you're authenticated already. If you specify "access_token_cache_file", the authentication is cached in a file. Everytime you try to authenticate again, it'll read from that file and if you're authenticated already, Authenticator won't call Yale Access again as you have a valid access_token


# If AuthenticationState is REQUIRES_VALIDATION, then you'll need to go through verification process
# send_verification_code() will send a code to either your phone or email depending on login_method
# authenticator.send_verification_code()
# # Wait for your code and pass it in to validate_verification_code()
# validation_result = authenticator.validate_verification_code('678634')
# # If ValidationResult is INVALID_VERIFICATION_CODE, then you'll need to either enter correct one or resend by calling send_verification_code() again
# # If ValidationResult is VALIDATED, then you'll need to call authenticate() again to finish authentication process
# authentication = authenticator.authenticate()
