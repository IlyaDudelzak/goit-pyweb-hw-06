from create_tables import create_tables
from statistic import get_statitics
from faking import fake_fill
from pprint import pprint
from pathlib import Path
from faker import Faker

import logging
import rich

def print_results(results: list):
    if results:
        rich.print("[yellow]Result of statistics tasks:[/yellow]")
        for result in results:
            rich.print(result)
    else:
        rich.print("[red]Result of statistics empty[/red]")


def main():
    skip_created_tables = True
    if create_tables(skip_created_tables):
        if not skip_created_tables:
            fake_fill()
        results = get_statitics()
        print_results(results)

    

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    FORMAT = "%(asctime)s  %(message)s"
    logging.basicConfig(format=FORMAT, level=logging.DEBUG)
    main()


