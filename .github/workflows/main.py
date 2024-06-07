# .github/workflows/pr-analysis.yml
name: Analyze Pull Request

on:
  push:
    types: [opened, synchronize, reopened, edited]
  pull_request:
    types: [opened, synchronize, reopened, edited]
    # branches:
    #   - branch1

jobs:
  analyze:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'

    - name: Install dependencies
      run: 
        python -m pip install --upgrade pip
        pip install requests

    - name: Get base commit and version
      run: |
        base_commit=$(git rev-parse HEAD)
        version=$(echo "$base_commit" | cut -c1-7)
        echo "base_commit=$base_commit" >> $GITHUB_ENV
        echo "version=$version" >> $GITHUB_ENV
        
    - name: Run analysis script
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        PR_NUMBER: ${{ github.event.pull_request.number }}
        GITHUB_REPOSITORY: ${{ github.repository }}
        BASE_COMMIT: ${{ env.base_commit }}
        VERSION: ${{ env.version }}
      run: python scripts/analyze_pr.py
