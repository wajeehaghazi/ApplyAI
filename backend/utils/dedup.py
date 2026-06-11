def deduplicate_by_url(
    jobs: list) -> list:

    seen_urls = set()
    unique_jobs = []

    for job in jobs:
        url = job.get("job_url")

        if url and url not in seen_urls:
            seen_urls.add(url)

            unique_jobs.append(job)

    return unique_jobs