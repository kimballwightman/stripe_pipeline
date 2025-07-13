#!/usr/bin/env python3
"""
Stripe Sandbox Environment Setup Script
This script checks for existing data in your Stripe sandbox and creates mock data if needed.
All objects are related through IDs to create a realistic test environment.
"""

import stripe
import os
from dotenv import load_dotenv
import json
from datetime import datetime, timedelta

# Load environment variables
load_dotenv()

# Configure Stripe
stripe.api_key = os.getenv("STRIPE_API_SECRET_KEY")

def print_section(title):
    """Print a formatted section header"""
    print(f"\n{'='*60}")
    print(f" {title}")
    print(f"{'='*60}")

def print_step(step_num, description):
    """Print a formatted step"""
    print(f"\n{step_num}. {description}")
    print("-" * 50)

def check_stripe_connection():
    """Verify that we can connect to Stripe"""
    try:
        # Try to retrieve account info
        account = stripe.Account.retrieve()
        print(f"✅ Successfully connected to Stripe!")
        print(f"   Account ID: {account.id}")
        print(f"   Business Type: {account.business_type}")
        print(f"   Country: {account.country}")
        return True
    except Exception as e:
        print(f"❌ Failed to connect to Stripe: {e}")
        return False

def check_existing_data():
    """Check for existing data in all major Stripe objects"""
    print_section("CHECKING EXISTING DATA")
    
    existing_data = {}
    
    # Check customers
    print_step(1, "Checking existing customers")
    customers = stripe.Customer.list(limit=10)
    existing_data['customers'] = customers.data
    print(f"   Found {len(customers.data)} existing customers")
    
    # Check payment methods (need to check via customers since payment methods require customer context)
    print_step(2, "Checking existing payment methods")
    payment_methods = []
    for customer in customers.data[:5]:  # Check first 5 customers
        pm_list = stripe.PaymentMethod.list(customer=customer.id, limit=10)
        payment_methods.extend(pm_list.data)
    existing_data['payment_methods'] = payment_methods
    print(f"   Found {len(payment_methods)} existing payment methods")
    
    # Check products
    print_step(3, "Checking existing products")
    products = stripe.Product.list(limit=10)
    existing_data['products'] = products.data
    print(f"   Found {len(products.data)} existing products")
    
    # Check prices
    print_step(4, "Checking existing prices")
    prices = stripe.Price.list(limit=10)
    existing_data['prices'] = prices.data
    print(f"   Found {len(prices.data)} existing prices")
    
    # Check subscriptions
    print_step(5, "Checking existing subscriptions")
    subscriptions = stripe.Subscription.list(limit=10)
    existing_data['subscriptions'] = subscriptions.data
    print(f"   Found {len(subscriptions.data)} existing subscriptions")
    
    # Check invoices
    print_step(6, "Checking existing invoices")
    invoices = stripe.Invoice.list(limit=10)
    existing_data['invoices'] = invoices.data
    print(f"   Found {len(invoices.data)} existing invoices")
    
    # Check payment intents
    print_step(7, "Checking existing payment intents")
    payment_intents = stripe.PaymentIntent.list(limit=10)
    existing_data['payment_intents'] = payment_intents.data
    print(f"   Found {len(payment_intents.data)} existing payment intents")
    
    return existing_data

