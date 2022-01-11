runapp:
	uvicorn src.main:app --reload
testapp:
	pytest
fmt:
	black ./
	isort ./
build:
	make fmt && docker-compose build && docker-compose up -d