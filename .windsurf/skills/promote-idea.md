---
name: promote-idea
description: Promote IdeaForge idea to production repository with full control plane integration
activation: manual
---

# Promote Idea Skill

## Purpose

Automate the promotion of IdeaForge ideas to production repositories with complete control plane integration.

## When to Use

Say any of:
- "Promote [idea-name] from IdeaForge"
- "Create repo for [idea-name]"
- "Turn [idea-name] into a real project"
- "Implement [idea-name] from IdeaForge"

## What This Does

**Fully automated workflow:**

1. ✅ Extract idea details from IdeaForge
2. ✅ Create GitHub repository
3. ✅ Initialize with control plane submodule
4. ✅ Set up Windsurf automation (auto-deploy, testing)
5. ✅ Initialize development environment
6. ✅ Create testing infrastructure
7. ✅ Update control plane documentation
8. ✅ Deploy infrastructure (if needed)
9. ✅ Verify everything works
10. ✅ Update IdeaForge idea as "Promoted"

## Process

### 1. Extract from IdeaForge

```
Read: ~/Projects/IdeaForge/ideas/[idea-name].md

Extract:
- Name
- Description
- Tech stack
- Type (web app, API, CLI, library)
- Deployment needs
- Port (if applicable)
```

### 2. Create Repository

```bash
# Create on GitHub via API or manual
# Clone locally
# Initialize with README
# Push to GitHub
```

### 3. Integrate Control Plane

```bash
# Add Cloudy-Work submodule
git submodule add git@github.com:heybearc/Cloudy-Work.git .cloudy-work

# Copy Windsurf automation
cp -r ~/Projects/Cloudy-Work/.windsurf/ .windsurf/

# Commit and push
```

### 4. Initialize Development

Based on project type:

**Web App (Next.js):**
```bash
npm init -y
npm install next@14 react react-dom
npm install -D typescript @playwright/test
# Create app/, tests/, etc.
```

**Python Project:**
```bash
python -m venv venv
pip install -r requirements.txt
# Create src/, tests/, etc.
```

**CLI Tool:**
```bash
# Initialize based on language
# Set up entry point
# Configure build
```

### 5. Set Up Testing

```bash
# Create playwright.config.ts
# Create tests/smoke-test.spec.ts
# Configure .env.test template
```

### 6. Update Control Plane

```bash
cd ~/Projects/Cloudy-Work

# Update APP-MAP.md
# Update inventory.md
# Commit and push
```

### 7. Deploy Infrastructure

**If web app:**
- Create blue-green LXC containers
- Deploy to STANDBY
- Configure HAProxy
- Set up PM2

**If local-only:**
- Skip infrastructure
- Ready for local development

### 8. Verify

```bash
# Test auto-deploy
touch .debugging
# Make change, verify deployment

# Run smoke tests
npm run test:smoke:quick

# Verify control plane integration
```

### 9. Update IdeaForge

```bash
cd ~/Projects/IdeaForge

# Update idea file
# Add "Status: Promoted on [date]"
# Add link to new repo
# Commit and push
```

## Example Interaction

```
You: "Promote passive-income-tracker from IdeaForge"

Windsurf:
🔍 Reading IdeaForge idea file...
✅ Found: passive-income-tracker
   Type: Next.js web application
   Deployment: Blue-green containers
   Port: 3001

📦 Creating GitHub repository...
✅ Repository created: heybearc/passive-income-tracker

🔧 Initializing with control plane...
✅ Cloudy-Work submodule added
✅ Windsurf automation configured
✅ Auto-deploy enabled
✅ Test generation enabled

💻 Setting up development environment...
✅ Next.js 14 initialized
✅ TypeScript configured
✅ Playwright tests created
✅ Smoke tests ready

📋 Updating control plane...
✅ Added to APP-MAP.md
✅ Added to inventory.md
✅ Control plane updated

🚀 Deploying infrastructure...
✅ Created LXC containers (blue/green)
✅ Deployed to STANDBY
✅ HAProxy configured
✅ PM2 configured

🧪 Verifying...
✅ Auto-deploy working
✅ Smoke tests passing (3/3)
✅ Application accessible

📝 Updating IdeaForge...
✅ Marked as promoted

🎉 Promotion complete!

New repository: https://github.com/heybearc/passive-income-tracker
STANDBY URL: https://blue.passive-income-tracker.com
Ready for development!
```

## Project Types

### Web Application
- Creates blue-green containers
- Configures HAProxy
- Sets up PM2
- Port 3001
- Full auto-deploy + testing

### API Service
- Creates blue-green containers
- Configures HAProxy
- Sets up PM2
- Port 3001
- Full auto-deploy + testing

### CLI Tool
- Local development only
- No containers
- Package for distribution
- Unit tests only

### Library/Package
- Local development only
- No containers
- Publish to npm/PyPI
- Unit tests only

### Background Job
- Single container or local
- Cron or systemd
- Monitoring setup
- Unit tests

## Infrastructure Decisions

**Needs containers if:**
- Web application (user-facing)
- API service (external access)
- Long-running service
- Needs high availability

**Local-only if:**
- CLI tool
- Library/package
- Development tool
- Personal utility

## Benefits

**Automated setup:**
- No manual repo creation
- No manual configuration
- Consistent structure
- Best practices enforced

**Control plane integration:**
- Governance from day one
- Standard workflows
- Auto-deploy enabled
- Testing infrastructure ready

**Fast start:**
- Minutes, not hours
- Ready for development immediately
- Infrastructure deployed
- Tests passing

**Consistency:**
- Same structure as other apps
- Same automation
- Same testing approach
- Same deployment process

## Notes

- Always review IdeaForge idea first
- Confirm tech stack and deployment needs
- Verify infrastructure requirements
- Test thoroughly before marking complete
- Update both control plane and IdeaForge