def create_mock_data():
    """Create comprehensive mock data with proper relationships"""
    print_section("CREATING MOCK DATA")
    
    mock_data = {}
    
    # Step 1: Create a test customer
    print_step(1, "Creating test customer")
    try:
        customer = stripe.Customer.create(
            email="test.customer@example.com",
            name="Test Customer",
            description="Mock customer for testing",
            metadata={
                "environment": "sandbox",
                "created_by": "setup_script",
                "test_data": "true"
            }
        )
        mock_data['customer'] = customer
        print(f"✅ Created customer: {customer.id}")
        print(f"   Email: {customer.email}")
        print(f"   Name: {customer.name}")
    except Exception as e:
        print(f"❌ Failed to create customer: {e}")
        return None
    
    # Step 2: Create a setup intent for payment method collection
    print_step(2, "Creating setup intent for payment method")
    try:
        # Create a setup intent for future payments
        setup_intent = stripe.SetupIntent.create(
            customer=customer.id,
            payment_method_types=['card'],
            usage='off_session',
            metadata={
                "test_data": "true",
                "purpose": "mock_payment_method"
            }
        )
        
        mock_data['setup_intent'] = setup_intent
        print(f"✅ Created setup intent: {setup_intent.id}")
        print(f"   Status: {setup_intent.status}")
        print(f"   Client secret: {setup_intent.client_secret}")
        print(f"   Use this client secret in your frontend to collect payment method")
        
        # Note: In a real app, the frontend would use this client secret
        # to collect the payment method. For testing, we'll continue without it.
        
    except Exception as e:
        print(f"❌ Failed to create setup intent: {e}")
        print("   Continuing without payment method setup...")
    
    # Step 3: Create a product
    print_step(3, "Creating test product")
    try:
        product = stripe.Product.create(
            name="Premium Subscription",
            description="A premium subscription service for testing",
            metadata={
                "category": "subscription",
                "test_data": "true"
            }
        )
        mock_data['product'] = product
        print(f"✅ Created product: {product.id}")
        print(f"   Name: {product.name}")
    except Exception as e:
        print(f"❌ Failed to create product: {e}")
        return None
    
    # Step 4: Create prices for the product
    print_step(4, "Creating prices for the product")
    try:
        # Monthly price
        monthly_price = stripe.Price.create(
            unit_amount=2999,  # $29.99
            currency="usd",
            recurring={"interval": "month"},
            product=product.id,
            nickname="Monthly Premium",
            metadata={"test_data": "true"}
        )
        
        # Annual price (with discount)
        annual_price = stripe.Price.create(
            unit_amount=29999,  # $299.99 (save ~$60/year)
            currency="usd",
            recurring={"interval": "year"},
            product=product.id,
            nickname="Annual Premium",
            metadata={"test_data": "true"}
        )
        
        mock_data['monthly_price'] = monthly_price
        mock_data['annual_price'] = annual_price
        print(f"✅ Created monthly price: {monthly_price.id} (${monthly_price.unit_amount/100}/month)")
        print(f"✅ Created annual price: {annual_price.id} (${annual_price.unit_amount/100}/year)")
    except Exception as e:
        print(f"❌ Failed to create prices: {e}")
        return None
    
    # Step 5: Create a subscription
    print_step(5, "Creating test subscription")
    try:
        # Create subscription without payment method (will be in incomplete status)
        subscription = stripe.Subscription.create(
            customer=customer.id,
            items=[{"price": monthly_price.id}],
            payment_behavior='default_incomplete',
            payment_settings={
                'save_default_payment_method': 'on_subscription'
            },
            expand=['latest_invoice.payment_intent'],
            metadata={
                "test_data": "true",
                "subscription_type": "premium"
            }
        )
        mock_data['subscription'] = subscription
        print(f"✅ Created subscription: {subscription.id}")
        print(f"   Status: {subscription.status}")
        if subscription.status == 'incomplete':
            print(f"   Payment intent: {subscription.latest_invoice.payment_intent.id}")
            print(f"   Client secret: {subscription.latest_invoice.payment_intent.client_secret}")
        else:
            print(f"   Current period: {datetime.fromtimestamp(subscription.current_period_start)} to {datetime.fromtimestamp(subscription.current_period_end)}")
            if hasattr(subscription, 'latest_invoice') and subscription.latest_invoice:
                print(f"   Latest invoice: {subscription.latest_invoice.id}")
    except Exception as e:
        print(f"❌ Failed to create subscription: {e}")
        return None
    
    # Step 6: Create a one-time payment intent
    print_step(6, "Creating test payment intent")
    try:
        payment_intent = stripe.PaymentIntent.create(
            amount=4999,  # $49.99
            currency="usd",
            customer=customer.id,
            automatic_payment_methods={
                'enabled': True,
            },
            description="One-time premium feature purchase",
            metadata={
                "test_data": "true",
                "purchase_type": "one_time_feature"
            }
        )
        mock_data['payment_intent'] = payment_intent
        print(f"✅ Created payment intent: {payment_intent.id}")
        print(f"   Amount: ${payment_intent.amount/100}")
        print(f"   Status: {payment_intent.status}")
        print(f"   Client secret: {payment_intent.client_secret}")
    except Exception as e:
        print(f"❌ Failed to create payment intent: {e}")
        return None
    
    # Step 7: Create an invoice (for the subscription)
    print_step(7, "Creating test invoice")
    try:
        # Create an invoice item first
        invoice_item = stripe.InvoiceItem.create(
            customer=customer.id,
            amount=1999,  # $19.99 setup fee
            currency="usd",
            description="Setup fee for premium subscription",
            metadata={"test_data": "true"}
        )
        
        # Create the invoice
        invoice = stripe.Invoice.create(
            customer=customer.id,
            description="Premium subscription setup",
            metadata={
                "test_data": "true",
                "invoice_type": "setup"
            }
        )
        
        # Finalize the invoice
        invoice = stripe.Invoice.finalize_invoice(invoice.id)
        
        mock_data['invoice'] = invoice
        print(f"✅ Created invoice: {invoice.id}")
        print(f"   Amount: ${invoice.amount_due/100}")
        print(f"   Status: {invoice.status}")
    except Exception as e:
        print(f"❌ Failed to create invoice: {e}")
        return None
    
    return mock_data

