import pandas as pd

class CSVHandler:

    def save(self,record):

        # Create a pandas DataFrame from the record
        df = pd.DataFrame(record)

        # Set the 'id' column as the index
        df.set_index('id', inplace=True)

        # Write the DataFrame to a CSV file
        df.to_csv('data/record.csv', index=True)

    def load(self):

        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv('data/record.csv')

        # Convert the DataFrame to a list of dictionaries
        record = df.to_dict(orient='records')

        return record