FROM ghabxph/python-common:0.0.2

# Copy project source code
COPY src /app

# WORKDIR to Source Code
WORKDIR /app

# Start the project
ENTRYPOINT ["/usr/local/bin/python", "./main.py"]
