FROM python:3

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy repo into Docker image
WORKDIR /test_task
COPY . .

# Run tests with default parameters
CMD pytest framework/tests_api/test_api.py --html=report.html
