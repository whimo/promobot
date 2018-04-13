from app import app as application
import config
import sys

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1].isdigit() and 1 < int(sys.argv[1]) < 65535:
        config.port = int(sys.argv[1])
    application.run(host=config.host, port=config.port, debug=config.debug)

