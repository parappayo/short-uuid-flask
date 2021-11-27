import base64
import uuid


def generate():
    return base64.urlsafe_b64encode(uuid.uuid4().bytes).decode('utf-8')[:-2]


if __name__ == "__main__":
	print(generate())
	bleh = uuid.uuid4().hex
	print(bleh)
	print(len(bleh))
