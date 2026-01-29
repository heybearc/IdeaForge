# BNI Chapter Toolkit - MVP Feature Breakdown

**Project:** BNI Chapter Toolkit  
**Version:** 1.0 (MVP)  
**Last Updated:** 2026-01-29

---

## 🎯 MVP Scope Definition

**Goal:** Launch a functional product that solves the core problems in 8-12 weeks.

**MVP Philosophy:** 
- Focus on the 20% of features that deliver 80% of the value
- Ship fast, iterate based on real user feedback
- Avoid feature creep - save advanced features for Phase 2+

**Must Have (MVP):**
- Digital member directory with shareable link
- Visitor check-in with business card photo capture
- Basic admin dashboard for chapter management

**Nice to Have (Phase 2):**
- OCR for business card text extraction
- BNI Connect integration
- Advanced analytics
- Mobile app

**Won't Have (MVP):**
- Referral tracking
- Member engagement scoring
- Multi-chapter management
- White-label options

---

## 📱 Feature 1: Digital Member Directory

### User Story
> "As a BNI member, I want to share my chapter's member directory with prospects so they can easily find and contact the right member for their needs."

### Requirements

**Public Directory Page (`/c/[slug]`)**
- [ ] Unique shareable URL for each chapter (e.g., `/c/twinsbiz`)
- [ ] Grid/list view of all active chapter members
- [ ] Member card displays:
  - Profile photo (or placeholder if none)
  - Full name
  - Company name
  - Job title
  - Industry/profession
  - Phone number (click-to-call on mobile)
  - Email (click-to-email)
  - Website link (if provided)
  - LinkedIn profile (if provided)
  - Brief business description (2-3 sentences)
- [ ] Filter by industry/profession (dropdown or search)
- [ ] Search by name or company
- [ ] Mobile-responsive design
- [ ] Fast loading (<2 seconds)
- [ ] No authentication required (public access)

**Share Functionality**
- [ ] "Share" button generates shareable link
- [ ] Copy link to clipboard
- [ ] Generate QR code for directory (downloadable PNG)
- [ ] Social media share buttons (optional)
- [ ] Track views (analytics for admin)

**SEO & Performance**
- [ ] Meta tags for social sharing (Open Graph)
- [ ] Server-side rendering for fast initial load
- [ ] Image optimization (Next.js Image component)
- [ ] Lazy loading for member photos

### Acceptance Criteria
- ✅ Directory loads in <2 seconds on mobile
- ✅ All member info displays correctly
- ✅ Filter/search works accurately
- ✅ Shareable link works on all devices
- ✅ QR code generates and downloads correctly
- ✅ Responsive on mobile, tablet, desktop

### Technical Implementation
```typescript
// Page: app/c/[slug]/page.tsx
export default async function ChapterDirectoryPage({ params }) {
  const chapter = await getChapterBySlug(params.slug);
  const members = await getActiveMembers(chapter.id);
  
  return (
    <DirectoryLayout chapter={chapter}>
      <FilterBar industries={uniqueIndustries} />
      <MemberGrid members={members} />
      <ShareButton chapterSlug={params.slug} />
    </DirectoryLayout>
  );
}
```

### Design Notes
- Clean, professional design (not too flashy)
- BNI brand colors (optional, chapter can customize)
- Large, readable fonts for mobile
- High-contrast for accessibility
- Print-friendly layout (optional)

---

## 🚪 Feature 2: Visitor Check-In System

### User Story
> "As a chapter VP, I want visitors to check in digitally so I can capture their information and business cards without manual data entry."

### Requirements

**Check-In Landing Page (`/checkin/[slug]`)**
- [ ] QR code scans to this page
- [ ] Chapter name and logo displayed
- [ ] Welcome message (customizable by chapter)
- [ ] Mobile-optimized form (large touch targets)
- [ ] Progress indicator (Step 1 of 3)

**Check-In Form**
- [ ] Step 1: Basic Information
  - First name (required)
  - Last name (required)
  - Email (required, validated)
  - Phone number (optional, formatted)
  - Company name (optional)
  - Reason for visit (dropdown: Guest, Potential Member, Substitute, Other)
