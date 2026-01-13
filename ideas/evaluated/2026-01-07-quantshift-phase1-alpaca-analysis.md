# QuantShift Phase 1: Alpaca Stock Bot - Current State Analysis

**Date:** 2026-01-07  
**Category:** trading-bots  
**Status:** IN PROGRESS (Day 11 of 30 paper trading)  
**ML Score:** 93/100 (Highest priority)

---

## 🎯 Current State Summary

### **What's Already Built (Impressive!)**

You have a **fully architected, production-ready trading platform** with:

#### **1. Complete Dashboard (trader.cloudigan.net)** ✅
- Real-time bot status monitoring
- Account equity, cash, buying power tracking
- Portfolio value and P&L (realized/unrealized)
- Open positions display
- Recent trades (last 5)
- Auto-refresh every 30 seconds
- Authentication system (username-based)
- User management
- Release notes system
- Health monitoring
- API status dashboard

#### **2. Broker-Agnostic Architecture** ✅
**This is professional-grade design:**
```
Strategy Layer (Pure Logic)
    ↓
Executor Layer (Broker-Specific)
    ↓
Bot Application (Orchestration)
```

**Key Components:**
- `BaseStrategy` - Abstract strategy interface
- `MACrossoverStrategy` - Concrete MA 5/20 implementation
- `AlpacaExecutor` - Alpaca-specific execution
- `run_bot_v2.py` - Main bot orchestration

**Why This Matters:**
- Same strategy works with ANY broker (Alpaca, Coinbase, etc.)
- Backtesting uses SAME code as live trading
- Easy to add new strategies without touching broker code
- Industry-standard architecture

#### **3. Paper Trading Bot (Day 11/30)** ✅
**Currently Running:**
- MA 5/20 crossover strategy
- Paper trading on Alpaca
- Started: December 26, 2025
- Target completion: January 25, 2026
- 19 days remaining

**Expected Performance (from backtest):**
- Win Rate: 52.6%
- Profit Factor: 2.40
- Max Drawdown: 6.34%
- Total Return: +17.4%

#### **4. Infrastructure** ✅
- PostgreSQL database (Container 131)
- Redis for state management
- Systemd services for bot management
- Production deployment on Proxmox
- Monitoring and health checks

#### **5. Admin Platform (Week 2 in progress)** 🔄
**Completed:**
- User management
- Authentication system
- Release notes
- Navigation structure
- Health monitoring
- API status

**This Week (Jan 6-12):**
- Settings page (email config)
- Session management
- Audit logs viewer

---

## 📊 Phase 1 Status: Alpaca Stock Bot

### **What You HAVE (Stock Bot Foundation):**

✅ **Core Trading Engine:**
- MA Crossover strategy (working, paper trading)
- Alpaca API integration (complete)
- Risk management (ATR-based position sizing)
- Stop loss / take profit logic
- Volume confirmation filter
- Trend confirmation filter

✅ **Execution Layer:**
- `AlpacaExecutor` class (fully implemented)
- Market data fetching
- Order execution
- Position management
- Account data normalization

✅ **Bot Orchestration:**
- Configuration system (YAML)
- Lifecycle management (start/stop/signals)
- Redis state updates
- PostgreSQL trade syncing
- Scheduled execution

✅ **Dashboard Integration:**
- Real-time bot status
- Trade history
- Position tracking
- Performance metrics
- Account balance

---

### **What You NEED (DCA Product Features):**

The current bot is a **discretionary trading bot** (MA crossover signals).  
For a **DCA product** ($9-19/mo subscription), you need:

#### **🔴 CRITICAL: DCA Scheduling System**
**What's Missing:**
- Recurring buy schedules (daily/weekly/monthly)
- Fixed dollar amount purchases ($50, $100, $200/week)
- Multi-symbol DCA (SPY, QQQ, VOO, VTI, etc.)
- Set-and-forget automation

**Current Gap:**
- Your bot trades based on MA crossover signals (discretionary)
- DCA needs to buy on SCHEDULE regardless of price
- Need new strategy: `DCAStrategy` class

