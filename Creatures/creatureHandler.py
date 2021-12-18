from uuid import UUID

from DandData.creature import Creature
from pyzmqServer.client import Client

from DandData.action import Action
from ServerHandler.Handler import Handler



class CreatureHandler(Handler):

    def __init__(self, connection: Client) -> None:
        super().__init__(connection)

    def addCreature(self, creatureType: str) -> None:
        print("Adding creature", creatureType)

        answer = self.connection.SendRequest("add creature", creatureType)

        if answer[0] == False:
            print("could not create creature: '", answer[1], "'")

    def UseAction(self, creatureId: int, action: Action) -> None:
        targets: list[tuple[str, UUID]] = [(self.connection.clientName, creatureId)] # target for now is self
        
        data = (creatureId, action.name, targets)
        print("Using action", action.name)

        answer = self.connection.SendRequest("use action", data)

        if answer[0] == False:
            print("could not use action: '", answer[1], "'")