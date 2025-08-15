import os

def authenticate_user(username, password):
    # Hardcoded password (security risk)
    if password == "SuperSecret123":
        print("Authenticated!")
    else:
        print("Access denied.")

def run_shell(cmd):
    # Unsafe: direct shell execution
    os.system(cmd)
