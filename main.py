from flask import Flask, jsonify
import os, requests


app = Flask(__name__)

# Read the token from the file
with open('/var/run/secrets/kubernetes.io/serviceaccount/token', 'r') as token_file:
    token = token_file.read().strip()

KUBERNETES_SERVICE_HOST = os.getenv('KUBERNETES_SERVICE_HOST')

# Set the URL for the API call
url = f'https://{KUBERNETES_SERVICE_HOST}/apis/batch/v1/namespaces/default/jobs'

requests.packages.urllib3.disable_warnings()

# Set headers with the authorization token
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {token}'
}

# Read the data from the JSON file
with open('k8s-resources/hello-world-job.json', 'r') as helloworld_job_json_file:
    helloworld_job = helloworld_job_json_file.read()

@app.route('/api/', methods=['POST'])
def api():
    # Make the POST request
    response = requests.post(url, headers=headers, data=helloworld_job, verify=False)

    # Check the response status
    if response.status_code == 201:
        print("Job created successfully.")
        status="success"
    else:
        print(f"Failed to create the job. Status code: {response.status_code}")
        print(response.text)
        status="fail"
    return jsonify(status=status)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
