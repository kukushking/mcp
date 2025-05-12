"""AWS SDK for pandas MCP Glue Data Catalog Tools."""

import logging
from typing import List

import awswrangler as wr
from awslabs.aws_sdk_pandas_mcp_server.tools.utils import format_pandas

logger = logging.getLogger(__name__)


def s3_read_parquet(
    path: str,
) -> str:
    """Read Parquet file(s) from an S3 prefix or list of S3 objects paths.

    Args:s
        path:
            S3 prefix (accepts Unix shell-style wildcards)
            (e.g. s3://bucket/prefix) or list of S3 objects paths (e.g. [s3://bucket/key0, s3://bucket/key1]).
    Returns:
        Results table
    """

    logger.info(f'Reading parquet file(s) from S3 path: {path}')

    df = wr.s3.read_parquet(
        path=path,
    )

    return format_pandas(df)