def display_summary(existing_data, mock_data):
    """Display a summary of all data in the environment"""
    print_section("ENVIRONMENT SUMMARY")
    
    print("\n📊 EXISTING DATA SUMMARY:")
    print(f"   Customers: {len(existing_data.get('customers', []))}")
    print(f"   Payment Methods: {len(existing_data.get('payment_methods', []))}")
    print(f"   Products: {len(existing_data.get('products', []))}")
    print(f"   Prices: {len(existing_data.get('prices', []))}")
    print(f"   Subscriptions: {len(existing_data.get('subscriptions', []))}")
    print(f"   Invoices: {len(existing_data.get('invoices', []))}")
    print(f"   Payment Intents: {len(existing_data.get('payment_intents', []))}")
    
    if mock_data:
        print("\n🆕 NEWLY CREATED MOCK DATA:")
        print(f"   Customer ID: {mock_data.get('customer', {}).get('id', 'N/A')}")
        print(f"   Setup Intent ID: {mock_data.get('setup_intent', {}).get('id', 'N/A')}")
        print(f"   Product ID: {mock_data.get('product', {}).get('id', 'N/A')}")
        print(f"   Monthly Price ID: {mock_data.get('monthly_price', {}).get('id', 'N/A')}")
        print(f"   Annual Price ID: {mock_data.get('annual_price', {}).get('id', 'N/A')}")
        print(f"   Subscription ID: {mock_data.get('subscription', {}).get('id', 'N/A')}")
        print(f"   Payment Intent ID: {mock_data.get('payment_intent', {}).get('id', 'N/A')}")
        print(f"   Invoice ID: {mock_data.get('invoice', {}).get('id', 'N/A')}")
    
    print("\n🔗 OBJECT RELATIONSHIPS:")
    if mock_data:
        customer_id = mock_data.get('customer', {}).get('id', 'N/A')
        print(f"   Customer ({customer_id}) has:")
        print(f"     → Setup Intent: {mock_data.get('setup_intent', {}).get('id', 'N/A')}")
        print(f"     → Subscription: {mock_data.get('subscription', {}).get('id', 'N/A')}")
        print(f"     → Payment Intent: {mock_data.get('payment_intent', {}).get('id', 'N/A')}")
        print(f"     → Invoice: {mock_data.get('invoice', {}).get('id', 'N/A')}")
        
        product_id = mock_data.get('product', {}).get('id', 'N/A')
        print(f"   Product ({product_id}) has:")
        print(f"     → Monthly Price: {mock_data.get('monthly_price', {}).get('id', 'N/A')}")
        print(f"     → Annual Price: {mock_data.get('annual_price', {}).get('id', 'N/A')}")

