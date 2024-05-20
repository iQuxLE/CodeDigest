### Before:

```
export PROJECT_ROOT='/path/to/project'
export OUTPUT_FILE='output.txt'
export OPENAI_API_KEY='your_openai_api_key_here'
```

### Guide
```
poetry install
```

### Generate Function Descriptions:

```
poetry run python scripts/generate_function_descriptions.py
```

### Generate Project Tree:
```
poetry run python app/scripts/generate_tree.py
```

### Summarize Project Files:
```
poetry run python app/scripts/summarize_files.py
```

### Process entire project
```
poetry run python app/scripts/process.py
```

### For testing:

```
 export PYTHONPATH=$PYTHONPATH:$(pwd)/src 
 poetry run pytest 
```