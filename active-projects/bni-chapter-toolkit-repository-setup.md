# BNI Chapter Toolkit - Repository Setup Guide

**Project:** BNI Chapter Toolkit  
**Date:** 2026-01-29  
**Purpose:** Complete guide to initialize the project repository and development environment

---

## 📁 Repository Structure

```
bni-chapter-toolkit/
├── .github/
│   ├── workflows/
│   │   ├── ci.yml                    # CI/CD pipeline
│   │   └── deploy.yml                # Deployment workflow
│   └── ISSUE_TEMPLATE/
│       ├── bug_report.md
│       └── feature_request.md
├── prisma/
│   ├── schema.prisma                 # Database schema
│   ├── migrations/                   # Database migrations
│   └── seed.ts                       # Seed data for development
├── public/
│   ├── images/
│   │   ├── logo.png
│   │   └── placeholder-avatar.png
│   └── favicon.ico
├── src/
│   ├── app/                          # Next.js App Router
│   │   ├── (public)/                 # Public routes (no auth)
│   │   │   ├── c/
│   │   │   │   └── [slug]/
│   │   │   │       └── page.tsx      # Member directory
│   │   │   └── checkin/
│   │   │       └── [slug]/
│   │   │           └── page.tsx      # Visitor check-in
│   │   ├── (auth)/                   # Protected routes
│   │   │   └── admin/
│   │   │       ├── dashboard/
│   │   │       │   └── page.tsx
│   │   │       ├── members/
│   │   │       │   ├── page.tsx
│   │   │       │   └── [id]/
│   │   │       │       └── page.tsx
│   │   │       ├── visitors/
│   │   │       │   ├── page.tsx
│   │   │       │   └── [id]/
│   │   │       │       └── page.tsx
│   │   │       ├── qrcode/
│   │   │       │   └── page.tsx
│   │   │       ├── settings/
│   │   │       │   └── page.tsx
│   │   │       └── analytics/
│   │   │           └── page.tsx
│   │   ├── api/
│   │   │   ├── admin/
│   │   │   │   ├── member/
│   │   │   │   │   └── route.ts
│   │   │   │   ├── visitor/
│   │   │   │   │   └── route.ts
│   │   │   │   └── analytics/
│   │   │   │       └── route.ts
│   │   │   ├── visitor/
│   │   │   │   └── checkin/
│   │   │   │       └── route.ts
│   │   │   ├── billing/
│   │   │   │   ├── checkout/
│   │   │   │   │   └── route.ts
│   │   │   │   └── webhook/
│   │   │   │       └── route.ts
│   │   │   └── upload/
│   │   │       └── route.ts
│   │   ├── layout.tsx                # Root layout
│   │   ├── page.tsx                  # Landing page
│   │   └── globals.css               # Global styles
│   ├── components/
│   │   ├── ui/                       # shadcn/ui components
│   │   │   ├── button.tsx
│   │   │   ├── card.tsx
│   │   │   ├── form.tsx
│   │   │   ├── input.tsx
│   │   │   ├── table.tsx
│   │   │   └── ...
│   │   ├── directory/
│   │   │   ├── member-card.tsx
│   │   │   ├── member-grid.tsx
│   │   │   ├── filter-bar.tsx
│   │   │   └── share-button.tsx
│   │   ├── checkin/
│   │   │   ├── checkin-form.tsx
│   │   │   ├── camera-capture.tsx
│   │   │   └── confirmation.tsx
│   │   ├── admin/
│   │   │   ├── sidebar.tsx
│   │   │   ├── stats-card.tsx
│   │   │   ├── member-table.tsx
│   │   │   ├── visitor-table.tsx
│   │   │   └── qr-generator.tsx
│   │   └── shared/
│   │       ├── header.tsx
│   │       ├── footer.tsx
│   │       └── loading.tsx
│   ├── lib/
│   │   ├── db.ts                     # Prisma client
│   │   ├── auth.ts                   # Auth helpers
│   │   ├── cloudinary.ts             # Image upload
│   │   ├── qrcode.ts                 # QR code generation
│   │   ├── email.ts                  # Email notifications
│   │   ├── analytics.ts              # Analytics tracking
│   │   └── utils.ts                  # Utility functions
│   ├── types/
│   │   ├── chapter.ts
│   │   ├── member.ts
│   │   ├── visitor.ts
│   │   └── index.ts
│   └── schemas/
│       ├── member.ts                 # Zod schemas
│       ├── visitor.ts
│       └── chapter.ts
├── .env.example                      # Environment variables template
├── .env.local                        # Local environment (gitignored)
├── .eslintrc.json                    # ESLint config
├── .gitignore
├── .prettierrc                       # Prettier config
├── components.json                   # shadcn/ui config
├── next.config.js                    # Next.js config
├── package.json
├── postcss.config.js
├── README.md
├── tailwind.config.ts
└── tsconfig.json
```

