import great_expectations as gx
s3_bucket = '<S3_Bucket>'


context = gx.data_context.FileDataContext.create("Titanic")
datasource = context.sources.add_or_update_pandas_s3(
    name="s3_datasource", bucket=s3_bucket)

asset = datasource.add_csv_asset(
    name="titanic_dataset",
    batching_regex="titanic.csv")

# Creando Batch Request ------------------------------------------

request = asset.build_batch_request()

context.add_or_update_expectation_suite(expectation_suite_name="test_titanic")
validator = context.get_validator(
    batch_request=request, expectation_suite_name="test_titanic")

# Validaciones ------------------------------------------
validator.expect_column_values_to_be_between(
    column="Age", min_value=0, max_value=120)
validator.expect_column_values_to_be_between(
    column="Sex", min_value=0, max_value=1)

validator.save_expectation_suite(discard_failed_expectations=False)

checkpoint = context.add_or_update_checkpoint(
    name="my_checkpoint",
    validations=[{"batch_request": request, "expectation_suite_name": "test_titanic"}])

# ! The error is here, on the checkpoint.run() !  ------------------------------------------
checkpoint_result = checkpoint.run()
# ! ------------------------------------------

context.open_data_docs()
