runapp:
	uvicorn src.main:app --reload
testapp:
	pytest
fmt:
	black ./
	isort ./