import calendar
import datetime
from typing import Any
from collections import abc

class Event:   
	@property
	def name(self) -> str:
		return self.__name
	
	@property
	def start(self) -> datetime.datetime:
		return self.__start
	
	@property
	def end(self) -> datetime.datetime:
		return self.__end

	def __init__(self, name: str, start: datetime.datetime, end: datetime.datetime):
		"""Initialises the Event class

		Args:
			name (str): The name of the event
			start (datetime.datetime): The start date and time of the event
			end (datetime.datetime): The end date and time of the event

		Raises:
			TypeError: If the name argument is not a string
			TypeError: If the start argument is not a datetime
			TypeError: If the end argument is not a datetime
		"""              
		
		if not isinstance(name, str):
			raise TypeError(f"Name must be a string, not {type(name)}")
		self.__name = name
		
		if not isinstance(start, datetime.datetime):
			raise TypeError(f"Start must be a datetime, not {type(start)}")
		self.__start = start
		
		if not isinstance(end, datetime.datetime):
			raise TypeError(f"End must be a datetime, not {type(end)}")
		self.__end = end

	def __repr__(self) -> str:
		return f'Event(name={self.name}, start={self.start}, end={self.end})'
	
	def __str__(self) -> str:
		return f"  {self.name}:\n    Start: {self.start:%Y-%m-%d %H:%M}\n    End: {self.end:%Y-%m-%d %H:%M}"
	
	def __eq__(self, __value: object) -> bool:
		""" 
		Returns True if the name, start, and end of the current Event object is equal to the name, start, and end of the other Event object.  
		>>> e1 = Event('event1', datetime.datetime(2022, 1, 1), datetime.datetime(2022, 1, 2))
		>>> e2 = Event('event1', datetime.datetime(2022, 1, 1), datetime.datetime(2022, 1, 2))
		>>> e3 = Event('event2', datetime.datetime(2022, 1, 1), datetime.datetime(2022, 1, 2))
		>>> e4 = Event('event1', datetime.datetime(2022, 1, 2), datetime.datetime(2022, 1, 3))
		>>> e1 == e2
		True
		>>> e1 == e3
		False
		>>> e1 == e4
		False"""

		if not isinstance(__value, Event):
			return NotImplemented
		
		return self.name == __value.name and self.start == __value.start and self.end == __value.end
	
	def __lt__(self, __value: object) -> bool:
		"""Returns True if the start time of the first event is before the start time of the second event, False otherwise.
		
		>>> Event('e1', datetime.datetime(2021,1,1), datetime.datetime(2021,1,2)) < Event('e2', datetime.datetime(2021,1,2), datetime.datetime(2021,1,3)) 
		... #e1 starts before e2
		True
		
		>>> Event('e1', datetime.datetime(2021,1,2), datetime.datetime(2021,1,3)) < Event('e2', datetime.datetime(2021,1,1), datetime.datetime(2021,1,2)) 
		... #e1 starts after e2
		False
		
		>>> Event('e1', datetime.datetime(2021,1,1), datetime.datetime(2021,1,2)) < Event('e2', datetime.datetime(2021,1,1), datetime.datetime(2021,1,2))
		... #e1 starts at the same time as e2
		False"""

		if not isinstance(__value, Event):
			return NotImplemented
		
		return self.start < __value.start
	
	def __le__(self, __value: object) -> bool:
		"""Returns True if the start time of the first event is before or at the same time as the start time of the second event, False otherwise.
		
		>>> Event('e1', datetime.datetime(2021,1,1), datetime.datetime(2021,1,2)) <= Event('e2', datetime.datetime(2021,1,2), datetime.datetime(2021,1,3)) 
		... #e1 starts before e2
		True
		
		>>> Event('e1', datetime.datetime(2021,1,2), datetime.datetime(2021,1,3)) <= Event('e2', datetime.datetime(2021,1,1), datetime.datetime(2021,1,2)) 
		... #e1 starts after e2
		False
		
		>>> Event('e1', datetime.datetime(2021,1,1), datetime.datetime(2021,1,2)) <= Event('e2', datetime.datetime(2021,1,1), datetime.datetime(2021,1,2))
		... #e1 starts at the same time as e2
		True"""

		if not isinstance(__value, Event):
			return NotImplemented
		
		return self.start <= __value.start
	
	def __gt__(self, __value: object) -> bool:
		"""Returns True if the start time of the first event is after the start time of the second event, False otherwise.

		>>> Event('e1', datetime.datetime(2021,1,1), datetime.datetime(2021,1,2)) > Event('e2', datetime.datetime(2021,1,2), datetime.datetime(2021,1,3)) 
		... #e1 starts before e2
		False
		
		>>> Event('e1', datetime.datetime(2021,1,2), datetime.datetime(2021,1,3)) > Event('e2', datetime.datetime(2021,1,1), datetime.datetime(2021,1,2)) 
		... #e1 starts after e2
		True
		
		>>> Event('e1', datetime.datetime(2021,1,1), datetime.datetime(2021,1,2)) > Event('e2', datetime.datetime(2021,1,1), datetime.datetime(2021,1,2))
		... #e1 starts at the same time as e2
		False"""

		if not isinstance(__value, Event):
			return NotImplemented
		
		return self.start > __value.start
	
	def __ge__(self, __value: object) -> bool:
		"""Returns True if the start time of the first event is after or at the same time as the start time of the second event, False otherwise.

		>>> Event('e1', datetime.datetime(2021,1,1), datetime.datetime(2021,1,2)) >= Event('e2', datetime.datetime(2021,1,2), datetime.datetime(2021,1,3)) 
		... #e1 starts before e2
		False
		
		>>> Event('e1', datetime.datetime(2021,1,2), datetime.datetime(2021,1,3)) >= Event('e2', datetime.datetime(2021,1,1), datetime.datetime(2021,1,2)) 
		... #e1 starts after e2
		True
		
		>>> Event('e1', datetime.datetime(2021,1,1), datetime.datetime(2021,1,2)) >= Event('e2', datetime.datetime(2021,1,1), datetime.datetime(2021,1,2))
		... #e1 starts at the same time as e2
		True"""

		if not isinstance(__value, Event):
			return NotImplemented
		
		return self.start >= __value.start
	
	def __ne__(self, __value: object) -> bool:
		"""
		Returns True if the name, start, or end of the current Event object is not equal to the name, start, or end of the other Event object.

		>>> e1 = Event("e1", datetime.datetime(2022, 1, 1), datetime.datetime(2022, 1, 31))
		>>> e2 = Event("e2", datetime.datetime(2022, 1, 1), datetime.datetime(2022, 1, 30))
		>>> e1 != e2
		True

		>>> e1 = Event("e1", datetime.datetime(2022, 1, 1), datetime.datetime(2022, 1, 31))
		>>> e2 = Event("e1", datetime.datetime(2022, 1, 1), datetime.datetime(2022, 1, 31))
		>>> e1 != e2
		False
		"""

		if not isinstance(__value, Event):
			return NotImplemented

		return self.name != __value.name or self.start != __value.start or self.end != __value.end
	
	def __hash__(self) -> int:
		return hash((self.name, self.start, self.end))
	
