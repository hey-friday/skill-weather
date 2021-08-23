import friday

# build our own custom skill
class ExampleSkill(friday.skill.FridaySkill):
    # method is called when skill is configured
    def config(self):
        conf_state = self.config_input.configuration.state
        data = self.config_input.configuration.data

        # check for initial state
        if conf_state == "FRIDAY.INIT":
            self.response.text = "Welcome to this example skill. What is your name?"
            self.response.configuration.state = "SETUP.QUESTION.NAME"

        # check for setup question state
        elif conf_state == "SETUP.QUESTION.NAME":
            self.response.text = "Welcome, " + data + ". I'll help you out from now on."
            self.response.configuration.state = "FRIDAY.FINISH"

    # method is called when skill is called
    def process(self):
        # print information about the command
        print("Command:")
        print(" Lang:", self.input.command.lang)
        print(" Content:", self.input.command.content)
        print(" Category:", self.input.command.category)
        print(" NER-Items:", self.input.command.ner_items, "\n")

        # print information about the context
        print("Context")
        print(" Interaction-Type:", self.input.context.interaction.type)
        print(" Device-Name:", self.input.context.device.name)
        print(" Room-Name:", self.input.context.room.name)
        print(" Payload:", self.input.context.payload)


# this is an example of how to use the friday-skill-api in python
if __name__ == '__main__':
    exampleSkill = ExampleSkill()