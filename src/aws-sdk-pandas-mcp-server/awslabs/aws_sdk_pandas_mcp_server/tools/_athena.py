"""AWS SDK for pandas MCP Athena Tools."""

import logging

import awswrangler as wr
from awslabs.aws_sdk_pandas_mcp_server.tools.utils import format_pandas

logger = logging.getLogger(__name__)


def athena_read_sql_query(
    sql: str,
    database: str,
    workgroup: str | None = 'primary',
) -> str:
    """Execute an SQL query using AWS Athena.

    Args:
        sql: SQL query.
        database: Glue Data Catalog database name.
        workgroup: Athena workgroup. `primary` by default.
        boto3_session: boto3 Session object.

    Returns:
        Results table
    """

    logger.info(f'Executing Athena SQL query: {sql}')
    logger.info(f'Database: {database}')

    df = wr.athena.read_sql_query(
        sql=sql,
        database=database,
        workgroup=workgroup,
        ctas_approach=False,  # Execute queries directly (not CTAS)
    )

    return format_pandas(df)


def athena_read_sql_table(
    database: str,
    table: str,
    workgroup: str | None = 'primary',
) -> str:
    """Read an SQL table using AWS Athena.

    Args:
        database: Glue Data Catalog database name.
        table: Glue Data Catalog table name.
        workgroup: Athena workgroup. `primary` by default.
        boto3_session: boto3 Session object.

    Returns:
        Results table
    """

    logger.info(f'Database: {database}')
    logger.info(f'Table: {table}')

    df = wr.athena.read_sql_table(
        database=database,
        table=table,
        workgroup=workgroup,
        ctas_approach=False,  # Execute queries directly (not CTAS)
    )

    return format_pandas(df)