class EventSet(set):
	"""A set of Events, used to create Calendar objects and store Events. 
	It must be instantiated with an iterable of Events, if not, returning a TypeError.
	"""

	def __init__(self, events: abc.Iterable=list()):
		"""Initialises the EventSet class

		Args:
			events (abc.Iterable, optional): An iterable of events. Defaults to list().

		Raises:
			TypeError: If events is not an iterable
			TypeError: If any item in iterable events is not an Event
				
		>>> e = EventSet(20)
		Traceback (most recent call last):
		...
		TypeError: Events must be an iterable, not <class 'int'>

		>>> e = EventSet('some string')
		Traceback (most recent call last):
		...
		TypeError: Events must be an iterable of Events, not <class 'str'>
		
		>>> e = EventSet({Event('Tennis with Frank', datetime.datetime(2020,1,1), datetime.datetime(2020,1,2))})
		"""

		if not isinstance(events, abc.Iterable):
			raise TypeError(f"Events must be an iterable, not {type(events)}")
		
		for x in events: #there has to be a way to do this that doesn't iterate over every item, right?
			if not isinstance(x, Event):
				raise TypeError(f"Events must be an iterable of Events, not {type(x)}")
			
		super().__init__(events)

	def __repr__(self) -> str:
		return 'EventList:\n'+',\n'.join(['    '+repr(event) for event in self])
	
