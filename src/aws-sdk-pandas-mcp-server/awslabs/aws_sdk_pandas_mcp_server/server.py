"""AWS SDK for pandas (awswrangler) MCP Server implementation."""

import argparse
import boto3
import logging
import os

from mcp.server.fastmcp import FastMCP
from awslabs.aws_sdk_pandas_mcp_server.tools import (
    athena_read_sql_query,
    athena_read_sql_table,
    get_table,
    get_table_location,
    list_databases,
    list_tables,
    s3_read_parquet,
)

logger = logging.getLogger(__name__)


# Get AWS profile and region
AWS_PROFILE = os.environ.get('AWS_PROFILE', 'default')
logger.info(f'AWS_PROFILE: {AWS_PROFILE}')

AWS_REGION = os.environ.get('AWS_REGION', 'us-east-1')
logger.info(f'AWS_REGION: {AWS_REGION}')

# Create boto3 session
boto3_session = boto3.Session(profile_name=AWS_PROFILE, region_name=AWS_REGION)


mcp = FastMCP(
    name='awslabs.aws-sdk-pandas-mcp-server',
    version='0.1.0',
    description='AWS SDK for Pandas (awswrangler) MCP Server',
)


# Tools
mcp.tool(name='list_tables')(list_tables)
mcp.tool(name='list_databases')(list_databases)
mcp.tool(name='get_table')(get_table)
mcp.tool(name='get_table_location')(get_table_location)
mcp.tool(name='athena_execute_sql_query')(athena_read_sql_query)
mcp.tool(name='athena_read_sql_table')(athena_read_sql_table)
mcp.tool(name='s3_read_parquet')(s3_read_parquet)

# Resources
mcp.resource(uri='glue://catalog/{catalog_id}/databases')(list_databases)
mcp.resource(uri='glue://catalog/{catalog_id}/database/{database}/tables')(list_tables)
mcp.resource(uri='glue://catalog/{catalog_id}/database/{database}/table/{table}')(get_table)


def main():
    """Run the MCP server with CLI argument support."""
    parser = argparse.ArgumentParser(
        description='An AWS Model Context Protocol (MCP) server for AWS SDK for pandas'
    )
    parser.add_argument('--port', type=int, default=None, help='Port to run the server on')

    args = parser.parse_args()

    if args.port:
        mcp.settings.port = args.port

    mcp.run()


if __name__ == '__main__':
    main()
