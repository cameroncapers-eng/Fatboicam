
# --------------------------------------------------
# .insert()
# --------------------------------------------------
print("2. .insert()")
from abc import ABC


class FruitCollection(ABC):
	"""Abstract base for fruit collections."""

	def __init__(self, items: list[str] | None = None) -> None:
		self._items: list[str] = list(items) if items else []

	def insert(self, index: int, value: str) -> None:
		# allow negative and out-of-range indices consistent with list.insert
		self._items.insert(index, value)

	def append(self, value: str) -> None:
		self._items.append(value)

	def remove(self, value: str) -> None:
		# raise ValueError if not present, like list.remove
		self._items.remove(value)

	def to_list(self) -> list[str]:
		return list(self._items)

	def __len__(self) -> int:
		"""Return number of items in the collection."""
		return len(self._items)

	def __contains__(self, item: str) -> bool:
		"""Support the `in` operator."""
		return item in self._items

	def __iter__(self):
		"""Iterate over items in the collection."""
		return iter(self._items)

	def __repr__(self) -> str:
		return f"{self.__class__.__name__}({self._items!r})"


class fruits(FruitCollection):
	"""Concrete implementation of a fruit collection backed by a list."""

	def __init__(self, items: list[str] | None = None) -> None:
		self._items: list[str] = list(items) if items else []

	def insert(self, index: int, value: str) -> None:
		# allow negative and out-of-range indices consistent with list.insert
		self._items.insert(index, value)

	def append(self, value: str) -> None:
		self._items.append(value)

	def remove(self, value: str) -> None:
		# raise ValueError if not present, like list.remove
		self._items.remove(value)

	def to_list(self) -> list[str]:
		return list(self._items)

	# useful dunder methods proxied to the internal list
	def __len__(self) -> int:
		return len(self._items)

	def __contains__(self, item: str) -> bool:
		return item in self._items

	def __iter__(self):
		return iter(self._items)

	def __repr__(self) -> str:
		return f"{self.__class__.__name__}({self._items!r})"


# demonstration using the concrete class
fruits_list = fruits(["cannalope", "Grapes", "Blueberry"])
fruits_list.insert(1, "cherry")
print("After insert(1, 'cherry'):")
print(fruits_list.to_list())
print()

