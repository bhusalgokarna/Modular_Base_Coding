import os
import pandas as pd
from src.verkeerOngevallen.models.pipeline import AccidentDataPipeline
import argparse

def main():
    # Argument parser for the path
    parser = argparse.ArgumentParser(description="Process accident data.")
    parser.add_argument(
        "--path",
        default="Data",  # Set the default path to "Data"
        help="Path to the data folder (default: Data)."
    )
    args = parser.parse_args()

    try:
        # Initialize the pipeline and process the data
        pipeline = AccidentDataPipeline(args.path)
        df = pipeline.process_data()
        
        # Print the first 5 rows of the dataframe
        print(df.head())
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
