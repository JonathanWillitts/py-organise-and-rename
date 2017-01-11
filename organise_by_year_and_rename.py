"""Script to organise and rename subdirectories within a given directory.

Searches for subdirectories whose names start in the format 'yymmdd', then
organises and renames them.

Author: Jonathan Willitts
"""
import configparser
from datetime import datetime
import logging
import os
import re


def main():
    """Configures logging, reads in config file, then executes organise and
    rename function.
    """
    # Create logger.
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    log_format = '[%(asctime)s] %(levelname)-8s %(message)s'
    log_formatter = logging.Formatter(log_format)

    # Create console handler to display logs.
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    logger.addHandler(console_handler)

    # Read config file.
    parser = configparser.ConfigParser()
    parser.read('config.ini')

    # Create file handler to save logs (if defined).
    log_file = parser.get('MISC', 'log_file')
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(log_formatter)
        logger.addHandler(file_handler)
        logger.info('Logging to log file: ' + log_file)
    else:
        logger.info('No log file specified.')

    # Rename and organise directories.
    root_dir = parser.get('MISC', 'root_directory')
    organise_by_year_and_rename(root_dir)


def organise_by_year_and_rename(root_dir):
    """Organises subdirectories found in root folder, and renames them.

    Searches for subdirectories whose names start in the format 'yymmdd', and
    moves them to a folder corresponding to their year 'YYYY', renaming them
    to start 'YYYY-mm-dd'.

    e.g. would organise and rename a directory in the root directory named:
        '161225 - Christmas Day' to:
        '2016/2016-12-25 - Christmas Day'

    Args:
        root_dir: The root directory whose subdirectories are to be organised
                  and renamed.

    Raises:
        StopIteration: If specified root directory not found.
    """
    logger = logging.getLogger()
    logger.info("\n---\nChecking directories in: '" + root_dir + "'\n---")

    try:
        # Get all subdirectories in the root directory.
        _, dir_list, _ = next(os.walk(root_dir))
    except StopIteration as exc:
        logger.critical("Root directory not found: " + root_dir + str(exc))
        raise

    # Define pattern for expected date prefix, e.g. 161225 (for 25/12/2016).
    date_prefix_length = 6
    date_re_pattern = re.compile(
        r"^\d{" + re.escape(str(date_prefix_length)) + r"}"
    )

    for dir_ in dir_list:
        # Get dir name prefix (potential date string).
        dir_prefix = dir_[:date_prefix_length]

        # Only continue if directory name starts with (6) digits.
        if re.match(date_re_pattern, dir_prefix):
            try:
                old_date = datetime.strptime(dir_prefix, "%y%m%d")
            except ValueError as exc:
                logger.warning(
                    "Skipping folder '" + dir_ +
                    "' as it does not start in format 'yymmdd'. "
                    "Exception details: " + str(exc)
                )
            else:
                dir_suffix = dir_[date_prefix_length:]
                new_dir_name = old_date.strftime("%Y-%m-%d") + dir_suffix

                dir_year = old_date.strftime('%Y')
                new_path = os.path.join(root_dir, dir_year, new_dir_name)
                old_path = os.path.join(root_dir, dir_)

                # Move to new path/name, creating missing dirs along the way.
                logger.info("Moving '" + old_path + "' to '" + new_path + "'")
                os.renames(old_path, new_path)


if __name__ == '__main__':
    main()
