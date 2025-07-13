#!/usr/bin/env python3
"""
List all Stripe objects in your sandbox environment
This script provides a quick overview of all objects and their IDs for testing
"""

import stripe
import os
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

# Configure Stripe
stripe.api_key = os.getenv("STRIPE_API_SECRET_KEY")

def print_section(title):
    """Print a formatted section header"""
    print(f"\n{'='*60}")
    print(f" {title}")
    print(f"{'='*60}")

def list_customers():
    """List all customers"""
    print("\n📧 CUSTOMERS:")
    customers = stripe.Customer.list(limit=10)
    for customer in customers.data:
        print(f"   {customer.id} - {customer.email or 'No email'} ({customer.name or 'No name'})")
        if customer.metadata:
            print(f"      Metadata: {customer.metadata}")

def list_products_and_prices():
    """List all products and their prices"""
    print("\n🛍️ PRODUCTS & PRICES:")
    products = stripe.Product.list(limit=10)
    for product in products.data:
        print(f"   Product: {product.id} - {product.name}")
        if product.description:
            print(f"      Description: {product.description}")
        
        # Get prices for this product
        prices = stripe.Price.list(product=product.id, limit=10)
        for price in prices.data:
            amount = f"${price.unit_amount/100}" if price.unit_amount else "Free"
            interval = f"/{price.recurring.interval}" if price.recurring else ""
            print(f"      Price: {price.id} - {amount}{interval} ({price.currency.upper()})")

def list_subscriptions():
    """List all subscriptions"""
    print("\n📋 SUBSCRIPTIONS:")
    subscriptions = stripe.Subscription.list(limit=10, expand=['data.items.data.price'])
    for subscription in subscriptions.data:
        print(f"   {subscription.id} - Status: {subscription.status}")
        print(f"      Customer: {subscription.customer}")
        try:
            if hasattr(subscription, 'items') and subscription.items:
                for item in subscription.items.data:
                    price_info = f"{item.price.id}"
                    if hasattr(item.price, 'nickname') and item.price.nickname:
                        price_info += f" - {item.price.nickname}"
                    if hasattr(item.price, 'unit_amount') and item.price.unit_amount:
                        price_info += f" (${item.price.unit_amount/100})"
                    print(f"      Item: {price_info}")
        except Exception as e:
            print(f"      Items: Unable to retrieve ({e})")
        if subscription.status == 'incomplete' and subscription.latest_invoice:
            print(f"      Latest Invoice: {subscription.latest_invoice}")

def list_payment_intents():
    """List all payment intents"""
    print("\n💳 PAYMENT INTENTS:")
    payment_intents = stripe.PaymentIntent.list(limit=10)
    for pi in payment_intents.data:
        amount = f"${pi.amount/100}" if pi.amount else "No amount"
        print(f"   {pi.id} - {amount} ({pi.currency.upper()}) - Status: {pi.status}")
        print(f"      Customer: {pi.customer or 'No customer'}")
        if pi.description:
            print(f"      Description: {pi.description}")

def list_invoices():
    """List all invoices"""
    print("\n🧾 INVOICES:")
    invoices = stripe.Invoice.list(limit=10)
    for invoice in invoices.data:
        amount = f"${invoice.amount_due/100}" if invoice.amount_due else "No amount"
        print(f"   {invoice.id} - {amount} ({invoice.currency.upper()}) - Status: {invoice.status}")
        print(f"      Customer: {invoice.customer}")
        if hasattr(invoice, 'subscription') and invoice.subscription:
            print(f"      Subscription: {invoice.subscription}")

def list_setup_intents():
    """List all setup intents"""
    print("\n🔧 SETUP INTENTS:")
    setup_intents = stripe.SetupIntent.list(limit=10)
    for si in setup_intents.data:
        print(f"   {si.id} - Status: {si.status}")
        print(f"      Customer: {si.customer or 'No customer'}")
        if si.usage:
            print(f"      Usage: {si.usage}")

def main():
    """Main execution function"""
    print_section("STRIPE SANDBOX OBJECTS")
    print(f"Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    try:
        # Verify connection
        account = stripe.Account.retrieve()
        print(f"Account: {account.id} ({account.country})")
        
        # List all objects
        list_customers()
        list_products_and_prices()
        list_subscriptions()
        list_payment_intents()
        list_invoices()
        list_setup_intents()
        
        print_section("TESTING RECOMMENDATIONS")
        print("\n🧪 FOR TESTING YOUR APPLICATION:")
        print("1. Use the customer IDs above to test customer-related features")
        print("2. Use the product/price IDs for subscription or purchase flows")
        print("3. Use the setup intent client secrets for payment method collection")
        print("4. Use the payment intent client secrets for payment processing")
        print("5. Check incomplete subscriptions - they need payment method completion")
        
        print("\n💡 USEFUL STRIPE DASHBOARD LINKS:")
        print("- Customers: https://dashboard.stripe.com/test/customers")
        print("- Products: https://dashboard.stripe.com/test/products")
        print("- Subscriptions: https://dashboard.stripe.com/test/subscriptions")
        print("- Payment Intents: https://dashboard.stripe.com/test/payments")
        print("- Invoices: https://dashboard.stripe.com/test/invoices")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main() 