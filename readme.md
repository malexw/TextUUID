# TextUUID

TextUUID is a Sublime Text 3 plugin for generating UUIDs from text strings. TextUUID uses UUID version 5 to create deterministic identifiers for any namespace/string pair from that pair's SHA-1 hash.

## Usage

Suppose you wanted to create a UUID for a service called `login`. Select the phrase you would like to generate a UUID for, and run the `text_uuid` command.

```python
SERVICE_ID = 'login'

SERVICE_ID = '384ee5fc-87d6-5599-8b45-5ad4932525bc'
```

I prefer to include a comment to remind me what string I used to generate the UUID.

```python
SERVICE_ID = '384ee5fc-87d6-5599-8b45-5ad4932525bc' # login
```

TextUUID also includes a command for generating completely random UUIDs, called `random_uuid`

## Installation

To install TextUUID, copy the text_uuid.py file to your Sublime Text 3 user packages directory. You can find this directory via Preferences > Browse Packages from within Sublime Text 3.

## Configuration

Out of the box, the UUIDs generated from TextUUID are not deterministic. TextUUID needs a namespace to generate deterministic UUIDs, which is itself a UUID. TextUUID looks for a Sublime Text 3 setting called "namespace_uuid", whose value should be a string representation of a 32 character, base 16 number. e.g.:

```json
{
    "namespace_uuid": "73ca8ae1-96e1-4354-b7d1-cf8302565e55"
}
```

The `random_uuid` command generates UUIDs that would be suitable for a namespace.

You may also wish to set up key bindings for these commands. Under Preferences > Key Bindings - User, you could add settings like this:

```json
[
    {"keys": ["super+u"], "command": "text_uuid"},
    {"keys": ["ctrl+super+u"], "command": "random_uuid"}
]
```
