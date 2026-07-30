#!/bin/bash

# AIKYA Git Hook Installer
# Installs a pre-push hook to enforce the defined "Ways of Working".

REPO_ROOT=$(git rev-parse --show-toplevel)
HOOK_PATH="$REPO_ROOT/.git/hooks/pre-push"

echo "Installing AIKYA pre-push guardrail..."

cat > "$HOOK_PATH" << 'EOF'
#!/bin/bash

# AIKYA Pre-Push Guardrail
# Enforces branching strategy:
# 1. No direct pushes to 'main'.
# 2. Branch names must follow conventions (feature/, hotfix/, bugfix/, chore/, docs/, refactor/, infra/).

remote="$1"
url="$2"

z40="0000000000000000000000000000000000000000"

while read local_ref local_sha remote_ref remote_sha
do
    if [ "$local_sha" = $z40 ]; then
        # Delete remote branch, always allowed
        continue
    fi

    # Extract branch name
    branch_name=$(echo "$local_ref" | sed 's#refs/heads/##')

    # Guardrail 1: No direct pushes to main
    if [ "$branch_name" = "main" ]; then
        echo " [ERROR] Direct push to 'main' is disallowed by AIKYA 'Ways of Working'."
        echo "         Please push to 'staging' or a feature branch and create a PR."
        exit 1
    fi

    # Guardrail 2: Branch naming convention
    if [[ ! "$branch_name" =~ ^(feature/|hotfix/|bugfix/|chore/|docs/|refactor/|infra/|staging|demo) ]]; then
        echo " [ERROR] Invalid branch name: '$branch_name'"
        echo "         Branches must follow the AIKYA naming convention:"
        echo "         - feature/*"
        echo "         - hotfix/*"
        echo "         - bugfix/*"
        echo "         - chore/*"
        echo "         - docs/*"
        echo "         - refactor/*"
        echo "         - infra/*"
        echo "         (Use --no-verify to bypass if absolutely necessary)"
        exit 1
    fi
done

exit 0
EOF

chmod +x "$HOOK_PATH"
echo "Success: Pre-push guardrail installed at $HOOK_PATH"
