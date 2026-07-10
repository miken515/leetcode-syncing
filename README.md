# Leetcode Syncing

This repository automates the synchronization of Leetcode problems to a local folder using GitHub Actions.

## Features

- Automatically syncs Leetcode problems daily at 8:00 AM UTC.
- Supports manual workflow dispatch for on-demand syncing.
- Stores problems in a specified destination folder.
- Customizable commit messages for synced problems.

## Setup

1. **Fork this repository** to your GitHub account.
2. **Add the required secrets** to your repository:
   - `LEETCODE_CSRF_TOKEN`: Your Leetcode CSRF token.
   - `LEETCODE_SESSION`: Your Leetcode session token.
3. **Modify the destination folder** in the workflow file if needed:
   - Edit `.github/workflows/sync-leetcode.yml` and update the `destination-folder` field.

## Usage

- The workflow runs automatically every day at 8:00 AM UTC.
- To trigger the workflow manually:
  1. Go to the "Actions" tab in your repository.
  2. Select the "Sync Leetcode" workflow.
  3. Click "Run workflow."

## Notes

- Ensure your Leetcode session token and CSRF token are valid.
- The synced problems will be stored in the specified destination folder.