---

## 🚀 Initial Setup Commands

### 1. Create Next.js Project

```bash
# Navigate to projects directory
cd ~/Projects

# Create new Next.js project
npx create-next-app@latest bni-chapter-toolkit \
  --typescript \
  --tailwind \
  --app \
  --src-dir \
  --import-alias "@/*" \
  --use-npm

# Navigate into project
cd bni-chapter-toolkit
```

### 2. Install Core Dependencies

```bash
# Database & ORM
npm install @prisma/client
npm install -D prisma

# Authentication (choose one)
npm install @clerk/nextjs
# OR
npm install next-auth @auth/prisma-adapter

# Forms & Validation
npm install react-hook-form @hookform/resolvers zod

# UI Components
npm install lucide-react class-variance-authority clsx tailwind-merge

# Image Upload
npm install cloudinary

# QR Code Generation
npm install qrcode
npm install -D @types/qrcode

# Date Handling
npm install date-fns

# Email
npm install nodemailer
npm install -D @types/nodemailer

# Payments (Phase 3)
# npm install stripe @stripe/stripe-js
```

### 3. Install shadcn/ui

```bash
# Initialize shadcn/ui
npx shadcn-ui@latest init

# Install required components
npx shadcn-ui@latest add button
npx shadcn-ui@latest add card
npx shadcn-ui@latest add input
npx shadcn-ui@latest add label
npx shadcn-ui@latest add form
npx shadcn-ui@latest add table
npx shadcn-ui@latest add dialog
npx shadcn-ui@latest add dropdown-menu
npx shadcn-ui@latest add select
npx shadcn-ui@latest add textarea
npx shadcn-ui@latest add toast
npx shadcn-ui@latest add avatar
npx shadcn-ui@latest add badge
npx shadcn-ui@latest add separator
```

### 4. Initialize Prisma

```bash
# Initialize Prisma
npx prisma init

# This creates:
# - prisma/schema.prisma
# - .env file with DATABASE_URL
```

### 5. Set Up Git Repository

```bash
# Initialize git
git init

# Create .gitignore (should already exist from create-next-app)
# Ensure these are included:
# node_modules/
# .next/
# .env.local
# .env
# *.log

# Initial commit
git add .
git commit -m "Initial commit: BNI Chapter Toolkit MVP"

# Create GitHub repository (via GitHub CLI or web)
gh repo create bni-chapter-toolkit --private --source=. --remote=origin

# Push to GitHub
git push -u origin main
```

---

## 🗄️ Database Setup

### Option A: Supabase (Recommended for MVP)

```bash
# 1. Create Supabase account at https://supabase.com
# 2. Create new project
# 3. Copy connection string from Settings > Database
# 4. Update .env.local

# .env.local
DATABASE_URL="postgresql://postgres:[PASSWORD]@db.[PROJECT-REF].supabase.co:5432/postgres"
DIRECT_URL="postgresql://postgres:[PASSWORD]@db.[PROJECT-REF].supabase.co:5432/postgres"
```

### Option B: Self-Hosted PostgreSQL (Proxmox)

```bash
# 1. SSH to Proxmox container
ssh root@10.92.3.XX

# 2. Install PostgreSQL
apt update
apt install postgresql postgresql-contrib

# 3. Create database and user
sudo -u postgres psql
CREATE DATABASE bni_toolkit;
CREATE USER bni_user WITH PASSWORD 'your_secure_password';
GRANT ALL PRIVILEGES ON DATABASE bni_toolkit TO bni_user;
\q

# 4. Update .env.local
DATABASE_URL="postgresql://bni_user:your_secure_password@10.92.3.XX:5432/bni_toolkit"
```

### Create Database Schema

```bash
# Create initial migration
npx prisma migrate dev --name init

# Generate Prisma client
npx prisma generate

# (Optional) Seed database with test data
npx prisma db seed
```

---

## 🔐 Authentication Setup

### Option A: Clerk (Recommended)

