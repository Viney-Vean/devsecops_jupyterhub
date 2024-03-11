# jupyterhub_config.py

c.JupyterHub.authenticator_class = 'jupyterhub.auth.PAMAuthenticator'
c.PAMAuthenticator.whitelist = {'admin'}
c.Authenticator.admin_users = {'admin'}
c.LocalAuthenticator.create_system_users = True