- [ ] Step 2: Business Card Capture
  - Camera access request
  - Take photo of card front (required)
  - Take photo of card back (optional)
  - Retake option if photo is blurry
  - Preview before submission
- [ ] Step 3: Confirmation
  - Review all entered information
  - Edit button to go back
  - Submit button
  - Privacy policy acceptance checkbox

**Form Validation**
- [ ] Real-time validation (show errors as user types)
- [ ] Email format validation
- [ ] Phone number formatting (US format)
- [ ] Required field indicators
- [ ] Clear error messages

**Photo Capture**
- [ ] Use device camera (mobile) or file upload (desktop)
- [ ] Image compression before upload (max 2MB)
- [ ] Upload to Cloudinary
- [ ] Loading indicator during upload
- [ ] Error handling if upload fails

**Confirmation Page**
- [ ] "Thank you" message
- [ ] "You've successfully checked in" confirmation
- [ ] Link to chapter member directory
- [ ] "What happens next" explanation
- [ ] Chapter contact information

**Admin Notification**
- [ ] Email to chapter admin(s) when visitor checks in
- [ ] Include visitor name, company, reason for visit
- [ ] Link to view full visitor details in admin dashboard
- [ ] Option to disable notifications (admin settings)

### Acceptance Criteria
- ✅ Form works on all mobile devices (iOS, Android)
- ✅ Camera access works correctly
- ✅ Photos upload successfully (<5 seconds)
- ✅ Form validation prevents invalid submissions
- ✅ Admin receives email notification within 1 minute
- ✅ Visitor sees confirmation page after submission
- ✅ All data saved to database correctly

### Technical Implementation
```typescript
// Page: app/checkin/[slug]/page.tsx
export default function CheckInPage({ params }) {
  const [step, setStep] = useState(1);
  const [formData, setFormData] = useState({});
  
  return (
    <CheckInLayout chapterSlug={params.slug}>
      {step === 1 && <BasicInfoForm onNext={handleNext} />}
      {step === 2 && <BusinessCardCapture onNext={handleNext} />}
      {step === 3 && <ConfirmationStep onSubmit={handleSubmit} />}
    </CheckInLayout>
  );
}

// API: app/api/visitor/checkin/route.ts
export async function POST(request: Request) {
  const data = await request.json();
  
  // Validate data
  const validated = visitorSchema.parse(data);
  
  // Save to database
  const visitor = await createVisitor(validated);
  
  // Send notification email
  await sendVisitorNotification(visitor);
  
  return Response.json({ success: true, visitor });
}
```

### Design Notes
- Large form fields (easy to tap on mobile)
- Clear step indicators (1 of 3, 2 of 3, etc.)
- Minimal distractions (focus on form completion)
- Friendly, welcoming tone
- Clear instructions for camera usage

---

## 🔧 Feature 3: Admin Dashboard

### User Story
> "As a chapter admin, I want to manage my chapter's members and view visitor data so I can keep the directory up-to-date and follow up with visitors."

### Requirements

**Admin Authentication**
- [ ] Login page (`/admin/login`)
- [ ] Email + password authentication (Clerk or NextAuth.js)
- [ ] "Forgot password" flow
- [ ] Role-based access (admin, president, VP)
- [ ] Session management (stay logged in)
- [ ] Logout functionality

**Dashboard Home (`/admin/dashboard`)**
- [ ] Welcome message with chapter name
- [ ] Quick stats cards:
  - Total active members
  - Visitors this week
  - Visitors this month
  - Directory views this week
- [ ] Recent visitors list (last 10)
- [ ] Quick actions:
  - Add new member
  - View all visitors
  - Generate QR code
  - Chapter settings

**Member Management (`/admin/members`)**
- [ ] List all members (table view)
- [ ] Columns: Photo, Name, Company, Industry, Status, Actions
- [ ] Sort by name, company, industry, date added
- [ ] Filter by status (active, inactive)
- [ ] Search by name or company
- [ ] Pagination (20 members per page)
- [ ] Bulk actions (activate, deactivate, delete)

