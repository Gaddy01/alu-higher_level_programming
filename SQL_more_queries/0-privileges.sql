-- comment
#!/bin/bash
USERS = ('user_0d_1' 'user_0d_2')
HOST = 'localhost'

for USER in '${USERS[@]}'
do
	SHOW GRANTS FOR '$USER'@'$HOST';
done
