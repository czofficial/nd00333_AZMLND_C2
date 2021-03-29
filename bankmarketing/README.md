# Machine Learning Operations

* [Overview](#overview)
* [Architectural Diagram](#architectural-diagram)
* [Key Steps](#key-steps)
* [Screen Recording](#screen-recording)

## Overview
The main objective of this project ist to use Microsoft Azure to configure a cloud-based machine learning production model, before deploying and consuming it. This also includes crating, publishing and consuming a pipeline.

The data for this project is related to direct marketing campaigns of a Portuguese banking institution. The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, in order to access if the product (bank term deposit) would be ('yes') or not ('no') subscribed. The classification goal is to predict if the client will subscribe (yes/no) a term deposit (variable y). [Here is the link to the dataset](https://archive.ics.uci.edu/ml/datasets/bank+marketing).

The project's main steps are the following:
1. Authentication
2. Automated ML experiment
3. Deploy the best model
4. Enable logging
5. Swagger documentation
6. Consume model endpoints
7. Create and publish a pipeline
8. Documentation

## Architectural Diagram
*TODO*: Provide an architectual diagram of the project and give an introduction of each step. An architectural diagram is an image that helps visualize the flow of operations from start to finish. In this case, it has to be related to the completed project, with its various stages that are critical to the overall flow. For example, one stage for managing models could be "using Automated ML to determine the best model". 

## Key Steps
*TODO*: Write a short discription of the key steps. Remeber to include all the screenshots required to demonstrate key steps. 

### Authentication
The Azure command-line interface (Azure CLI) is a set of commands used to create and manage Azure resources. In this step, a service principal is created, using the AzureML Command Module as an extension. A service principal is an identity created for use with applications, hosted services, and automated tools to access Azure resources. This access is restricted by the roles assigned to the service principal, giving you control over which resources can be accessed and at which level. For security reasons, it's always recommended to use service principals with automated tools rather than allowing them to log in with a user identity.

![sp_ml-auth](.Screenshots/sp_ml-auth_01.png)
The command 'az ad sp show' shows the details of the service principal.

![sp_role-error](.Screenshots/sp_role-error.png)
The command 'az ml workspace share' shares a workspace with another user with a given role. In this case, the role assignment already exists.

![iam_role](.Screenshots/iam_role.png)
Once, the service principal (ea69...) is successfully created and shared with the workspace (udacity-ws), the owner (ml-auth) can be seen in the Azure Portal as well. Access control (IAM) is the page that you typically use to assign roles to grant access to Azure resources. It's also known as identity and access management (IAM).

### Automated ML experiment
Text

### Deploy the best model
Text

### Enable logging
Text

### Swagger documentation
Text

### Consume model endpoints
Text

### Create and publish a pipeline
Text

### Documentation
The submission includes this README file that describes the main components of the project and a screencast that shows the entire process of the working ML application.

## Screen Recording
This screen recording shows the entire process of the working ML application, including the following areas:
- Working deplyoed ML model endpoint
- Deployed pipeline
- Available AutoML model
- Successful API requests to the endpoint with a JSON payload

[Here is the link to the screen recording.](https://www.dropbox.com/s/4o3gu8uhmwxfruw/Udacity_ML-Engineer_with_MS-Azure_Project-02_Screen-Recording.mov?dl=0)