```bash
# 1. Create Clerk account at https://clerk.com
# 2. Create new application
# 3. Copy API keys from Dashboard

# .env.local
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=pk_test_...
CLERK_SECRET_KEY=sk_test_...
NEXT_PUBLIC_CLERK_SIGN_IN_URL=/admin/login
NEXT_PUBLIC_CLERK_SIGN_UP_URL=/admin/signup
NEXT_PUBLIC_CLERK_AFTER_SIGN_IN_URL=/admin/dashboard
NEXT_PUBLIC_CLERK_AFTER_SIGN_UP_URL=/admin/dashboard
```

### Option B: NextAuth.js

```bash
# 1. Generate secret
openssl rand -base64 32

# .env.local
NEXTAUTH_URL=http://localhost:3000
NEXTAUTH_SECRET=your_generated_secret
```

---

## 📸 Image Upload Setup (Cloudinary)

```bash
# 1. Create Cloudinary account at https://cloudinary.com
# 2. Copy credentials from Dashboard

# .env.local
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

---

## 📧 Email Setup (SendGrid or Nodemailer)

### Option A: SendGrid (Recommended for Production)

```bash
# 1. Create SendGrid account at https://sendgrid.com
# 2. Create API key from Settings > API Keys

# .env.local
SENDGRID_API_KEY=SG.xxx
SENDGRID_FROM_EMAIL=noreply@bnichaptertoolkit.com
```

### Option B: Nodemailer (Development/Self-Hosted)

```bash
# .env.local
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your_email@gmail.com
SMTP_PASSWORD=your_app_password
SMTP_FROM=noreply@bnichaptertoolkit.com
```

---

## 🌐 Environment Variables

### Complete .env.local Template

```bash
# Database
DATABASE_URL="postgresql://user:password@localhost:5432/bni_toolkit"
DIRECT_URL="postgresql://user:password@localhost:5432/bni_toolkit"

# Authentication (Clerk)
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=pk_test_...
CLERK_SECRET_KEY=sk_test_...
NEXT_PUBLIC_CLERK_SIGN_IN_URL=/admin/login
NEXT_PUBLIC_CLERK_SIGN_UP_URL=/admin/signup
NEXT_PUBLIC_CLERK_AFTER_SIGN_IN_URL=/admin/dashboard
NEXT_PUBLIC_CLERK_AFTER_SIGN_UP_URL=/admin/dashboard

# Image Upload (Cloudinary)
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret

# Email (SendGrid)
SENDGRID_API_KEY=SG.xxx
SENDGRID_FROM_EMAIL=noreply@bnichaptertoolkit.com

# App Configuration
NEXT_PUBLIC_APP_URL=http://localhost:3000
NEXT_PUBLIC_APP_NAME="BNI Chapter Toolkit"

# Payments (Phase 3)
# STRIPE_SECRET_KEY=sk_test_...
# STRIPE_PUBLISHABLE_KEY=pk_test_...
# STRIPE_WEBHOOK_SECRET=whsec_...

# Analytics (Optional)
# PLAUSIBLE_DOMAIN=bnichaptertoolkit.com
```

### Create .env.example

```bash
# Copy .env.local to .env.example and remove sensitive values
cp .env.local .env.example

# Edit .env.example to show structure without real values
# Commit .env.example to git (but NOT .env.local)
```

---

## 🎨 Tailwind & UI Configuration

### tailwind.config.ts

```typescript
import type { Config } from "tailwindcss";

const config: Config = {
  darkMode: ["class"],
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        // BNI brand colors (optional, can customize per chapter)
        primary: {
          DEFAULT: "#0066CC",
          foreground: "#FFFFFF",
        },
        secondary: {
          DEFAULT: "#F0F0F0",
          foreground: "#000000",
        },
      },
    },
  },
  plugins: [require("tailwindcss-animate")],
};

export default config;
```

---

## 🧪 Testing Setup (Optional for MVP)

```bash
# Install testing libraries
npm install -D @testing-library/react @testing-library/jest-dom jest jest-environment-jsdom

# Install Playwright for E2E tests (Phase 2)
# npm install -D @playwright/test
```

---

## 📝 Development Scripts

### Update package.json

```json
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint",
    "db:push": "prisma db push",
    "db:migrate": "prisma migrate dev",
    "db:generate": "prisma generate",
    "db:seed": "prisma db seed",
    "db:studio": "prisma studio",
    "format": "prettier --write .",
    "type-check": "tsc --noEmit"
  }
}
```

---

## 🚀 Deployment Setup

### Option A: Vercel (Recommended for MVP)

```bash
# 1. Install Vercel CLI
npm install -g vercel

# 2. Login to Vercel
vercel login

# 3. Deploy
vercel

# 4. Set environment variables in Vercel dashboard
# - Go to project settings
# - Add all environment variables from .env.local
# - Redeploy

