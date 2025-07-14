#!/usr/bin/env python3
"""
Test script to verify the Stripe data generator implementation.
This script tests various configurations to ensure everything works correctly.
"""

import os
import sys
import tempfile
import shutil
from main import StripeDataGenerator
from config import STRIPE_API_SECRET_KEY

def test_basic_simulation():
    """Test basic simulation mode (no API calls)."""
    print("🧪 Testing basic simulation mode...")
    
    with tempfile.TemporaryDirectory() as temp_dir:
        # Override output directory
        import config
        original_output_dir = config.OUTPUT_DIRECTORY
        config.OUTPUT_DIRECTORY = temp_dir
        
        try:
            generator = StripeDataGenerator(
                simulate_api_requests=False,
                enable_rate_limiting=False,
                enable_random_errors=False,
                error_rate=0.0,
                use_real_stripe_api=False
            )
            
            # Generate a small dataset
            data = generator.generate_all_data()
            
            # Basic validation
            assert len(data["customers"]) > 0, "No customers generated"
            assert len(data["products"]) > 0, "No products generated"
            assert len(data["prices"]) > 0, "No prices generated"
            
            print("✅ Basic simulation test passed")
            return True
            
        except Exception as e:
            print(f"❌ Basic simulation test failed: {e}")
            return False
        finally:
            config.OUTPUT_DIRECTORY = original_output_dir

def test_api_simulation():
    """Test API simulation mode."""
    print("🧪 Testing API simulation mode...")
    
    with tempfile.TemporaryDirectory() as temp_dir:
        import config
        original_output_dir = config.OUTPUT_DIRECTORY
        config.OUTPUT_DIRECTORY = temp_dir
        
        try:
            generator = StripeDataGenerator(
                simulate_api_requests=True,
                enable_rate_limiting=True,
                enable_random_errors=True,
                error_rate=0.1,  # 10% error rate for testing
                use_real_stripe_api=False
            )
            
            data = generator.generate_all_data()
            
            # Validate API simulation worked
            assert generator.api_simulator is not None, "API simulator not initialized"
            assert generator.api_stats["total_requests"] > 0, "No API requests simulated"
            assert generator.api_stats["using_real_api"] is False, "Should be using simulation"
            
            print("✅ API simulation test passed")
            return True
            
        except Exception as e:
            print(f"❌ API simulation test failed: {e}")
            return False
        finally:
            config.OUTPUT_DIRECTORY = original_output_dir

def test_real_api_setup():
    """Test real API setup (without actually calling API)."""
    print("🧪 Testing real API setup...")
    
    if not STRIPE_API_SECRET_KEY:
        print("⚠️  Skipping real API test - no STRIPE_API_SECRET_KEY found")
        return True
    
    try:
        # Test that we can initialize with real API mode
        generator = StripeDataGenerator(
            simulate_api_requests=True,
            enable_rate_limiting=True,
            enable_random_errors=False,
            error_rate=0.0,
            use_real_stripe_api=True
        )
        
        # Check that API simulator is configured for real API
        assert generator.api_simulator is not None, "API simulator not initialized"
        assert generator.api_simulator.use_real_api is True, "Should be using real API"
        
        print("✅ Real API setup test passed")
        return True
        
    except Exception as e:
        print(f"❌ Real API setup test failed: {e}")
        return False

def test_environment_variables():
    """Test environment variable handling."""
    print("🧪 Testing environment variable handling...")
    
    try:
        # Test that config loads environment variables
        from config import STRIPE_API_SECRET_KEY, STRIPE_API_PUBLISHABLE_KEY, STRIPE_API_URL
        
        # These should be loaded from environment or None
        assert STRIPE_API_URL is not None, "STRIPE_API_URL should have default value"
        
        # Test API key validation
        if STRIPE_API_SECRET_KEY:
            assert STRIPE_API_SECRET_KEY.startswith(("sk_test_", "sk_live_")), "Invalid API key format"
        
        print("✅ Environment variable test passed")
        return True
        
    except Exception as e:
        print(f"❌ Environment variable test failed: {e}")
        return False

def test_tracking_functionality():
    """Test success/failure tracking functionality."""
    print("🧪 Testing tracking functionality...")
    
    with tempfile.TemporaryDirectory() as temp_dir:
        import config
        original_output_dir = config.OUTPUT_DIRECTORY
        config.OUTPUT_DIRECTORY = temp_dir
        
        try:
            generator = StripeDataGenerator(
                simulate_api_requests=True,
                enable_rate_limiting=False,
                enable_random_errors=True,
                error_rate=0.2,  # 20% error rate to test tracking
                use_real_stripe_api=False
            )
            
            data = generator.generate_all_data()
            
            # Test tracking data
            assert generator.api_stats is not None, "API stats not collected"
            assert "total_requests" in generator.api_stats, "Missing total_requests"
            assert "successful_requests" in generator.api_stats, "Missing successful_requests"
            assert "failed_requests" in generator.api_stats, "Missing failed_requests"
            assert "error_breakdown" in generator.api_stats, "Missing error_breakdown"
            assert "endpoint_stats" in generator.api_stats, "Missing endpoint_stats"
            
            # Test that some errors occurred (with 20% error rate)
            if generator.api_stats["total_requests"] > 10:
                assert generator.api_stats["failed_requests"] > 0, "Expected some failed requests"
            
            print("✅ Tracking functionality test passed")
            return True
            
        except Exception as e:
            print(f"❌ Tracking functionality test failed: {e}")
            return False
        finally:
            config.OUTPUT_DIRECTORY = original_output_dir

def run_all_tests():
    """Run all tests."""
    print("🚀 Running Stripe Data Generator Tests")
    print("=" * 50)
    
    tests = [
        test_environment_variables,
        test_basic_simulation,
        test_api_simulation,
        test_real_api_setup,
        test_tracking_functionality
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"❌ Test {test.__name__} crashed: {e}")
            failed += 1
        print()
    
    print("=" * 50)
    print(f"📊 Test Results: {passed} passed, {failed} failed")
    
    if failed == 0:
        print("🎉 All tests passed!")
        return True
    else:
        print("❌ Some tests failed")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1) 