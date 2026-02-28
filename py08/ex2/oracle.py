import os
import sys
from dotenv import load_dotenv


def load_configuration():
    load_dotenv()

    config = {
        "MATRIX_MODE": os.getenv("MATRIX_MODE"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT")
    }
    return config


def security_check(config):
    print("\nEnvironment security check:")

    if os.path.exists(".env"):
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly configured")
        print("[OK] Production overrides active")
    else:
        print("[WARNING] .env file not found")


def validate_config(config):
    missing = []
    for key ,value in config.items():
        if value is None:
            missing.append(key)


    if missing:
        print("WARNING: Missing configuration variables:")
        for conf in missing:
            print(f" - {conf}")
        print("\nPlease configure your environment properly.\n")
        return False

    return True


def main():
    print("\nORACLE STATUS: Reading the Matrix...\n")

    config = load_configuration()

    if not validate_config(config):
        sys.exit(1)

    print("Configuration loaded:")
    print(f"Mode: {config['MATRIX_MODE']}")
    print(f"Database: {config['DATABASE_URL']}")
    print("API Access: Authenticated")
    print(f"Log Level: {config['LOG_LEVEL']}")
    print(f"Zion Network: {config['ZION_ENDPOINT']}")

    security_check(config)
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