# 5. Set up custom domain (optional)
# - Go to project settings > Domains
# - Add custom domain
# - Update DNS records
```

### Option B: Self-Hosted (Proxmox)

```bash
# 1. SSH to container
ssh root@10.92.3.XX

# 2. Clone repository
git clone https://github.com/yourusername/bni-chapter-toolkit.git
cd bni-chapter-toolkit

# 3. Install dependencies
npm install

# 4. Set up environment variables
cp .env.example .env.local
nano .env.local  # Edit with production values

# 5. Build application
npm run build

# 6. Start with PM2
npm install -g pm2
pm2 start npm --name "bni-toolkit" -- start
pm2 save
pm2 startup

# 7. Set up Nginx reverse proxy
# (Similar to existing TheoShift/LDC Tools setup)
```

---

## 🔄 CI/CD Pipeline (GitHub Actions)

### .github/workflows/ci.yml

```yaml
name: CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Type check
        run: npm run type-check
      
      - name: Lint
        run: npm run lint
      
      - name: Build
        run: npm run build
```

---

## 📚 Documentation Files to Create

### README.md

```markdown
# BNI Chapter Toolkit

Digital platform for BNI chapters to replace physical business card binders with shareable member directories and modernize visitor check-in.

## Features
- Digital member directory with shareable link
- Visitor check-in with business card capture
- Admin dashboard for chapter management

## Tech Stack
- Next.js 14+ (App Router)
- TypeScript
- PostgreSQL + Prisma
- TailwindCSS + shadcn/ui
- Clerk (Authentication)
- Cloudinary (Image Upload)

## Getting Started
[Installation instructions]

## License
MIT
```

### CONTRIBUTING.md

```markdown
# Contributing to BNI Chapter Toolkit

## Development Setup
[Setup instructions]

## Code Style
- Use TypeScript
- Follow ESLint rules
- Use Prettier for formatting

## Commit Messages
- Use conventional commits format
- Examples: feat:, fix:, docs:, refactor:

## Pull Request Process
1. Create feature branch
2. Make changes
3. Test locally
4. Submit PR with description
```

---

## ✅ Setup Checklist

### Initial Setup
- [ ] Create Next.js project
- [ ] Install dependencies
- [ ] Initialize Prisma
- [ ] Set up Git repository
- [ ] Create GitHub repository
- [ ] Configure environment variables

### Database
- [ ] Choose database provider (Supabase or self-hosted)
- [ ] Create database
- [ ] Run migrations
- [ ] Generate Prisma client
- [ ] Test database connection

### Authentication
- [ ] Choose auth provider (Clerk or NextAuth.js)
- [ ] Create auth account
- [ ] Configure auth settings
- [ ] Test login flow

### Services
- [ ] Set up Cloudinary account
- [ ] Configure image upload
- [ ] Set up email service (SendGrid or SMTP)
- [ ] Test email notifications

### Development
- [ ] Run dev server (`npm run dev`)
- [ ] Verify hot reload works
- [ ] Test database queries
- [ ] Test authentication

### Deployment
- [ ] Choose deployment platform (Vercel or self-hosted)
- [ ] Deploy to staging
- [ ] Configure production environment variables
- [ ] Test production build
- [ ] Set up custom domain (optional)

### Documentation
- [ ] Write README.md
- [ ] Create CONTRIBUTING.md
- [ ] Document API endpoints
- [ ] Create user guides

---

## 🐛 Troubleshooting

### Common Issues

**Issue:** Prisma client not generating
```bash
# Solution
npx prisma generate
```

**Issue:** Database connection fails
```bash
# Solution: Check DATABASE_URL in .env.local
# Ensure PostgreSQL is running
# Test connection: npx prisma db push
```

**Issue:** Authentication not working
```bash
# Solution: Check auth provider keys in .env.local
# Ensure URLs are correct
# Clear browser cookies and try again
```

**Issue:** Images not uploading
```bash
# Solution: Check Cloudinary credentials
# Ensure API key has upload permissions
# Check file size limits
```

**Issue:** Build fails on Vercel
```bash
# Solution: Check build logs
# Ensure all environment variables are set
# Verify Prisma is generating client in build step
```

---

## 📞 Support

**Development Questions:**
- Check documentation in `/docs`
- Review implementation plan
- Search GitHub issues

**Production Issues:**
- Check application logs
- Review error tracking (Sentry, LogRocket)
- Contact support team

---

**Last Updated:** 2026-01-29  
**Next Review:** After initial setup (Week 1)
