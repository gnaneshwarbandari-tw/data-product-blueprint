# {{ cookiecutter.project_name }}

Data Product for {{ cookiecutter.domain }} domain managed by {{ cookiecutter.team_name }}.

## Overview

**Purpose:** {{ cookiecutter.purpose_description }}

**Usage:** {{ cookiecutter.usage_description }}

**Owner:** {{ cookiecutter.owner_name }} ({{ cookiecutter.owner_email }})

## Data Product Details

### Input Ports
- **Name:** {{ cookiecutter.input_port_name }}
- **Type:** {{ cookiecutter.input_type[0] }}

### Output Ports
- **Name:** {{ cookiecutter.output_port_name }}

## Support

- **Teams Channel:** {{ cookiecutter.teams_channel_url }}
- **Email:** {{ cookiecutter.support_email }}

## Making Changes

1. Update the data product specification in `data-product/data-product.yaml`
2. Commit and push changes to trigger validation
3. The GitHub Actions workflow will automatically validate and register the data product

## Workflow

The repository includes a GitHub Actions workflow that:
- Automatically triggers on push/PR to main branch
- Validates the data product YAML structure
- Sends the data product specification to the registration API
- Currently configured as a mock registration for demonstration

To enable actual registration, update the API endpoint in `.github/workflows/validate.yaml`.