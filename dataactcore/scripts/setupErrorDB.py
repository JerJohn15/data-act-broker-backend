from dataactcore.models import errorModels
from dataactcore.models.errorModels import Status, ErrorType
from dataactcore.models.errorInterface import ErrorInterface
from dataactcore.scripts.databaseSetup import createDatabase
from dataactcore.config import CONFIG_DB


def setupErrorDB(hardReset = False):
    """Create job tracker tables from model metadata."""
    createDatabase(CONFIG_DB['error_db_name'])
    errorDb = ErrorInterface()
    if hardReset:
        errorModels.Base.metadata.drop_all(errorDb.engine)
    errorModels.Base.metadata.create_all(errorDb.engine)

    errorDb.session.commit()
    errorDb.session.close()

    # TODO: define these codes as enums in the data model?
    # insert status types
    statusList = [(1, 'complete', 'File has been processed'),
        (2, 'header_error', 'The file has errors in the header row'),
        (3, 'unknown_error', 'An unknown error has occurred with this file'),
        (4, 'single_row_error', 'CSV file must have a header row and at least one record'),
        (5, 'job_error', 'Error occurred in job manager')]
    for s in statusList:
        status = Status(status_id=s[0], name=s[1], description=s[2])
        errorDb.session.merge(status)

    # insert error types
    errorList = [(1, 'type_error', 'The value provided was of the wrong type'),
        (2, 'required_error', 'A required value was not provided'),
        (3, 'value_error', 'The value provided was invalid'),
        (4, 'read_error', 'Could not parse this record correctly'),
        (5, 'write_error', 'Could not write this record into the staging database')]
    for e in errorList:
        error = ErrorType(error_type_id=e[0], name=e[1], description=e[2])
        errorDb.session.merge(error)

    errorDb.session.commit()
    errorDb.session.close()

if __name__ == '__main__':
    setupErrorDB(True)
