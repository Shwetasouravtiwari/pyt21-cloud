import os
import os

settings = {
    'host': os.environ.get('ACCOUNT_HOST', 'https://pyt21-cosmosdb.documents.azure.com:443/'),
    'master_key': os.environ.get('ACCOUNT_KEY', '1dCi1Z7mr0RbfuheX7x0PrXLckgAlPkvpbE9muRp00proIJIsUdfnLQtFrbMlJ4ssSIJZoKvcfoXG1jU558mNQ=='),
    'database_id': os.environ.get('COSMOS_DATABASE', 'ProductCatalog')
}