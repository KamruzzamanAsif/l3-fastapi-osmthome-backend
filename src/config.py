# global configs
import os

from dotenv import load_dotenv

load_dotenv()

# load fabric credentials
FABRIC_UID = os.getenv("UID")
FABRIC_PWD = os.getenv("PWD")
