import itc_utils.flight_service as itcfs

readClient = itcfs.get_flight_client()

nb_data_request = {
    'data_name': """bankloan-training-data.csv""",
    'interaction_properties': {
        #'row_limit': 500,
        'infer_schema': 'true',
        'infer_as_varchar': 'false'
    }
}

flightInfo = itcfs.get_flight_info(readClient, nb_data_request=nb_data_request)

data_df = itcfs.read_pandas_and_concat(readClient, flightInfo, timeout=240)
data_df_sample = data_df.head(3)
print(data_df_sample)

# Import the lib
from ibm_watson_studio_lib import access_project_or_space
wslib = access_project_or_space()

# let's assume you have the pandas DataFrame  pandas_df which contains the data
# you want to save as a csv file
wslib.save_data("output.csv", data_df_sample.to_csv(index=False).encode(), overwrite=True)

# the function returns a dict which contains the asset_name, asset_id, file_name and additional information
# upon successful saving of the data



