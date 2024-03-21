#!/bin/bash
# flask settings
export FLASK_APP=daily_message.py
export FLASK_DEBUG=0

flask run --host=0.0.0.0 --port=5000