**Implementation Needed:**
```python
class DCAStrategy(BaseStrategy):
    """Dollar-cost averaging strategy"""
    
    def __init__(self, config):
        self.schedule = config['schedule']  # 'daily', 'weekly', 'monthly'
        self.amount_per_purchase = config['amount']  # $100
        self.symbols = config['symbols']  # ['SPY', 'QQQ']
        self.day_of_week = config.get('day_of_week', 'Monday')
        self.time_of_day = config.get('time_of_day', '10:00')
    
    def generate_signals(self, market_data, account, positions):
        """Generate DCA buy signals based on schedule"""
        signals = []
        
        # Check if it's time to buy (based on schedule)
        if self.should_execute_dca():
            for symbol in self.symbols:
                # Calculate shares to buy with fixed dollar amount
                current_price = market_data[symbol]['close']
                shares = self.amount_per_purchase / current_price
                
                signals.append(Signal(
                    symbol=symbol,
                    signal_type=SignalType.BUY,
                    quantity=shares,
                    reason=f"DCA scheduled purchase: ${self.amount_per_purchase}"
                ))
        
        return signals
```

#### **🔴 CRITICAL: User Configuration UI**
**What's Missing:**
- DCA setup wizard for users
- Symbol selection (pick stocks/ETFs)
- Schedule configuration (daily/weekly/monthly)
- Amount per purchase ($50-500)
- Start/pause/stop controls

**Where to Add:**
- New page: `/dashboard/dca-settings`
- API endpoints: `/api/dca/config`, `/api/dca/schedule`
- Database table: `DCAConfiguration`

#### **🟡 IMPORTANT: Multi-User Support**
**Current State:**
- Single bot instance
- One strategy configuration
- Shared account

**DCA Product Needs:**
- Each user has their own DCA configuration
- Separate Alpaca accounts (or sub-accounts)
- Isolated portfolios
- User-specific schedules

**Implementation Options:**

**Option A: Multi-Tenant Bot (Recommended)**
```python
# One bot instance manages multiple users
for user in active_users:
    user_config = load_user_dca_config(user.id)
    user_executor = AlpacaExecutor(
        strategy=DCAStrategy(user_config),
        alpaca_client=get_user_alpaca_client(user),
        symbols=user_config['symbols']
    )
    results = user_executor.run_strategy_cycle()
    save_user_results(user.id, results)
```

**Option B: Bot Per User**
```python
# Each user gets their own bot instance
# More resource-intensive but simpler isolation
```

#### **🟡 IMPORTANT: Pricing Tiers**
**What's Missing:**
- Subscription management (Stripe integration)
- Tier-based feature access
- Usage tracking
- Billing system

**Proposed Tiers:**
- **Basic ($9/mo):** 3 symbols, weekly DCA only
- **Pro ($19/mo):** 10 symbols, daily/weekly/monthly DCA, custom schedules
- **Premium ($29/mo):** Unlimited symbols, advanced features

---

## 🚀 Phase 1 Roadmap: Alpaca DCA Bot

### **Week 1-2: DCA Strategy Implementation**
**Estimated: 20-30 hours**

**Tasks:**
1. Create `DCAStrategy` class
   - Schedule-based signal generation
   - Fixed dollar amount purchases
   - Multi-symbol support
   - Time-of-day optimization

2. Extend `AlpacaExecutor` for DCA
   - Fractional share support
   - Dollar-based orders (not share-based)
   - Schedule validation

3. Configuration system
   - YAML config for DCA parameters
   - User-specific configurations
   - Schedule management

**Deliverable:** Working DCA bot that buys on schedule

---

### **Week 3-4: User Configuration UI**
**Estimated: 30-40 hours**

**Tasks:**
1. DCA Settings Page (`/dashboard/dca-settings`)
   - Symbol picker (search stocks/ETFs)
   - Schedule selector (daily/weekly/monthly)
   - Amount input ($50-500)
   - Day/time picker
   - Start/pause/stop buttons

2. API Endpoints
   - `POST /api/dca/config` - Save user DCA config
   - `GET /api/dca/config` - Load user config
   - `POST /api/dca/start` - Start DCA
   - `POST /api/dca/pause` - Pause DCA
   - `GET /api/dca/history` - DCA purchase history

