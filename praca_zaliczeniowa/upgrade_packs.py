import subprocess
import sys

def upgrade_all_packages():
    # Get list of outdated packages
    print("Checking for outdated packages...")
    result = subprocess.run([sys.executable, '-m', 'pip', 'list', '--outdated', '--format=freeze'],
                            capture_output=True, text=True)
    outdated = result.stdout.strip().split('\n')

    if not outdated or outdated == ['']:
        print("All packages are up to date.")
        return

    # Extract package names
    packages = [line.split('==')[0] for line in outdated]

    # Upgrade each package
    for package in packages:
        print(f"Upgrading {package}...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', '--upgrade', package])

    print("All packages upgraded.")

if __name__ == "__main__":
    upgrade_all_packages()
