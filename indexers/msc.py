def index_msc(contID="", driver, logger):
    base_url = ""


    normalizers = {
            "date" : [],
            "status" : [],
            "location" : [],
            "transport" : [],
            "voyage" : []
            }

    # Step 1: Open the base URL
    try:


    except Exception:
        logger.warning('', 'connection reset', extra=d)     

    # Step 2: Find container form and submit container ID


    # Step 3: Access status page and collect status information


    # Step 4: Transform and normalize status data
    



    return container_status, indexer_status
