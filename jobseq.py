# Define a Job class to hold job attributes
class Job:
    def __init__(self, id, deadline, profit):
        self.id = id            # Job ID
        self.deadline = deadline  # Deadline of the job
        self.profit = profit      # Profit of the job

def job_sequencing(jobs):
    # Step 1: Sort the jobs based on profit in descending order
    jobs.sort(key=lambda job: job.profit, reverse=True)

    n = len(jobs)  # Number of jobs
    # Create an array to track which job is scheduled in each time slot
    result = [None] * n  
    # Create an array to track if a time slot is occupied
    slot = [False] * n    

    # Step 2: Iterate over the sorted jobs
    for job in jobs:
        # Try to find a time slot for this job
        # Start from the last possible time slot (min(deadline, n) - 1)
        for j in range(min(job.deadline, n) - 1, -1, -1):
            if not slot[j]:  # Check if this time slot is free
                slot[j] = True  # Mark this slot as occupied
                result[j] = job.id  # Schedule the job in this slot
                break  # Stop checking for other slots

    # Step 3: Collect all scheduled job IDs
    scheduled_jobs = [job_id for job_id in result if job_id is not None]
    return scheduled_jobs  # Return the list of scheduled jobs

# Example usage

    # List of jobs (ID, Deadline, Profit)
jobs = [
    Job(1, 2, 100),
    Job(2, 1, 19),
    Job(3, 2, 27),
    Job(4, 1, 25),
    Job(5, 3, 15)
]

scheduled_jobs = job_sequencing(jobs)  # Call the function
print("Scheduled Jobs:", scheduled_jobs)  # Print the scheduled job IDs
