from enum import Enum

class ProjectStatus(str, Enum):
    STARTED   = "started"
    DEV       = "dev"
    BUILD     = "build"
    TEST      = "test"
    DEPLOYED  = "deployed"

class TaskStatus(str, Enum):
    ASSIGNED  = "Assigned"
    STARTED   = "Started"
    COMPLETED = "Completed"
