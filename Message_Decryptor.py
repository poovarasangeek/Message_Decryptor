def bin_to_str(binary):
    decrypted_message=""
    byte_list=binary.split()
    for byte in byte_list:
        chr_=int(byte,2)
        decrypted_message+=chr(chr_)
    print("\nHere this is your decrypted message:\n",decrypted_message)   
    
user_input=input("\nEnter the encrypted message to decrypt:\n")    
bin_to_str(user_input) 