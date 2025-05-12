"""AWS SDK for pandas MCP Glue Data Catalog Tools."""

import logging

import awswrangler as wr
from awslabs.aws_sdk_pandas_mcp_server.tools.utils import format_pandas

logger = logging.getLogger(__name__)


def list_databases(
    catalog_id: str | None = None,
) -> str:
    """List databases in Glue Data Catalog.

    Args:s
        catalog_id: The ID of the Data Catalog from which to retrieve Databases. If none is provided, the AWS account ID is used by default.

    Returns:
        Results table
    """

    logger.info(f'Listing databases in catalog {catalog_id}')

    df = wr.catalog.databases(
        catalog_id=catalog_id,
    )

    return format_pandas(df)


def list_tables(
    catalog_id: str | None = None,
    database: str | None = None,
) -> str:
    """List tables in Glue Data Catalog.

    Args:s
        catalog_id: The ID of the Data Catalog from which to retrieve Databases. If none is provided, the AWS account ID is used by default.
        database: Glue Data Catalog database name.

    Returns:
        Results table
    """

    logger.info(f'Listing tables in catalog {catalog_id}, and database {database}')

    df = wr.catalog.tables(
        catalog_id=catalog_id,
        database=database,
    )

    return format_pandas(df)


def get_table(
    catalog_id: str | None = None,
    database: str | None = None,
    table: str | None = None,
) -> str:
    """Get table details from Glue Data Catalog.

    Args:s
        catalog_id: The ID of the Data Catalog from which to retrieve Databases. If none is provided, the AWS account ID is used by default.
        database: Glue Data Catalog database name.
        table: Glue Data Catalog table name.

    Returns:
        Results table
    """

    logger.info(f'Getting table from catalog {catalog_id}, and database {database}, table {table}')

    df = wr.catalog.table(
        catalog_id=catalog_id,
        database=database,
        table=table,
    )

    return format_pandas(df)


def get_table_location(
    catalog_id: str | None = None,
    database: str | None = None,
    table: str | None = None,
) -> str:
    """Get table details from Glue Data Catalog.

    Args:s
        catalog_id: The ID of the Data Catalog from which to retrieve Databases. If none is provided, the AWS account ID is used by default.
        database: Glue Data Catalog database name.
        table: Glue Data Catalog table name.

    Returns:
        Results table
    """

    logger.info(f'Getting table from catalog {catalog_id}, and database {database}, table {table}')

    return wr.catalog.get_table_location(
        catalog_id=catalog_id,
        database=database,
        table=table,
    )
