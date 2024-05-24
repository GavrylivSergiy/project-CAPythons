from abc import ABC, abstractmethod
from typing import Dict
from app.entities import Record, Field, AddressBook, Name, NotesBook
import uuid
from presentation.messages import Message


# Базовий клас для команд. Кожна команда повинна реалізовувати метод 'execute'
# review: Creating a class every command and every time the command is called
# seems a bit wasteful in terms of resources spent.
# I would prefer one class with all commands, created once

class Command(ABC):
    exit_command_flag = False

    def __init__(self, address_book: AddressBook | NotesBook,
                 #  notes_book: NotesBook
                 ):
        self.address_book = address_book
        # self.notes_book = notes_book

    @abstractmethod
    def execute(self, *args: str) -> None:
        pass


# Базовий клас для команд, що працюють з полями (Field). Він наслідує від 'Command' і додає специфічні методи для роботи з полями.
class FieldCommand(Command, ABC):
    @abstractmethod
    def execute_field(self, record: Record, field: Field) -> None:
        pass

    def execute(self, *args: str) -> None:
        if len(args) < 2:
            Message.error("incorrect_arguments")
            return
        name, *field_args = args
        record = self.address_book.find_by_name(Name(name))
        if not record:
            Message.error("contact_not_found", name=name)
            return

        field = self.create_field(*field_args)
        self.execute_field(record, field)

    @abstractmethod
    def create_field(self, *args: str) -> Field:
        pass


# Інтерфейс для класів, які будуть відповідати за збереження і завантаження контактів.
class StorageInterface(ABC):
    @abstractmethod
    def save_contacts(self, contacts: Dict[uuid.UUID, Record]) -> None:
        pass

    @abstractmethod
    def load_contacts(self) -> Dict[uuid.UUID, Record]:
        pass
