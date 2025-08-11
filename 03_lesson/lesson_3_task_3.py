from address import Address
from mailing import Mailing

to_address = Address("83020", "Донецк", "Артема", "21", "32")
from_address = Address("86037", "Макеевка", "Строителя", "10", "27")

mailing = Mailing(to_address, from_address, 670, "TRK564897")
print(mailing)
