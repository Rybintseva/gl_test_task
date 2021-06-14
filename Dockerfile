FROM ubuntu:20.04

# Install Python3, pip3 and requirements
RUN apt-get update && apt-get install -y python3 python3-pip python3-requests && \
    echo "Installing requirements..." && pip3 install pytest pytest-html --quiet

# Copy repo into Docker image
WORKDIR /gl_test_task
COPY ./  /gl_test_task/

# Run tests with default parameters
CMD pytest framework/tests_api/test_api.py --html=report.html
