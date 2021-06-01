.PHONY: all

all:
	@docker run --rm -it -v `pwd`:/app python:3 sh -c "cd /app && pip install feedparser >/dev/null 2>&1 && python main.py"