**Add/Edit Member Form**
- [ ] Modal or separate page
- [ ] Fields:
  - First name (required)
  - Last name (required)
  - Email (required)
  - Phone (optional)
  - Company (required)
  - Job title (optional)
  - Industry (required, dropdown)
  - Business description (textarea, 500 char max)
  - Website (optional, URL validation)
  - LinkedIn (optional, URL validation)
  - Profile photo (upload, max 5MB)
  - Status (active/inactive toggle)
  - Display order (number, for custom sorting)
- [ ] Form validation
- [ ] Save and continue editing
- [ ] Cancel button (confirm if unsaved changes)

**Visitor Management (`/admin/visitors`)**
- [ ] List all visitors (table view)
- [ ] Columns: Date, Name, Company, Reason, Card Photos, Actions
- [ ] Sort by date (newest first)
- [ ] Filter by date range (this week, this month, custom)
- [ ] Filter by reason for visit
- [ ] Search by name or company
- [ ] Pagination (50 visitors per page)
- [ ] Export to CSV button

**Visitor Detail View**
- [ ] Modal or separate page
- [ ] Display all visitor information
- [ ] Show business card photos (front/back)
- [ ] Zoom/download card photos
- [ ] Add follow-up notes (textarea)
- [ ] Mark as "followed up" (checkbox)
- [ ] Assign to member (dropdown)
- [ ] Edit visitor information
- [ ] Delete visitor (with confirmation)

**QR Code Generator (`/admin/qrcode`)**
- [ ] Generate QR code for visitor check-in
- [ ] Generate QR code for member directory
- [ ] Customize QR code (logo, colors) - Phase 2
- [ ] Download as PNG (high resolution)
- [ ] Download as PDF (printable)
- [ ] Preview before download
- [ ] Instructions for printing and displaying

**Chapter Settings (`/admin/settings`)**
- [ ] Chapter information:
  - Chapter name (editable)
  - Location (editable)
  - BNI chapter number (optional)
  - Shareable slug (editable, must be unique)
- [ ] Admin users:
  - List current admins
  - Add new admin (by email)
  - Remove admin (with confirmation)
  - Change admin role (admin, president, VP)
- [ ] Notification settings:
  - Email notifications on/off
  - Notification recipients (multiple emails)
- [ ] Branding (Phase 2):
  - Chapter logo upload
  - Primary color
  - Welcome message for visitors
- [ ] Danger zone:
  - Delete chapter (with confirmation, requires password)

**Export Functionality**
- [ ] Export visitors to CSV
- [ ] Columns: Date, First Name, Last Name, Email, Phone, Company, Reason
- [ ] Filter by date range before export
- [ ] Download immediately (no email)
- [ ] BNI Connect format (Phase 2)

### Acceptance Criteria
- ✅ Admin can log in and access dashboard
- ✅ Admin can add/edit/delete members
- ✅ Member changes reflect in public directory immediately
- ✅ Admin can view all visitors with photos
- ✅ Admin can export visitors to CSV
- ✅ Admin can generate and download QR codes
- ✅ Admin can update chapter settings
- ✅ All forms validate correctly
- ✅ Dashboard loads in <3 seconds

### Technical Implementation
```typescript
// Page: app/admin/dashboard/page.tsx
export default async function AdminDashboard() {
  const chapter = await getCurrentChapter();
  const stats = await getChapterStats(chapter.id);
  const recentVisitors = await getRecentVisitors(chapter.id, 10);
  
  return (
    <AdminLayout>
      <StatsCards stats={stats} />
      <RecentVisitorsList visitors={recentVisitors} />
      <QuickActions chapterId={chapter.id} />
    </AdminLayout>
  );
}

// API: app/api/admin/member/route.ts
export async function POST(request: Request) {
  const session = await getSession();
  if (!session) return Response.json({ error: 'Unauthorized' }, { status: 401 });
  
  const data = await request.json();
  const validated = memberSchema.parse(data);
  
  const member = await createMember(validated);
  
  return Response.json({ success: true, member });
}
```

