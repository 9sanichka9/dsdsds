class InvalidSeatNumberError(Exception):
    pass


class Ticket:
    def __init__(self, movie_title, seat_number, price):
        if not (1 <= seat_number <= 100):
            raise InvalidSeatNumberError(f"Некоректний номер місця: {seat_number}. Має бути від 1 до 100.")
        self.movie_title = movie_title
        self.seat_number = seat_number
        self.price = price

    def display_info(self):
        return f"Фільм: {self.movie_title}, Місце: {self.seat_number}, Ціна: {self.price} грн"


class StandardTicket(Ticket):
    def __init__(self, movie_title, seat_number, price, discount=0):
        super().__init__(movie_title, seat_number, price)
        self.discount = discount

    def display_info(self):
        info = super().display_info()
        if self.discount > 0:
            info += f", Знижка: {self.discount}%"
        return info


class VIPticket(Ticket):
    def __init__(self, movie_title, seat_number, price, lounge_access=True, complimentary_drinks=1):
        super().__init__(movie_title, seat_number, price)
        self.lounge_access = lounge_access
        self.complimentary_drinks = complimentary_drinks

    def display_info(self):
        info = super().display_info()
        info += f", VIP-зона: {'є' if self.lounge_access else 'немає'}, Напої: {self.complimentary_drinks}"
        return info


class Cinema:
    def __init__(self):
        self.tickets = []

    def add_ticket(self, ticket):
        try:
            if not isinstance(ticket, Ticket):
                raise ValueError("Об'єкт не є типом Ticket.")
            self.tickets.append(ticket)
        except InvalidSeatNumberError as e:
            print(f"Помилка: {e}")
        except Exception as e:
            print(f"Сталася помилка при створенні квитка: {e}")

    def display_all_tickets(self):
        if not self.tickets:
            print("Немає виданих квитків.")
        for ticket in self.tickets:
            print(ticket.display_info())


if __name__ == "__main__":
    cinema = Cinema()

    try:
        ticket1 = StandardTicket("Інтерстеллар", 15, 120, discount=10)
        ticket2 = VIPticket("Аватар", 50, 250, lounge_access=True, complimentary_drinks=3)
        ticket3 = StandardTicket("Месники", 101, 100)
    except InvalidSeatNumberError as e:
        print(f"Помилка: {e}")

    cinema.add_ticket(ticket1)
    cinema.add_ticket(ticket2)

    cinema.display_all_tickets()
