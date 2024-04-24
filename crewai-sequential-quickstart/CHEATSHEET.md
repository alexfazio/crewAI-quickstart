
### Cheatsheet

- Reset poetry env:
```
poetry env remove python                                                    
poetry env use python
```

- Update poetry.lock and install dependencies:
```
poetry lock                                                   
poetry install
```

- Remove poetry env
```
exit
poetry env remove $(basename $(poetry env info --path))
```

- Remove poetry env
```
exit
poetry env remove $(basename $(poetry env info --path))
```

- Run from scratch:
```
mv ./poetry.lock ~/.Trash
poetry env remove python 
poetry env use python
poetry lock 
poetry install
poetry run crewai-linkedin-collab
```

- Run from scratch v2:
```
mv ./poetry.lock ~/.Trash
poetry env remove python 
poetry env use python
poetry lock 
poetry install
poetry run python main.py
```