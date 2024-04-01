import unittest

class Artwork:
    def __init__(self, title, artist, date_of_creation, historical_significance, exhibition_location):
        self.title = title
        self.artist = artist
        self.date_of_creation = date_of_creation
        self.historical_significance = historical_significance
        self.exhibition_location = exhibition_location

class Exhibition:
    def __init__(self, name, location, start_date, end_date):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.artworks = []  # Aggregation: Exhibition has Artworks

    def add_artwork(self, artwork):
        self.artworks.append(artwork)

class Ticket:
    def __init__(self, price):
        self.price = price

    def calculate_price(self):
        return self.price

class Visitor:
    def __init__(self, name, age, national_id):
        self.name = name
        self.age = age
        self.national_id = national_id
        self.ticket = None  # Composition: Visitor owns a Ticket

    def purchase_ticket(self, ticket):
        self.ticket = ticket

class GroupVisitor:
    def __init__(self, members, guide, tour_date):
        self.members = members
        self.guide = guide
        self.tour_date = tour_date
        self.ticket = None  # Composition: GroupVisitor owns a Ticket

    def purchase_group_ticket(self, ticket):
        self.ticket = ticket

class SpecialEvent:
    def __init__(self, name, location, date, ticket_price):
        self.name = name
        self.location = location
        self.date = date
        self.ticket_price = ticket_price

def calculate_ticket_price(age, price):
    # Consider additional logic here if needed
    if 18 <= age <= 60:
        return price + (price * 0.05)  # Apply VAT for adults
    elif age < 18 or age > 60:
        return 0  # Free ticket for children, teachers, students, and seniors
    else:
        return None  # Invalid age

class MuseumSystem:
    def __init__(self):
        self.artworks = []
        self.exhibitions = []

    def add_artwork(self, artwork_data):
        artwork = Artwork(**artwork_data)
        self.artworks.append(artwork)
        return True

    def open_exhibition(self, exhibition_data):
        exhibition = Exhibition(**exhibition_data)
        self.exhibitions.append(exhibition)
        return True

    def purchase_ticket(self, ticket_data):
        visitor = Visitor(ticket_data['visitor_name'], ticket_data['age'], '123456789')
        ticket_price = calculate_ticket_price(visitor.age, 63)  # Default ticket price
        ticket = Ticket(ticket_price)
        visitor.purchase_ticket(ticket)
        return ticket

    def purchase_group_ticket(self, group_ticket_data):
        group_visitor = GroupVisitor(group_ticket_data['group_size'], group_ticket_data['guide_name'],
                                     group_ticket_data['tour_date'])
        ticket_price = calculate_ticket_price(25, 63)  # Assume the age of the group members is 25
        ticket = Ticket(ticket_price)
        group_visitor.purchase_group_ticket(ticket)
        return ticket

    def display_payment_receipt(self, ticket):
        return f"Payment Receipt: Price {ticket.calculate_price()} AED"

class TestMuseumSystem(unittest.TestCase):
    def setUp(self):
        # Initialize the Museum System
        self.museum_system = MuseumSystem()

    def test_add_new_artwork(self):
        # Test the addition of new art to the museum
        artwork_data = {
            "title": "Starry Night",
            "artist": "Vincent van Gogh",
            "date_of_creation": "1889",
            "historical_significance": "Iconic painting",
            "exhibition_location": "Permanent Gallery"
        }
        result = self.museum_system.add_artwork(artwork_data)
        self.assertTrue(result)
        # Check if the artwork was added successfully
        self.assertEqual(len(self.museum_system.artworks), 1)


    def test_open_new_exhibition(self):
        # Test the opening of a new exhibition at the museum
        exhibition_data = {
            "name": "Impressionism Exhibition",
            "location": "Exhibition Hall 1",
            "start_date": "2024-04-01",
            "end_date": "2024-06-30"
        }
        result = self.museum_system.open_exhibition(exhibition_data)
        self.assertTrue(result)
        # Check if the exhibition was opened successfully
        self.assertEqual(len(self.museum_system.exhibitions), 1)

    def test_purchase_tickets(self):
        # Test the purchase of tickets by an individual
        individual_ticket_data = {
            "visitor_name": "John Doe",
            "age": 30,
            "ticket_type": "Adult",
            "event_name": "Impressionism Exhibition"
        }
        individual_receipt = self.museum_system.purchase_ticket(individual_ticket_data)
        self.assertIsNotNone(individual_receipt)

        # Test the purchase of tickets by a tour group
        group_ticket_data = {
            "group_name": "School Group",
            "group_size": 25,
            "guide_name": "Tour Guide A",
            "event_name": "Impressionism Exhibition",
            "tour_date": "2024-05-15"  # Adding the tour_date key
        }
        group_receipt = self.museum_system.purchase_group_ticket(group_ticket_data)
        self.assertIsNotNone(group_receipt)

        def test_display_payment_receipt(self):
            # Test the display of payment receipts for purchasing tickets
            individual_ticket_data = {
                "visitor_name": "Jane Smith",
                "age": 25,
                "ticket_type": "Adult",
                "event_name": "Impressionism Exhibition"
            }
            individual_receipt = self.museum_system.purchase_ticket(individual_ticket_data)

            # Display payment receipt for individual ticket purchase
            receipt_display = self.museum_system.display_payment_receipt(individual_receipt)
            self.assertIsNotNone(receipt_display)

    if __name__ == '__main__':
        unittest.main()