3. Database Schema
   ```sql
   CREATE TABLE dca_configurations (
       id UUID PRIMARY KEY,
       user_id UUID REFERENCES users(id),
       symbols TEXT[],
       schedule VARCHAR(20), -- 'daily', 'weekly', 'monthly'
       amount_per_purchase DECIMAL(10,2),
       day_of_week VARCHAR(10),
       time_of_day TIME,
       is_active BOOLEAN,
       created_at TIMESTAMP,
       updated_at TIMESTAMP
   );
   
   CREATE TABLE dca_purchases (
       id UUID PRIMARY KEY,
       user_id UUID REFERENCES users(id),
       config_id UUID REFERENCES dca_configurations(id),
       symbol VARCHAR(10),
       shares DECIMAL(10,6),
       price DECIMAL(10,2),
       amount DECIMAL(10,2),
       executed_at TIMESTAMP
   );
   ```

**Deliverable:** Users can configure their own DCA schedules

---

### **Week 5-6: Multi-User Support**
**Estimated: 30-40 hours**

**Tasks:**
1. Multi-tenant bot architecture
   - User queue management
   - Isolated execution per user
   - Resource allocation
   - Error handling per user

2. Alpaca account management
   - User API key storage (encrypted)
   - Account validation
   - Balance checking
   - Error handling

3. User dashboard enhancements
   - DCA purchase history
   - Portfolio tracking (per user)
   - Performance metrics (per user)
   - Next scheduled purchase display

**Deliverable:** Multiple users can run DCA simultaneously

---

### **Week 7-8: Subscription & Launch**
**Estimated: 20-30 hours**

**Tasks:**
1. Stripe integration
   - Subscription plans (Basic/Pro/Premium)
   - Payment processing
   - Webhook handling
   - Billing portal

2. Feature gating
   - Tier-based symbol limits
   - Schedule restrictions per tier
   - Usage tracking

3. Onboarding flow
   - Welcome wizard
   - Alpaca account connection
   - First DCA setup
   - Educational content

4. Launch preparation
   - Landing page
   - Pricing page
   - Documentation
   - Support system

**Deliverable:** Launch-ready DCA product

---

## 💰 Revenue Model (Phase 1 Only)

### **Stock DCA Product Pricing:**
- **Basic:** $9/mo - 3 symbols, weekly DCA
- **Pro:** $19/mo - 10 symbols, daily/weekly/monthly DCA
- **Premium:** $29/mo - Unlimited symbols, advanced features

### **Projected Revenue (Stock Bot Only):**
**Month 3:**
- 100 users × $9 avg = $900/mo

**Month 6:**
- 300 users × $12 avg = $3,600/mo

**Month 12:**
- 800 users × $14 avg = $11,200/mo

---

## 🎯 Key Decisions Needed

### **1. DCA vs Discretionary Trading**
**Current:** MA crossover (discretionary signals)  
**DCA Product:** Schedule-based purchases

**Decision:** Build DCA as separate strategy OR replace MA crossover?

**Recommendation:** Keep both, let users choose:
- "Smart DCA" - Buy on schedule + MA confirmation
- "Pure DCA" - Buy on schedule regardless of price
- "Discretionary" - MA crossover only (current bot)

---

### **2. Alpaca Account Model**
**Option A:** Users connect their own Alpaca accounts
- **Pros:** No regulatory issues, users control funds
- **Cons:** Friction (users need Alpaca account), support burden

**Option B:** Master Alpaca account with sub-accounts
- **Pros:** Seamless UX, easier onboarding
- **Cons:** Regulatory complexity, custody issues

**Recommendation:** Option A (user-owned accounts) for Phase 1

---

### **3. Paper Trading vs Live Trading**
**Current:** Paper trading (Day 11/30)

**Decision:** When to offer live trading to customers?

**Recommendation:**
- Launch with paper trading first (educational/testing)
- Add live trading after 30-day validation
- Require users to complete paper trading before live

---

## 📋 Immediate Next Steps (This Week)

### **Priority 1: Finish Current Admin Features** 🔴
**Why:** Need settings/email before launching DCA product

**Tasks (from your roadmap):**
1. Settings page (email configuration)
2. Session management
3. Audit logs viewer

**Timeline:** Complete by Jan 12 (this week)

---

### **Priority 2: Design DCA Strategy** 🔴
**Why:** Core product feature

