# Author: Sakthi Santhosh
# Created on: 08/09/2023
def main() -> int:
    from lib import app_handle

    try:
        app_handle.run(debug=True, host="0.0.0.0", load_dotenv=True)
    except KeyboardInterrupt:
        print("Info: Exiting...")
        return 0
    except Exception as exception:
        print("Fatal:", exception)
        return 1

if __name__ == "__main__":
    exit(main())
