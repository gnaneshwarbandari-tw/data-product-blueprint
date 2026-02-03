# Data Product Blueprint

A Cookiecutter/Cruft template for creating standardized data product repositories with automated validation and registration workflows.

## Prerequisites

Install Cruft (recommended) or Cookiecutter:

```bash
# Using pip
pip install cruft

# Or using pipx (recommended)
pipx install cruft

# Alternative: Using cookiecutter
pip install cookiecutter
```

## Quick Start

### 1. Create a New Data Product

```bash
# Using cruft (recommended - supports template updates)
cruft create https://github.com/gnaneshwarbandari-tw/data-product-blueprint.git

# Or using cookiecutter
cookiecutter https://github.com/gnaneshwarbandari-tw/data-product-blueprint.git
```

### 2. Provide User Inputs

You'll be prompted to provide the following information:

| Input | Description | Example |
|-------|-------------|---------|
| `project_name` | Name of your data product | "Customer Orders Data Product" |
| `domain` | Business domain | "orders" |
| `team_name` | Owning team name | "Data Platform Team" |
| `owner_name` | Product owner's name | "John Doe" |
| `owner_email` | Product owner's email | "john.doe@company.com" |
| `support_email` | Support contact email | "data-support@company.com" |
| `teams_channel_url` | Microsoft Teams channel URL | "https://teams.microsoft.com/..." |
| `purpose_description` | What this data product does | "Provides order data for analytics" |
| `usage_description` | How to use this data product | "Order analysis and reporting" |
| `input_port_name` | Name of the input data source | "orders-kafka-stream" |
| `input_type` | Type of input (stream/batch) | "stream" |
| `output_port_name` | Name of the output destination | "orders-bigquery-table" |

**Note:** The `project_slug` (folder name) is automatically generated from `project_name` by converting to lowercase and replacing spaces with underscores.

### 3. Initialize Git and Push

```bash
cd <your_project_slug>
git init
git add .
git commit -m "Initial commit: Add data product specification"

# Create a new repository on GitHub and push
git remote add origin <your-repo-url>
git branch -M main
git push -u origin main
```

### 4. Automated Registration

Once pushed to GitHub:
- The GitHub Actions workflow automatically triggers
- Validates the data product YAML structure
- Registers the data product via API (currently mock)

## Template Structure

```
data-product-blueprint/
├── cookiecutter.json                     # Template configuration
├── .github/
│   └── workflows/
│       └── validate.yaml                 # GitHub Actions workflow (copied to repo root)
└── {{ cookiecutter.__project_slug }}/    # Generated project folder
    ├── README.md                         # Project documentation
    ├── .cruft.json                       # Cruft metadata (for updates)
    └── data-product/
        └── data-product.yaml             # Data product specification
```

### Generated Repository Structure

After creation, your repository will have:

```
your-repo/
├── .github/
│   └── workflows/
│       └── validate.yaml                 # Workflow at repo root
└── <project_slug>/                       # Your data product folder
    ├── README.md
    ├── .cruft.json
    └── data-product/
        └── data-product.yaml
```

## Configuration Reference

### cookiecutter.json

The template is configured via `cookiecutter.json`:

```json
{
  "_copy_without_render": [".github/*"],  // Files copied without templating
  "project_name": "...",                   // User input: project name
  "domain": "...",                         // User input: business domain
  // ... other user inputs ...
  "__project_slug": "{{ ... }}"           // Auto-generated from project_name
}
```

**Key features:**
- `_copy_without_render`: Prevents Jinja2 from processing GitHub Actions syntax (`${{ }}`)
- `__project_slug`: Private computed variable (prefix with `__` to hide from prompts)
- All other fields are prompted during project creation

### Data Product Specification

The `data-product.yaml` file follows this structure:

```yaml
apiVersion: v1.0
kind: DataProduct
name: {{ cookiecutter.project_name }}
domain: {{ cookiecutter.domain }}
team:
  name: {{ cookiecutter.team_name }}
  members:
    - username: {{ cookiecutter.owner_email }}
      name: {{ cookiecutter.owner_name }}
      role: owner
inputPorts:
  name: {{ cookiecutter.input_port_name }}
  type: {{ cookiecutter.input_type[0] }}
outputPorts:
  name: {{ cookiecutter.output_port_name }}
# ... additional fields
```

## GitHub Actions Workflow

The workflow (`.github/workflows/validate.yaml`) automatically:

1. **Triggers** on push/PR to main branch
2. **Checks out** the repository
3. **Installs** Python and dependencies (PyYAML, jsonschema)
4. **Finds** the data product YAML file dynamically
5. **Converts** YAML to JSON
6. **Registers** the data product (currently mock API call)

### Customizing the Workflow

To connect to a real API, update the workflow:

```yaml
- name: Register Data Product via API
  run: |
    curl -X POST "https://your-api.com/register" \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer ${{ secrets.API_TOKEN }}" \
      -d "$DATA_PRODUCT_JSON"
```

Add secrets in GitHub repository settings: **Settings → Secrets and variables → Actions**

## Updating Existing Projects

If you used `cruft` to create your project, you can update it when the template changes:

```bash
cd <your_project_slug>
cruft update
```

This will pull the latest template changes while preserving your customizations.

## Development

### Testing the Template Locally

```bash
# Test with default values
cruft create . --no-input

# Test with custom values
cruft create .
```

### Modifying the Template

1. Update files in `{{ cookiecutter.__project_slug }}/`
2. Update `cookiecutter.json` for new variables
3. Update `.github/workflows/validate.yaml` for workflow changes
4. Commit and push changes
5. Test with `cruft create` from the repository URL

## Troubleshooting

### Issue: Workflow not triggering
- Ensure `.github/workflows/` exists at repository root (not inside the data product folder)
- Check GitHub Actions is enabled in repository settings

### Issue: YAML validation fails
- Verify `data-product.yaml` has valid YAML syntax
- Ensure required fields are present

### Issue: Project slug is wrong
- The `__project_slug` is auto-generated from `project_name`
- Manually rename the folder if needed after creation

## License

[Add your license here]

## Contributing

[Add contribution guidelines here]
