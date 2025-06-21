from pydantic import BaseModel  # type: ignore


class Person(BaseModel):
    id: int
    name: str

    def upper(self) -> str:
        return self.name.upper()


p = Person(id=42, name="Siu Yin")
print(p)
print(p.model_dump_json())
d = p.model_dump()
print(d["id"])