def save_data_to_file(existing_data, mock_data):
    """Save all data to a JSON file for reference"""
    print_step("FINAL", "Saving data summary to file")
    
    summary_data = {
        "timestamp": datetime.now().isoformat(),
        "existing_data_counts": {
            "customers": len(existing_data.get('customers', [])),
            "payment_methods": len(existing_data.get('payment_methods', [])),
            "products": len(existing_data.get('products', [])),
            "prices": len(existing_data.get('prices', [])),
            "subscriptions": len(existing_data.get('subscriptions', [])),
            "invoices": len(existing_data.get('invoices', [])),
            "payment_intents": len(existing_data.get('payment_intents', []))
        },
        "mock_data_ids": {}
    }
    
    if mock_data:
        summary_data["mock_data_ids"] = {
            "customer_id": mock_data.get('customer', {}).get('id'),
            "setup_intent_id": mock_data.get('setup_intent', {}).get('id'),
            "product_id": mock_data.get('product', {}).get('id'),
            "monthly_price_id": mock_data.get('monthly_price', {}).get('id'),
            "annual_price_id": mock_data.get('annual_price', {}).get('id'),
            "subscription_id": mock_data.get('subscription', {}).get('id'),
            "payment_intent_id": mock_data.get('payment_intent', {}).get('id'),
            "invoice_id": mock_data.get('invoice', {}).get('id')
        }
    
    with open('stripe_environment_summary.json', 'w') as f:
        json.dump(summary_data, f, indent=2)
    
    print(f"✅ Data summary saved to 'stripe_environment_summary.json'")

def main():
    """Main execution function"""
    print_section("STRIPE SANDBOX ENVIRONMENT SETUP")
    print("This script will check your Stripe sandbox environment and create mock data if needed.")
    print("All created objects will be linked together with proper relationships.")
    
    # Step 1: Verify Stripe connection
    print_step("SETUP", "Verifying Stripe connection")
    if not check_stripe_connection():
        return
    
    # Step 2: Check existing data
    existing_data = check_existing_data()
    
    # Step 3: Determine if we need to create mock data
    needs_mock_data = (
        len(existing_data.get('customers', [])) == 0 or
        len(existing_data.get('products', [])) == 0 or
        len(existing_data.get('prices', [])) == 0
    )
    
    mock_data = None
    if needs_mock_data:
        print(f"\n🔄 Your environment has minimal data. Creating comprehensive mock data...")
        mock_data = create_mock_data()
    else:
        print(f"\n✅ Your environment already has data. Skipping mock data creation.")
        print(f"   If you want to create additional mock data, delete some existing objects first.")
    
    # Step 4: Display summary
    display_summary(existing_data, mock_data)
    
    # Step 5: Save summary to file
    save_data_to_file(existing_data, mock_data)
    
    print_section("SETUP COMPLETE")
    print("Your Stripe sandbox environment is ready!")
    print("\n📋 NEXT STEPS:")
    print("1. Check the 'stripe_environment_summary.json' file for all object IDs")
    print("2. Use these IDs in your application for testing")
    print("3. Visit your Stripe Dashboard to see all created objects")
    print("4. Run this script again anytime to check the current state")

if __name__ == "__main__":
    main() 