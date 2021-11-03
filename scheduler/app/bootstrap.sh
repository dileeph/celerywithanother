#!/bin/sh

celery -A scheduler beat --loglevel=INFO 