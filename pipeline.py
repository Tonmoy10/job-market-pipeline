import subprocess,sys

def run_pipeline():

    print("Extracting the jobs...")
    subprocess.run([sys.executable,"src/extract.py"],check=True)

    print("Loading jobs to the database...")
    subprocess.run([sys.executable,"src/load.py"],check=True)

    print("Running the quality tests and sql models...")
    subprocess.run(["dbt","build"],cwd="dbt_project/market_transform",check=True)

    print("Pipeline execution successful!")

run_pipeline()