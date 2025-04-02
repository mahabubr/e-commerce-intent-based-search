import logging
import os

filename = os.path.join(os.getcwd(), "app", "logger", "logs", "search.log")

logging.basicConfig(
    filename=filename,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def search_logger(search, refine_search, distance, execution_time):
    formatted_distance = ", ".join([f"{d:.2f}" for d in distance])

    logging.info("=" * 75)
    logging.info("  Intent Search Process Initiated  ")
    logging.info("=" * 75)

    logging.info("  Search Query: %s", search)
    logging.info("  Refined Search Query: %s", refine_search)
    logging.info("  Distance: %s", formatted_distance)
    logging.info("  Execution Time: %.4f seconds", execution_time)

    logging.info("=" * 75)
    logging.info("  Intent Search Process Completed ")
    logging.info("=" * 75 + "\n")
