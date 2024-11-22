import subprocess

def run_management_commands():
    try:
        # Run 'migrate' command
        print("Running migrations...")
        subprocess.check_call(['python', 'manage.py', 'migrate'])
        
        # Run 'collectstatic' command
        print("Collecting static files...")
        subprocess.check_call(['python', 'manage.py', 'collectstatic', '--noinput'])

        print("Both commands ran successfully!")
        
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_management_commands()