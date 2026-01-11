from main import app, db, User, Broker, calculate_commission, get_active_broker
from decimal import Decimal

def verify_broker_selection():
    with app.app_context():
        # 1. List all active brokers
        active_brokers = Broker.query.filter_by(is_active=True).all()
        print(f"\n--- Active Brokers Found: {len(active_brokers)} ---")
        for b in active_brokers:
            print(f"ID: {b.id}, Name: {b.name}, Rate: {b.commission_rate}%")

        # 2. See which one is selected by the system
        selected_broker = get_active_broker()
        print(f"\n--- System Selected Broker ---")
        if selected_broker:
            print(f"ID: {selected_broker.id}, Name: {selected_broker.name}, Rate: {selected_broker.commission_rate}%")
        else:
            print("No active broker selected.")

        # 3. Simulate a trade commission calculation
        trade_amount = Decimal('10000.00')
        commission = calculate_commission(trade_amount, selected_broker)
        print(f"\n--- Trade Simulation ---")
        print(f"Trade Amount: ${trade_amount}")
        print(f"Calculated Commission: ${commission}")
        
        # Verify if matches
        expected = trade_amount * (selected_broker.commission_rate / Decimal('100'))
        print(f"Verification: {trade_amount} * {selected_broker.commission_rate}% = {expected}")
        
if __name__ == "__main__":
    verify_broker_selection()
