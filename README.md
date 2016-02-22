# front-keeper
Front-keeper is a basic web interface for passkeeper

This one user interface permit to manage passkeper throught a simple web interface. 

It include feacture : 

- Init : Initialize your git passkeeper project 
- Decrypt : Decrypt files encrypted using passkeeper
- Encrypt : Encrypt files password
- List : List all ini password files
- New : Add new ini password file
- Search : Search a content in your ini files

Configuration in settings.py :

PASSKEEPER_PATH : Path of the passkeeper directory (could permit to integrate an initialied one)

PASSKEEPER_ENCRYPT_STATE : Default encryption state of passkeeper (1 : encrypted, 0 : decrypted)

NB : Insure your frontkeeper is encrypted if it's not new one, by default passkeeper consider it's on encrypted state. You can also change it in settings.
