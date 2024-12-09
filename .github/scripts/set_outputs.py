import sys
import os
env = sys.argv[1]
with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
    print(f"environment={env}", file=fh)
#     print(f"account_number_secret={env.upper()}_ACCOUNT_NUMBER", file=fh)
