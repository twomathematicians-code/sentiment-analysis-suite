import logging, sys
logging.basicConfig(stream=sys.stdout, level=logging.INFO,
    format="%(asctime)s %(levelname)-5s %(message)s", datefmt="%H:%M:%S")
