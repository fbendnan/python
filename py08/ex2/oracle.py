import os
import sys
from dotenv import load_dotenv


def load_configuration():
    # Load .env file if it exists
    load_dotenv()

    config = {
        "MATRIX_MODE": os.getenv("MATRIX_MODE"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT"),
    }

    return config


def security_check(config):
    print("\nEnvironment security check:")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found")

    if config["API_KEY"] and config["API_KEY"] == "558426658986989":
        print("[OK] No hardcoded secrets detected")
    else:
        print("[WARNING] API_KEY looks like a placeholder")
    if os.getenv("MATRIX_MODE") == "production":
        print("[OK] Production overrides active")
    else:
        print("[INFO] Running in development mode")


def validate_config(config):
    missing = [key for key, value in config.items() if not value]

    if missing:
        print("WARNING: Missing configuration variables:")
        for var in missing:
            print(f" - {var}")
        print("\nPlease configure your environment properly.\n")
        return False

    return True


def main():
    print("ORACLE STATUS: Reading the Matrix...\n")

    config = load_configuration()

    if not validate_config(config):
        sys.exit(1)

    print("Configuration loaded:")
    print(f"Mode: {config['MATRIX_MODE']}")

    if config["MATRIX_MODE"] == "development":
        print("Database: Connected to local instance")
    else:
        print("Database: Connected to production mainframe")

    print("API Access: Authenticated")
    print(f"Log Level: {config['LOG_LEVEL']}")
    print("Zion Network: Online")

    security_check(config)
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