### Design Notes
- Clean, professional admin interface
- Consistent with public-facing pages
- Clear navigation (sidebar or top nav)
- Breadcrumbs for deep pages
- Confirmation modals for destructive actions
- Loading states for all async operations
- Toast notifications for success/error messages

---

## 🔐 Feature 4: Authentication & Authorization

### User Story
> "As a chapter admin, I want secure access to the admin dashboard so only authorized users can manage chapter data."

### Requirements

**Authentication Provider**
- [ ] Choose provider: Clerk (recommended) or NextAuth.js
- [ ] Email + password authentication
- [ ] Password reset flow
- [ ] Email verification (optional for MVP)
- [ ] Session management
- [ ] Secure token storage

**Authorization Levels**
- [ ] **Admin**: Full access (add/edit/delete members, manage settings)
- [ ] **President**: Full access (same as admin)
- [ ] **VP**: Limited access (view visitors, export data, no member management)
- [ ] **Member**: No admin access (future: view own profile)

**Protected Routes**
- [ ] All `/admin/*` routes require authentication
- [ ] Redirect to login if not authenticated
- [ ] Redirect to dashboard after login
- [ ] Role-based route protection (VP can't access member management)

**Security Features**
- [ ] HTTPS only (enforced)
- [ ] CSRF protection (Next.js built-in)
- [ ] Rate limiting on login attempts
- [ ] Secure password requirements (8+ chars, mix of types)
- [ ] Session timeout (7 days)
- [ ] Logout on all devices option

### Acceptance Criteria
- ✅ Only authenticated users can access admin dashboard
- ✅ Users can log in with email + password
- ✅ Users can reset forgotten passwords
- ✅ Sessions persist across browser restarts
- ✅ Users can log out successfully
- ✅ Role-based permissions enforced

### Technical Implementation
```typescript
// Using Clerk
import { auth } from '@clerk/nextjs';

export default async function AdminPage() {
  const { userId } = auth();
  if (!userId) redirect('/admin/login');
  
  // Page content
}

// Middleware: middleware.ts
export default authMiddleware({
  publicRoutes: ['/c/:slug', '/checkin/:slug'],
  ignoredRoutes: ['/api/public/:path*'],
});
```

---

## 📊 Feature 5: Basic Analytics

### User Story
> "As a chapter admin, I want to see how many people are viewing our directory and checking in so I can measure engagement."

### Requirements

**Analytics Dashboard (`/admin/analytics`)**
- [ ] Date range selector (this week, this month, last 30 days, custom)
- [ ] Key metrics:
  - Total directory views
  - Unique directory visitors
  - Total visitor check-ins
  - Average check-ins per meeting
- [ ] Simple charts:
  - Directory views over time (line chart)
  - Check-ins over time (bar chart)
  - Top industries viewed (pie chart)
- [ ] No external analytics tools (self-hosted)

**Tracking Implementation**
- [ ] Track directory page views (server-side)
- [ ] Track visitor check-ins (already in database)
- [ ] Track member card clicks (optional)
- [ ] Store in database (simple events table)
- [ ] Privacy-friendly (no personal data tracking)

### Acceptance Criteria
- ✅ Analytics dashboard displays correct data
- ✅ Charts render correctly
- ✅ Date range filter works
- ✅ Data updates in real-time (or near real-time)

### Technical Implementation
```typescript
// Track page view
export async function trackPageView(chapterId: string, page: string) {
  await prisma.analyticsEvent.create({
    data: {
      chapterId,
      eventType: 'page_view',
      eventData: { page },
      timestamp: new Date(),
    },
  });
}

// Get analytics
export async function getChapterAnalytics(chapterId: string, dateRange: DateRange) {
  const events = await prisma.analyticsEvent.findMany({
    where: {
      chapterId,
      timestamp: { gte: dateRange.start, lte: dateRange.end },
    },
  });
  
  return aggregateEvents(events);
}
```

---

## 🎨 Feature 6: Responsive Design

### User Story
> "As a user, I want the app to work perfectly on my phone, tablet, and desktop so I can use it anywhere."

### Requirements

**Mobile-First Design**
- [ ] Design for mobile first, then scale up
- [ ] Touch-friendly UI (large buttons, adequate spacing)
- [ ] Fast loading on mobile networks
- [ ] Works offline (graceful degradation)

**Breakpoints**
- [ ] Mobile: 320px - 640px
- [ ] Tablet: 641px - 1024px
- [ ] Desktop: 1025px+

**Responsive Components**
- [ ] Navigation (hamburger menu on mobile, full nav on desktop)
- [ ] Member grid (1 column on mobile, 2 on tablet, 3-4 on desktop)
- [ ] Forms (full-width on mobile, centered on desktop)
- [ ] Tables (horizontal scroll on mobile, full table on desktop)
- [ ] Modals (full-screen on mobile, centered on desktop)

**Performance**
- [ ] Image optimization (Next.js Image component)
- [ ] Lazy loading for images
- [ ] Code splitting (automatic with Next.js)
- [ ] Minimize bundle size
- [ ] Fast initial load (<2 seconds on 3G)

### Acceptance Criteria
- ✅ App works on iPhone, Android, iPad, desktop
- ✅ All features accessible on mobile
- ✅ No horizontal scrolling on mobile
- ✅ Touch targets are at least 44x44px
- ✅ Text is readable without zooming

---

## 🚀 MVP Feature Priority

### Must Have (Week 1-8)
1. **Member Directory** (Week 3-4) - Core value proposition
2. **Visitor Check-In** (Week 5-6) - Core value proposition
3. **Admin Dashboard** (Week 7-8) - Required for chapter management
4. **Authentication** (Week 7) - Security requirement
5. **Responsive Design** (Throughout) - Mobile-first requirement

### Should Have (Week 9-11, Beta Phase)
1. **Basic Analytics** - Helps demonstrate value
2. **CSV Export** - Requested by VPs
3. **QR Code Generator** - Convenient for chapters

### Could Have (Phase 2, Post-Launch)
1. **OCR for Business Cards** - Nice to have, not critical
2. **BNI Connect Integration** - Valuable but can be manual for MVP
3. **Advanced Analytics** - Can use basic analytics for MVP
4. **Custom Branding** - Can use default branding for MVP

### Won't Have (MVP)
1. **Referral Tracking** - Too complex for MVP
2. **Member Engagement Scoring** - Not critical
3. **Mobile App** - Web app is sufficient
4. **Multi-Chapter Management** - One chapter at a time for MVP
5. **White-Label** - Not needed until scale

---

## ✅ MVP Definition of Done

**A feature is "done" when:**
- [ ] Code is written and tested
- [ ] Works on mobile, tablet, desktop
- [ ] Passes manual testing (happy path + edge cases)
- [ ] Error handling implemented
- [ ] Loading states implemented
- [ ] Accessible (keyboard navigation, screen readers)
- [ ] Documented (code comments, README)
- [ ] Deployed to staging environment
- [ ] Reviewed by at least one beta user
- [ ] No critical bugs

**MVP is "done" when:**
- [ ] All "Must Have" features complete
- [ ] Tested with TwinsBiz chapter (real users)
- [ ] No critical bugs
- [ ] Performance acceptable (<3 second load times)
- [ ] Security review passed
- [ ] Documentation complete (user guide, admin guide)
- [ ] Ready for beta launch with 5 chapters

---

## 📝 Feature Request Process (Post-MVP)

**How to handle feature requests from beta users:**

1. **Collect**: Add to feature request backlog (GitHub Issues or Notion)
2. **Categorize**: Bug, enhancement, new feature
3. **Prioritize**: Impact (high/medium/low) × Effort (high/medium/low)
4. **Decide**: Build, defer, or decline
5. **Communicate**: Let requester know decision and timeline

**Priority Matrix:**
- **High Impact + Low Effort** = Build immediately
- **High Impact + High Effort** = Plan for next phase
- **Low Impact + Low Effort** = Build if time permits
- **Low Impact + High Effort** = Decline (politely)

---

**Last Updated:** 2026-01-29  
**Next Review:** After MVP completion (Week 8)
