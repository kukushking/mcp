# AWS SDK for pandas (awswrangler) MCP Server

A Model Context Protocol (MCP) server that provides a bridge between MCP clients and AWS SDK for pandas (awswrangler), enabling AI assistants to perform data operations on AWS services using pandas DataFrames.

## Features

- Query and analyze data from Amazon S3, Amazon Athena, AWS Glue, Amazon Redshift, and other AWS data services
- Load and save pandas DataFrames to/from AWS services
- Perform ETL operations using pandas with AWS services
- Generate visualizations and insights from AWS data sources
- Follow AWS data best practices for efficient data operations

## Installation

1. Install `uv` from [Astral](https://docs.astral.sh/uv/getting-started/installation/)
2. Install Python using `uv python install 3.10`
3. Install the AWS SDK for pandas MCP Server:
   ```
   uvx awslabs.aws-sdk-pandas-mcp-server@latest
   ```

## Configuration

Add the AWS SDK for pandas MCP Server to your MCP client configuration:

```json
{
  "mcpServers": {
    "awslabs.aws-sdk-pandas-mcp-server": {
      "command": "uvx",
      "args": ["awslabs.aws-sdk-pandas-mcp-server@latest"],
      "env": {
        "AWS_PROFILE": "your-aws-profile",
        "AWS_REGION": "us-east-1",
        "FASTMCP_LOG_LEVEL": "ERROR"
      }
    }
  }
}
```

## Usage Examples

### Query data using Amazon Athena

```python
# Execute Athena query and get results as pandas DataFrame
df = wr.athena.read_sql_query(
    "SELECT * FROM my_database.my_table LIMIT 10",
    database="my_database"
)
```

## Documentation

For more information about AWS SDK for pandas (awswrangler), visit the [official documentation](https://aws-sdk-pandas.readthedocs.io/).
