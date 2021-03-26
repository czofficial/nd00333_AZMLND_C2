from azureml.core import Workspace
from azureml.core.webservice import Webservice

# Requires the config to be downloaded first to the current working directory
ws = Workspace.from_config(path="/Users/cz.official/Documents/Studium/2020 - Udacity/Machine Learning Engineer with Microsoft Azure/3. Machine Learning Operations/Github/nd00333_AZMLND_C2/bankmarketing/config.json")

# Set with the deployment name
name = "bankmarketing-deployment"

# load existing web service
service = Webservice(name=name, workspace=ws)
logs = service.get_logs()

# enable application insight
service.update(enable_app_insights=True)

for line in logs.split('\n'):
    print(line)