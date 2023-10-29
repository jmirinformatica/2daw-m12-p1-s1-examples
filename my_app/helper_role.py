from flask import current_app
from flask_login import current_user
from flask_principal import identity_loaded, identity_changed, ActionNeed, Permission, Identity, AnonymousIdentity

editor_rol = 'editor'
viewer_rol = 'viewer'

__read_rols = [editor_rol, viewer_rol]
__read_action = ActionNeed('read')
read_permission = Permission(__read_action)

__modify_rols = [editor_rol]
__modify_action = ActionNeed('modify')
modify_permission = Permission(__modify_action)

@identity_loaded.connect
def on_identity_loaded(sender, identity):
    identity.user = current_user

    if hasattr(current_user, 'role'):
        # current_user podria ser anonim
        
        if current_user.role in __read_rols:
            identity.provides.add(__read_action)
        
        if current_user.role in __modify_rols:
            identity.provides.add(__modify_action)

def notify_identity_changed():
    if hasattr(current_user, 'email'):
        # current_user podria ser anonim
        identity = Identity(current_user.email)
    else:
        identity = AnonymousIdentity()
        
    identity_changed.send(current_app._get_current_object(), identity = identity)