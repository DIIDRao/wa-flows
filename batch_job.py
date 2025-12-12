from prefect import flow, task, get_run_logger

@task
def extract_data():
    logger = get_run_logger()
    logger.info("Extracting data...")
    return ["item1", "item2"]

@task
def process_data(items):
    logger = get_run_logger()
    logger.info(f"Processing data: {items}")
    return items

@flow(log_prints=True)   # <---- VERY IMPORTANT
def batch_job():
    print("Starting batch job...")  # this will show in cloud because log_prints=True
    data = extract_data()
    processed = process_data(data)
    print("Batch job completed!")
    return processed

if __name__ == "__main__":
    batch_job()
