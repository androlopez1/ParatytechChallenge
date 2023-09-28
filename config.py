"""
Application configuration.

Most configuration is set via environment variables.

For local development, use a .env file to set
environment variables.
"""
from environs import Env
import os

env = Env()
env.read_env()

ENV = env.str("FLASK_ENV", default="development")
DEBUG = env.bool("DEBUG", default=1)
PROJECT_ID=env.str("PROJECT_ID")
HOST=env.str("HOST", default="127.0.0.1")
PORT=env.str("PORT", default="8080")