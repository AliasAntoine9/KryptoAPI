"""Create an API with Flask: Flask table"""

from sqlalchemy import create_engine, Column, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from table_handler.config import DB_URI

ENGINE = create_engine(DB_URI)
SESSION = sessionmaker(bind=ENGINE)()
BASE = declarative_base()


class VetClosedPositions(BASE):
	"""Table VET closed positions"""
	__tablename__ = "vet_closed_positions"

	buy_timestamp = Column(String(120), nullable=False, primary_key=True, unique=True)
	price_when_bought = Column(Float(), nullable=False)
	price_to_sale = Column(Float(), nullable=False)
	sold_timestamp = Column(String(120), nullable=False)
	price_when_sold = Column(Float(), nullable=False)


def add_closed_position(
		buy_timestamp,
		price_when_bought,
		price_to_sale,
		sold_timestamp,
		price_when_sold,
		) -> bool:
	"""This method is adding a new closed position in vet_closed_positions table"""
	try:
		closed_positions = VetClosedPositions(
			buy_timestamp=buy_timestamp,
			price_when_bought=price_when_bought,
			price_to_sale=price_to_sale,
			sold_timestamp=sold_timestamp,
			price_when_sold=price_when_sold,
		)
		SESSION.add(closed_positions)
		SESSION.commit()
		return True

	except Exception as e:
		print(e)
		return False
