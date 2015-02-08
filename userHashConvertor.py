file_passwords = open('hash-password.txt', 'r')
#file2_users = open('user-hash.txt', 'r')
passwords = []
count = 0

for line in file_passwords:
        column = line.split(':')      
        column_hash_passwords_HASH = column[0]
        column_hash_passwords_HASH_Stripped = column_hash_passwords_HASH.strip('\r\n')
        
        column_hash_password_PASSWD = column[1]
        column_hash_password_PASSWD_Stripped = column_hash_password_PASSWD.strip('\r\n')

        passwords.append(column_hash_password_PASSWD_Stripped)
        count = count + 1
        #print(column_hash_passwords)

        file_users = open('user-hash.txt', 'r')

        for line2 in file_users:    
            #print(line2)
            column1 = line2.split(':')      
            column_users_hash_HASH = column1[1]
            column_users_hash_HASH_Stripped = column_users_hash_HASH.strip('\r\n')
            
            column_users_hash_USERS = column1[0]
            column_users_hash_USERS_Stripped = column_users_hash_USERS.strip('\r\n')
            #print("--"+column_hash_users)
            #print('ssss')
            
            if(column_hash_passwords_HASH_Stripped == column_users_hash_HASH_Stripped):
              #  print("match")
              #  print("MMM"+column_hash_passwords_HASH_Stripped)
                print("-- "+column_users_hash_USERS_Stripped + " - " + column_hash_passwords_HASH_Stripped + " - " + column_hash_password_PASSWD_Stripped )
              #  print("CCC"+column_users_hash_HASH_Stripped)
                break
                
               
print(passwords)

file_passwords.close()      
file_users.close()
