# Libraries ------------------------------------------
import yaml

# Change for your S3 Bucket and Prefix ------------------------------------------
s3_bucket='<S3_Bucket>'
s3_prefix='gx_titanic'

# Read YAML file ------------------------------------------
with open('Titanic/great_expectations/great_expectations.yml', 'r') as file:
    data = yaml.safe_load(file)

# Modify data ------------------------------------------
# Bucket ------------------------------------------
data['stores']['expectations_S3_store']["store_backend"]['bucket'] = s3_bucket
data['stores']['validations_S3_store']["store_backend"]['bucket'] = s3_bucket

# Prefix ------------------------------------------
data['stores']['expectations_S3_store']["store_backend"]['prefix'] = s3_prefix
data['stores']['validations_S3_store']["store_backend"]['prefix'] = s3_prefix

# Write YAML file ------------------------------------------
with open('Titanic/great_expectations/great_expectations.yml', 'w') as file:
    yaml.safe_dump(data, file)
