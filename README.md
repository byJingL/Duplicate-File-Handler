# Duplicate File Handler
Duplicate File Handler is a useful tool that can free some space on your drive. It can check and compares files in a folder, displays the result, and removes duplicates.
## Main Skill
OS Module, Hash, Hash Table, hashlib module
## Theory
1. Check files with same size.
2. Check files with same hash.
## How to use
Warning: Once files are deleted, they are not in bin and can't be put back.
- Download [handler.py](/handler.py)
- Run [handler.py](/handler.py) with argument of which folder you want to check. eg. 
    ``` 
    python3 handler.py root_folder
    ```
- Follow the instruction of the program inputs:
  - `Enter file format` (optional): Empty input will check any file format.
  - `Size sorting options` (required): 1 or 2
  - `Check for duplicates? (yes or no)` (required): yes for checking no for not checking.
  - `Delete files? (yes or no)` (required): yes for deleting no for not deleting.
  - `Enter file numbers to delete` (required): numbers separated by spaces.

## Example
```
> python handler.py root_folder

Enter file format:
>>>

Size sorting options:
1. Descending
2. Ascending

Enter a sorting option:
>>> 1

5550640 bytes
root_folder/poker_face.mp3
root_folder/poker_face_copy.mp3

4590560 bytes
root_folder/gordon_ramsay_chicken_breast.avi
root_folder/audio/sia_snowman.mp3
root_folder/audio/rock/smells_like_teen_spirit.mp3

3422208 bytes
root_folder/audio/classic/unknown.mp3
root_folder/masterpiece/rick_astley_never_gonna_give_you_up.mp3

============================================
Check for duplicates? (yes or no)
>>> yes

5550640 bytes
Hash: 909ba4ad2bda46b10aac3c5b7f01abd5
1. root_folder/poker_face.mp3
2. root_folder/poker_face_copy.mp3

3422208 bytes
Hash: a7f5f35426b927411fc9231b56382173
3. root_folder/audio/classic/unknown.mp3
4. root_folder/masterpiece/rick_astley_never_gonna_give_you_up.mp3

============================================
Delete files? (yes or no)
>>> yes

Enter file numbers to delete:
>>> 8 10

Wrong format

Enter file numbers to delete:
>>> 1 2 4

Total freed up space: 14523488 bytes
```

## Disclaimer
The original learning materials and project ideas are from [JetBrains Academy](https://www.jetbrains.com/academy/). All codes were written by myself.