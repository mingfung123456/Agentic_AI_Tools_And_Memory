Here’s a **shorter, macOS-focused version** of the full guide (optimized for Terminal on macOS in 2026).

```markdown
# Quick Guide: Multiple GitHub Accounts with SSH on macOS

**Goal**: Use separate SSH keys per GitHub account → no credential prompts, no token leaks.

### 1. Generate one SSH key per account (use ed25519)
Open Terminal and run for each account (change email & filename):

```bash
# Personal account example
ssh-keygen -t ed25519 -C "your.personal@gmail.com" -f ~/.ssh/id_ed25519_personal

# Work account example
ssh-keygen -t ed25519 -C "your.work@company.com" -f ~/.ssh/id_ed25519_work
```

- Press Enter → set a passphrase (recommended for security)
- Keys saved in `~/.ssh/`

### 2. Copy & add public key to GitHub
For each key:

```bash
# Copy to clipboard
pbcopy < ~/.ssh/id_ed25519_personal.pub
```

Then:
- Log into the matching GitHub account
- Settings → SSH and GPG keys → **New SSH key**
- Title: e.g. "MacBook Personal 2026"
- Paste the key (starts with `ssh-ed25519 AAAAC3...`)
- Add SSH key

Repeat for every account.

### 3. Create SSH config (~/.ssh/config)
```bash
# Open (or create) the file
nano ~/.ssh/config
```

Paste & adapt (use your filenames):

```text
Host github-personal
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_personal
    IdentitiesOnly yes

Host github-work
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_work
    IdentitiesOnly yes
```

Save (Ctrl+O → Enter → Ctrl+X in nano).

Fix permissions:
```bash
chmod 600 ~/.ssh/config
chmod 600 ~/.ssh/id_ed25519_*
```

### 4. Test it works
```bash
ssh -T git@github-personal    # → Hi yourusername! You've successfully authenticated...
ssh -T git@github-work
```

### 5. Clone / use repos with the alias
```bash
# Personal
git clone git@github-personal:yourusername/my-repo.git

# Work (or change existing remote)
git remote set-url origin git@github-work:company/repo.git
```

### 6. Set correct git identity per repo (do this inside each repo folder!)
```bash
# Personal repo
git config user.name "Fung Personal"
git config user.email "your.personal@gmail.com"

# Work repo
git config user.name "Fung Work"
git config user.email "your.work@company.com"
```

**Done!**  
- No more PATs in code  
- Automatic key selection via aliases  
- Commits go to the right account  

If test fails (Step 4), paste the error here. Enjoy clean multi-account workflow on your Mac! 🚀
```

This version is ~50% shorter, macOS-specific (pbcopy, nano, chmod), and keeps only the essentials while still being complete. Save it as `multi-github-ssh-mac.md` if you like. Let me know if you want it even shorter or with screenshots!