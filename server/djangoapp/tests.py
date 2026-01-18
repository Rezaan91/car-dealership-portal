from django.test import TestCase
from django.contrib.auth.models import User
from .models import CarMake, CarModel, Dealer, Review


class CarMakeTestCase(TestCase):
    def setUp(self):
        CarMake.objects.create(name="Toyota", description="Japanese automobile manufacturer")

    def test_car_make_creation(self):
        toyota = CarMake.objects.get(name="Toyota")
        self.assertEqual(toyota.description, "Japanese automobile manufacturer")


class DealerTestCase(TestCase):
    def setUp(self):
        Dealer.objects.create(
            name="Test Motors",
            address="123 Test St",
            city="Test City",
            state="Test State",
            zip_code="12345",
            phone="123-456-7890",
            email="test@testmotors.com"
        )

    def test_dealer_creation(self):
        dealer = Dealer.objects.get(name="Test Motors")
        self.assertEqual(dealer.city, "Test City")
        self.assertEqual(dealer.state, "Test State")


class ReviewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.dealer = Dealer.objects.create(
            name="Test Motors",
            address="123 Test St",
            city="Test City",
            state="Test State",
            zip_code="12345",
            phone="123-456-7890",
            email="test@testmotors.com"
        )

    def test_review_creation(self):
        review = Review.objects.create(
            dealer=self.dealer,
            customer=self.user,
            purchase=True,
            review_text="Great service!",
            sentiment="positive"
        )
        self.assertEqual(review.sentiment, "positive")
        self.assertTrue(review.purchase)
