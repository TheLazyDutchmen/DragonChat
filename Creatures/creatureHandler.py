from Creatures.Actions.Action import Action
from ServerHandler.Handler import Handler
class CreatureHandler(Handler):

    def addCreature(self, creatureType: str):
        data = (self.groupName, self.userName, creatureType)
        print("Adding creature", creatureType)

        answer = self.SendServerMessage("addCreature", data)

        return answer[0]

    def UseAction(self, creatureId: int, action: Action):
        data = (self.groupName, self.userName, creatureId, action)
        print("Using action", action.name)

        answer = self.SendServerMessage("useAction", data)

        return answer[0]