class SharedCalendar(calendar.Calendar):
	@property
	def events(self):
		return self.__events

	def __init__(self, name: str='', events: abc.Iterable=list()):
		"""Initialises the SharedCalendar class, which is a calendar that stores Events. It must be instantiated with an iterable of Events, if not, returning a TypeError.

		Args:
			name (str, optional): The name of the SharedCalendar object. Defaults to ''.
			events (abc.Iterable, optional): An iterable filled with events to be added to the calendar. Defaults to list().

		Raises:
			TypeError: If the name argument is not a string, or if the events argument is not an iterable.
			
		>>> e = SharedCalendar(20, [])
		Traceback (most recent call last):
		...
		TypeError: Name must be a string, not <class 'int'>
		
		>>> e = SharedCalendar('calendar', 1)
		Traceback (most recent call last):
		...
		TypeError: Events must be an iterable, not <class 'int'>"""        
		super().__init__()
		
		if not isinstance(name, str):
			raise TypeError(f"Name must be a string, not {type(name)}")
		self.name = name

		if not isinstance(events, abc.Iterable):
			raise TypeError(f"Events must be an iterable, not {type(events)}")

		self.__events = EventSet(events)

	def __repr__(self) -> str:
		return super().__repr__()
	
	def __str__(self) -> str:
		event_string = [str(event) for event in sorted(self.__events)] #Sorts the events by start time
		return f"{self.name}:\n" + '\n'.join(event_string)
	
	def add_event(self, event: Event) -> None:
		"""Adds the event given to the calendar.

		Args:
			event (Event): The event to be added to the calendar

		Raises:
			TypeError: If the event argument is not an Event
		"""        
		if not isinstance(event, Event):
			raise TypeError(f"Event must be an Event, not {type(event)}")
		
		self.__events.add(event)

	def remove_event(self, event: Event) -> None:
		"""Removes the event given from the calendar, if it exists.

		Args:
			event (Event): The event to be removed from the calendar

		Raises:
			TypeError: If the event argument is not an Event
		"""        
		if not isinstance(event, Event):
			raise TypeError(f"Event must be an Event, not {type(event)}")
		
		self.__events.discard(event)

	def events_between(self, start: datetime.datetime, end: datetime.datetime) -> list[Event]:
		"""
		Returns a list of events that occur between the start and end times given.

		Args:
			start (datetime.datetime): The start time of the time span to find events in.
			end (datetime.datetime): The end time of the time span.

		Returns:
			list[Event]: The list of events in the time span

		Raises:
			TypeError: If start or end is not a datetime.datetime object.

		>>> e = SharedCalendar("Sam's Calendar", {Event('Tennis with Frank', datetime.datetime(2020,1,1), datetime.datetime(2020,1,2)), Event('Tennis with Frank 2', datetime.datetime(2020,1,3), datetime.datetime(2020,1,4))})
		
		>>> e.events_between(datetime.datetime(2019,12,31), datetime.datetime(2020,1,1,6))
		[Event(name=Tennis with Frank, start=2020-01-01 00:00:00, end=2020-01-02 00:00:00)]
		"""
		if not isinstance(start, datetime.datetime):
			raise TypeError(f"start must be a datetime.datetime, not {type(start)}")
		if not isinstance(end, datetime.datetime):
			raise TypeError(f"end must be a datetime.datetime, not {type(end)}")
		return [event for event in self.__events if 
				start <= event.start < end
				or start < event.end <= end
				or event.start <= start < event.end
				or event.start < end <= event.end]
		
	def has_conflicts(self) -> bool:
		"""Returns True if there are any conflicting events in the calendar, False otherwise.

		Returns:
			bool: True if there are any conflicting events in the calendar, False otherwise.

		>>> e = SharedCalendar("Sam's Calendar", {Event('Tennis with Frank', datetime.datetime(2020,1,1), datetime.datetime(2020,1,2)), Event('Tennis with Frank 2', datetime.datetime(2020,1,3), datetime.datetime(2020,1,4))})
		>>> e.has_conflicts()
		False
  
		>>> e = SharedCalendar("Sam's Calendar 2", {Event('Tennis with Frank', datetime.datetime(2020,1,1), datetime.datetime(2020,1,2)), Event('Tennis with Frank 2', datetime.datetime(2020,1,1), datetime.datetime(2020,1,4))})
		>>> e.has_conflicts()
		True
		"""	
  		  
		return any(bool([e for e in self.events_between(event.start, event.end) if e != event]) for event in self.events)
		#this could use refactoring probably to get it speedier
		
	

if __name__ == "__main__":
	import doctest
	doctest.testmod()

	e = SharedCalendar("Sam's Calendar", {Event('Tennis with Frank', datetime.datetime(2020,1,1), datetime.datetime(2020,1,2)), Event('Tennis with Dave', datetime.datetime(2020,1,3), datetime.datetime(2020,1,4))})

	print(e)