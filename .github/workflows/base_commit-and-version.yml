name: Get Base Commit and Version

on:
  push:
    types: [opened, synchronize, reopened, edited]
  pull_request:
    types: [opened, synchronize, reopened, edited]

jobs:
  get-base-commit:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      - name: Get base commit and version
        run: |
          base_commit=$(git rev-parse HEAD)
          version=$(echo "$base_commit" | cut -c1-7)
          echo "base_commit=$base_commit" >> $GITHUB_ENV
          echo "version=$version" >> $GITHUB_ENV

      - name: Display Base Commit and Version
        run: |
          echo "Base Commit: ${{ env.base_commit }}"
          echo "Version: ${{ env.version }}"
