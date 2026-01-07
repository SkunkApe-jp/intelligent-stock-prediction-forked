## How to See Broker Management and Dividend Payout in Action

Here's a step-by-step guide to see these features working:

### Starting the Application
1. Run the Flask application: `python main.py`
2. Open your browser and go to the local URL (usually http://localhost:5000)

### Broker Management Features

**Admin Side:**
1. **Login as Admin** - Use the admin dashboard at `/admin` 
2. **Add Brokers** - Navigate to broker management section and add brokers with different commission rates (e.g., 0.5%, 1%, 2%)
3. **View Broker Analytics** - See total commissions earned, transaction counts, and performance metrics

**User Side:**
1. **Register as Regular User** - Create a new account
2. **Make Trades** - Execute buy/sell transactions and see automatic commission calculation
3. **View Transaction History** - See how broker fees are automatically applied to each trade

### Dividend Payout Features

**User Dashboard:**
1. **Record Dividend** - Use the dividend recording form in your dashboard
2. **Automatic Calculation** - Enter dividend per share amount and system calculates total payout
3. **Instant Credit** - See immediate wallet balance updates
4. **Transaction Audit** - View complete dividend transaction history

**Portfolio Integration:**
1. **Holdings-Based Calculation** - System automatically knows how many shares you own
2. **Real-time Balance** - See dividends credited to your wallet immediately
3. **Historical Records** - Track all dividend payouts over time

### Key Features in Action
- **Commission Tracking**: Every trade automatically calculates and deducts broker commissions
- **Admin Oversight**: Complete visibility into all broker activities and earnings
- **Dividend Automation**: One-click dividend recording with instant portfolio integration
- **Audit Trail**: Complete transaction history for both features

The system provides a fully functional simulated trading environment where you can test all broker and dividend features end-to-end.