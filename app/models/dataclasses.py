from dataclasses import dataclass


@dataclass
class ApiInput:
    name: str


@dataclass
class ApiOutput:
    greeting: str
