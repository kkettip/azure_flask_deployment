# azure_flask_deployment

### Steps to deploy app in Azure.

##### 1. Create website.

##### 2. Follow instructions on <https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=apt> to install Azure CLI on Linux in terminal/Google cloud shell. Use code: curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash to instal in one command. This will allow users to connect to Azure cloud.

##### 3. Test that Azure CLI is installed with code: az  AZURE will be displayed to confirm that it is installed.

##### 4. Login using code: az login --use-device-code. This provides permission for Google cloud shell to connect with Azure cloud. A url for microsoft Azure will be provided for access to enter code for the login process.

##### 5. Get azure student subscription ID with code: az account list --output table  

##### 6. Change into subscription id with code: az account set --subscription SubscriptionId. Replace SubscriptionId found from table of step 5.

##### 7. Go to Azure web portal and create new resource group name found in Azure's Dashboard.

##### 8. To deploy the website, use code: az webapp up --runtime PYTHON:3.9 --sku B1 --logs into terminal that will automatically generate a group name and app name or code : az webapp up --resource-group <groupname> --name <app-name> --runtime <PYTHON:3.9> --sku <B1>. Insert group name created in step 7 and create an app name for insertion into the code.

##### 9. Once the website is deployed, a url to access the website will be provided.

##### 10. The following is the websites' url for the Telehealth Usage Trends' website.

**<https://kettip-hha504.azurewebsites.net/>**