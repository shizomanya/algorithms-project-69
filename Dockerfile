FROM node:18-bullseye

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3.10 \
    python3.10-venv \
    python3.10-dev \
    pip

# Set Python 3.10 as the default python and pip
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1
RUN update-alternatives --install /usr/bin/pip3 pip3 /usr/bin/pip3.10 1

# Install poetry
RUN curl -sSL 'https://install.python-poetry.org' | python3.10 -

# Copy project files
WORKDIR /project
COPY . .

# Setup the project
RUN chmod +x ./code-setup
RUN ./code-setup

# Install node packages
RUN npm install
