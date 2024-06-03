from yalexs.api import Api 
from yalexs.authenticator import Authenticator
import restricted

api = Api(timeout=20)
authenticator = Authenticator(api, "email", restricted.email, restricted.august_password, restricted.august_token_cache)
authentication = authenticator.authenticate()


def confirm_authorization(current_auth):
    state = current_auth.state
    if 'bad_password' in state.name.lower():
        print('Password was wrong. Maybe it expired? Check in the August app on your phone. There is no website.')
        return
    if 'requires_validation' in state.name.lower():
        authenticator.send_verification_code()
        authenticator.validate_verification_code(input('Check your email for a 6 digit code from August; input here.'))
        corrected = authenticator.authenticate()
        print(f'The new August token is:\n{corrected.access_token}\n and the current state is {corrected.state}.')
        if 'validated' in corrected.state.name.lower():
            return corrected
        else:
            print('Error in authorizing. Try again; maybe pasting error? Debug here and check JSON for clues')
            return
    if 'authenticated' in state.name.lower():
        print('Already authenticated.')
        return current_auth
    else:
        print('Authentication error. Either that or they changed their JSON. Check confirm_authorization() function.')
        return


cleared = confirm_authorization(authentication)
all_locks = api.get_locks(authentication.access_token)


class Lock:
    def __init__(self, name, id, api):
        self.name = name
        self.id = id
        self.api = api
        self.token = cleared.access_token

    def unlock(self):
        self.api.unlock(self.token, self.id)
        return f'{self.name} unlocked.'

    def lock(self):
        self.api.lock(self.token, self.id)
        return f'{self.name} locked.'


def get_locks_and_ids():
    name_and_id = {}
    for lock in all_locks:
        name_and_id[lock.device_name] = lock.device_id
    return name_and_id


def get_my_front_door():
    locks = get_locks_and_ids()
    for lock in locks:
        if 'front door' in lock.lower():
            return Lock(lock, locks[lock], api)


if __name__ == '__main__':
    front_door = get_my_front_door()
