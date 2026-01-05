Use:
```
git update-index --assume-unchanged compose.yaml
```
When you want pull / push to make no changes to a file.
Usually, .gitignore works, but this is for when you already
have a file tracked locally and remotely but want to keep
separate copies in these locations.

You can also undo it like this:
```
git update-index --no-assume-unchanged path/to/your/file
```
