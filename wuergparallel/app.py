import concurrent.futures
import jobs
import zukunft


# Testing wait_for_all_jobs_to_have_been_finished()
zukunft.wait_for_all_jobs_to_have_been_finished(jobs.get_jobs(), concurrent.futures.FIRST_COMPLETED)
#zukunft.wait_for_all_jobs_to_have_been_finished(jobs.get_jobs(), concurrent.futures.ALL_COMPLETED)

