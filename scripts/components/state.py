class State:
    """One state's behavior. Make a subclass per state and override update()
    (and optionally enter()/exit()). `name` is the string the handler stores it under."""

    def __init__(self, name):
        self.name = name
        self.handler = None  # set by StateHandler.add_state()

    @property
    def entity(self):
        # convenience: reach the entity the state machine is attached to
        return self.handler.entity

    def enter(self):
        """Called once when we switch INTO this state (reset timers, swap color)."""
        pass

    def exit(self):
        """Called once when we switch OUT of this state."""
        pass

    def update(self):
        """Runs every frame while this is the current state."""
        pass