**Tasks:**
1. Sketch out `DCAStrategy` class
2. Define configuration schema
3. Plan schedule logic
4. Design UI mockups

**Timeline:** Jan 13-14 (next week)

---

### **Priority 3: Validate Paper Trading** 🟡
**Why:** Need proof strategy works before selling

**Tasks:**
1. Monitor bot performance (daily)
2. Compare to backtest metrics
3. Document any issues
4. Prepare for live trading decision (Jan 25)

**Timeline:** Ongoing (19 days remaining)

---

## 🎓 What Makes Your Architecture Excellent

### **1. Broker-Agnostic Design**
Most trading bots are tightly coupled to one broker. Yours isn't.

**Benefit:** When you add Coinbase (Phase 2), you can reuse:
- Strategy layer (same DCA logic)
- Dashboard (same UI)
- Database (same schema)
- Only need new `CoinbaseExecutor`

### **2. Separation of Concerns**
- Strategies = Pure logic (no broker code)
- Executors = Broker-specific (no strategy code)
- Bot = Orchestration (ties everything together)

**Benefit:** Easy to test, maintain, and extend

### **3. Production-Ready Infrastructure**
- PostgreSQL (not SQLite)
- Redis (state management)
- Systemd (process management)
- Health monitoring
- Proper logging

**Benefit:** Can scale to thousands of users

---

## 🚨 Potential Challenges

### **1. Regulatory Compliance**
**Issue:** Offering trading services may require licenses

**Mitigation:**
- Users connect their own Alpaca accounts (you don't custody funds)
- Clear disclaimers (not investment advice)
- Educational focus
- Consult lawyer before launch

### **2. Alpaca API Limits**
**Issue:** Rate limits, paper trading restrictions

**Mitigation:**
- Implement rate limiting
- Queue user requests
- Monitor API usage
- Plan for scaling

### **3. Support Burden**
**Issue:** Users will have questions, issues, complaints

**Mitigation:**
- Comprehensive documentation
- Video tutorials
- FAQ system
- Support ticket system
- Community forum

---

## 📊 Success Metrics

### **Technical Metrics:**
- Bot uptime: >99%
- DCA execution accuracy: 100%
- API response time: <500ms
- Error rate: <1%

### **Business Metrics:**
- User signups: 100/month
- Conversion rate: 20% (free → paid)
- Churn rate: <5%/month
- MRR growth: 20%/month

### **User Metrics:**
- Average DCA amount: $200/week
- Symbols per user: 4
- Active users: 80%
- Support tickets: <5/week

---

## 🎯 Summary: Phase 1 Path Forward

### **What You Have:**
✅ Professional trading platform architecture  
✅ Working MA crossover bot (paper trading)  
✅ Complete dashboard with monitoring  
✅ User management and authentication  
✅ Production infrastructure

### **What You Need (4-8 weeks):**
🔴 DCA strategy implementation (2 weeks)  
🔴 User configuration UI (2 weeks)  
🔴 Multi-user support (2 weeks)  
🔴 Subscription system (2 weeks)

### **Timeline:**
- **Weeks 1-2 (Jan 6-19):** Finish admin features + design DCA
- **Weeks 3-4 (Jan 20-Feb 2):** Build DCA strategy + UI
- **Weeks 5-6 (Feb 3-16):** Multi-user support
- **Weeks 7-8 (Feb 17-Mar 2):** Subscription + launch

### **Launch Target:**
**March 2026** - Stock DCA product ($9-29/mo)

---

## 💡 Recommendation

**Your QuantShift platform is VERY well architected.** You're not starting from scratch - you're 60% done with Phase 1.

**Focus on:**
1. Finish current admin features (this week)
2. Complete 30-day paper trading validation (Jan 25)
3. Build DCA strategy (Feb)
4. Launch Stock DCA product (March)
5. THEN add Coinbase crypto bot (Phase 2)

**Don't rush.** Your architecture is solid. Take time to:
- Validate paper trading performance
- Build DCA features properly
- Test with beta users
- Launch when ready

**You're building a $50k-100k/year business. Do it right.** 🚀

---

**Next Action:** Want me to help design the `DCAStrategy` class or create detailed UI mockups for the DCA settings page?
