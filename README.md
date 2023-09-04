# README #
*Proyect made using Python 3.9*

Create virtual environment
```
python -m venv ./venv
```

Activate venv
```
source venv/bin/activate
```


Install requirements 
```
pip install -r requirements.txt
```
# Following [0.17.13 tutorial](https://docs.greatexpectations.io/docs/deployment_patterns/how_to_use_gx_with_aws/how_to_use_gx_with_aws_using_cloud_storage_and_pandas)

1. Upload `titanic.csv` to your S3 bucket/prefix.
2. Update your bucket and prefix in the script `a01_updating_bucket_prefix.py`, lines 5 and 6, then run it.
3. Update the bucket in `a02_gx_script.py`, line 2. Then, rut it. The problem is here.

Great expectation is saving the JSON file with a `.` after the date but it's trying to retrieve it from the path with a `/` in after the date.

For example, its saving it as `~/20230901T143314.240808Z/~` but its looking for `~/20230901T143314/240808Z/~`

Error:
```sh
"great_expectations.exceptions.exceptions.InvalidKeyError: Unable to retrieve object from TupleS3StoreBackend with the following Key: gx_titanic/test_titanic/__none__/20230901T143314/240808Z/s3_datasource-titanic_dataset.json"
```
